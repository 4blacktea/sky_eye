#!/usr/bin/python
# -*- coding: UTF-8 -*-


from gevent import monkey
import requests
import gevent
from gevent import Timeout
import dns.resolver
from time import *
import datetime
import mysql.connector
import sys
try:
    from gevent.coros import RLock, Semaphore
except:
    from gevent.lock import RLock, Semaphore


monkey.patch_all()
domains = []
# 协程信号量，1000
sem = Semaphore(1000)
# 域名
domain = ''
# 字典位置
dict_path = './dicts/dict_subdomain.txt'
# 需要排除的反向代理ip池
nginx_ips = ['203.107.45.163']
# 获取参数
if len(sys.argv) > 1:
    domain = sys.argv[1]
else:
    raise RuntimeError('args error')


# 数据库连接
def my_mysql():
    mydb = mysql.connector.connect(
        host="10.10.10.2",       # 数据库主机地址
        port=3306,
        user="root",    # 数据库用户名
        passwd="adminermysql",   # 数据库密码
        database="sky_eye"
    )
    mycursor = mydb.cursor(buffered=True)
    return mycursor,mydb


# dns解析
def dns_query(domain, type):
    A_list = []
    try:
        dnsquery = dns.resolver.resolve(domain, type)
        for i in dnsquery.response.answer:
            for j in i:
                if str(j).strip() not in nginx_ips:
                    pass
                    A_list.append(str(j))
    except:
        pass
    return A_list


# 获取a记录
def get_A(domain):
    return dns_query(domain, 'A')


# 加载字典
def get_dict():
    f = open(dict_path,'r')
    dicts_raw = f.readlines()
    f.close()
    dicts = [i.strip() for i in dicts_raw]
    return dicts


# 协程调用
def coroutine(sub_domain,main_domain):
    domain = sub_domain + '.' + main_domain
    sem.acquire()
    ## 判断泛解析，最好挪到循环外
    A_ng = get_A("wdqdqwdqwd13dqw32rfewg." + main_domain)
    A_list = get_A(domain)
    # 判断是否有A记录，目前还有点坑，cname也会被记到这
    if len(A_list) != 0:
        A_list.sort()
        A_ng.sort()
        print(A_list, flush=True)
        print(A_ng, flush=True)
        if A_list == A_ng:
            pass
        else:
            domains.append(domain)
    sem.release()


# 协程扫描
def scan():
    sub_domains = get_dict()
    gevent.joinall([gevent.spawn(coroutine, sub_domain, domain) for sub_domain in sub_domains])


# 入口
if __name__ == '__main__':
    print('start subdomain scan', flush=True)
    t1 = time()         
    scan()
    t2 = time()
    mycursor,mydb = my_mysql()
    exit_domain = []
    select_sql = "select domain from domain"
    mycursor.execute(select_sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        exit_domain.append(x[0])
    for i in domains:
        if i in exit_domain:
            updata_sql = "UPDATE domain set updatetime=%s where domain=%s"
            mycursor.execute(updata_sql,(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),i))
            mydb.commit()
            continue
        insert_sql = "INSERT INTO domain (id, domain, main_domain, domain_group, createtime, updatetime) VALUES (%s, %s, %s, %s, %s, %s)"
        mycursor.execute(insert_sql,(0,i,domain,"KS",datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        mydb.commit()
    mycursor.close()
    mydb.close()
    print("耗时：" + str(t2 - t1) + "s", flush=True)
