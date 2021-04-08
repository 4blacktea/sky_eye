#!/usr/bin/python
# -*- coding: UTF-8 -*-


import nmap
import sys
import datetime
import mysql.connector


main_domain = ''


# 获取参数
if len(sys.argv) > 1:
    main_domain = sys.argv[1]
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


# 端口扫描
def nmap_A_scan(network_prefix,main_domain):
    res_tol = []
    nm = nmap.PortScanner()
    print('starting   ' + network_prefix, flush=True)
    # 配置nmap扫描参数
    scan_raw_result = nm.scan(network_prefix, '1-65535')
    print('started   ' + network_prefix, flush=True)
    print(scan_raw_result)
    # 分析扫描结果
    for host, result in scan_raw_result['scan'].items():
        
        if result['status']['state'] == 'up':
            try:
                for port in result['tcp']:
                    try:
                        res_tu = [0,network_prefix,main_domain,"-"]
                        res_tu.append(port)
                        try:
                            res_tu.append(result['tcp'][port]['name'])
                        except:
                            res_tu.append("-")
                        try:
                            if len(result['tcp'][port]['version'])==0:
                                res_tu.append("-")
                            else:
                                res_tu.append(result['tcp'][port]['version'])
                        except:
                            res_tu.append("-")
                        try:
                            res_tu.append(result['tcp'][port]['state'])
                        except:
                            res_tu.append("-")
                        res_tu.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                        res_tu.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    except:
                        pass
                    res_tol.append(res_tu)
            except:
                pass


    mycursor,mydb = my_mysql()
    exit_port  = []
    select_sql = "select port from port where domain=%s"
    mycursor.execute(select_sql,(network_prefix,))
    myresult = mycursor.fetchall()
    for x in myresult:
        exit_port.append(x[0])
    insert_sql = "INSERT INTO port (id, domain, main_domain, domain_group, port, protocol, p_version, p_status, createtime, updatetime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    for i in res_tol:
        print(exit_port)
        if i[4] in exit_port:
            updata_sql = "UPDATE port set updatetime=%s where domain=%s and port=%s"
            mycursor.execute(updata_sql,(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),i[1],i[4]))
            mydb.commit()
            continue
        mycursor.execute(insert_sql,tuple(i))
        mydb.commit()
    mycursor.close()
    mydb.close()
    return res_tol


# 获取域名列表
def get_ips():
    ips = []
    mycursor,mydb = my_mysql()
    select_sql = "select domain from domain where main_domain=%s"
    mycursor.execute(select_sql,(main_domain,))
    myresult = mycursor.fetchall()
    for x in myresult:
        ips.append(x[0])
    return ips


if __name__ == '__main__':
    print('start port scan', flush=True)
    for domain in get_ips():
        nmap_A_scan(domain,main_domain)
    print('end port scan', flush=True)
