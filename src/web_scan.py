#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import base64
import requests
import time
import signal
import subprocess
import platform
import mysql.connector
import datetime
import sys

'''

# 想将字符串转编码成base64,要先将字符串转换成二进制数据
url = "https://www.cnblogs.com/songzhixue/"
bytes_url = url.encode("utf-8")
str_url = base64.b64encode(bytes_url)  # 被编码的参数必须是二进制数据
print(str_url)

b'aHR0cHM6Ly93d3cuY25ibG9ncy5jb20vc29uZ3poaXh1ZS8='


# 将base64解码成字符串
import base64
url = "aHR0cHM6Ly93d3cuY25ibG9ncy5jb20vc29uZ3poaXh1ZS8="
str_url = base64.b64decode(url).decode("utf-8")
print(str_url)

'https://www.cnblogs.com/songzhixue/'


'''

cmd = "google-chrome --headless --disable-gpu  --no-sandbox  --window-size=1920,1080 --screenshot=%s %s"

main_domain = 'qschou.com'
if len(sys.argv) > 1:
    main_domain = sys.argv[1]
else:
    raise RuntimeError('args error')


# 数据库连接
def my_mysql():
    mydb = mysql.connector.connect(
        host="10.10.10.2",            # 数据库主机地址
        user="root",               # 数据库用户名
        passwd="adminermysql",   # 数据库密码
        database="sky_eye"          
    )
    mycursor = mydb.cursor(buffered=True)
    return mycursor,mydb


# 带有timeout机制的稳定的os命令执行库
def run_cmd(cmd_string, timeout=10):
    print("命令为：" + cmd_string)
    p = subprocess.Popen(cmd_string, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True, close_fds=True,
                         start_new_session=True)
 
    format = 'utf-8'
    if platform.system() == "Windows":
        format = 'gbk'
 
    try:
        (msg, errs) = p.communicate(timeout=timeout)
        ret_code = p.poll()
        if ret_code:
            code = 1
            msg = "[Error]Called Error ： " + str(msg.decode(format))
        else:
            code = 0
            msg = str(msg.decode(format))
    except subprocess.TimeoutExpired:
        # 注意：不能只使用p.kill和p.terminate，无法杀干净所有的子进程，需要使用os.killpg
        p.kill()
        p.terminate()
        os.killpg(p.pid, signal.SIGTERM)
 
        # 注意：如果开启下面这两行的话，会等到执行完成才报超时错误，但是可以输出执行结果
        # (outs, errs) = p.communicate()
        # print(outs.decode('utf-8'))
 
        code = 1
        msg = "[ERROR]Timeout Error : Command '" + cmd_string + "' timed out after " + str(timeout) + " seconds"
    except Exception as e:
        code = 1
        msg = "[ERROR]Unknown Error : " + str(e)
 
    return code, msg


def judge_http(url):
    starttime= time.time()
    try:
        r = requests.get(url,timeout=10)
        print("*********get time" + str(time.time()-starttime))
        return True
    except:
        return False

def cut_screen(url, domain, port, protocol):
    #print(str(base64.b64encode(url.encode("utf-8")),encoding="utf-8")+".png")
    if judge_http(url):
        print(url + "___________success")
        starttime= time.time()
        #run_cmd(cmd % ("./result_pic/pics/"+str(base64.b64encode(url.encode("utf-8")),encoding="utf-8")+".png",url))
        #run_cmd(cmd % ("mkdir ")
        run_cmd(cmd % ("./result_pic/pics/"+str(base64.b64encode(url.encode("utf-8")),encoding="utf-8")+".png",url))
        run_cmd("chmod 777 /www/wwwroot/www/pics/*")
        mycursor,mydb = my_mysql()

        exit_url = []
        select_sql = "select web_url from web where domain=%s"
        #print domain
        mycursor.execute(select_sql,(domain,))
        myresult = mycursor.fetchall()
        for x in myresult:
            exit_url.append(x[0])
            #print "####"
            #print x[0]
            #print exit_url


        if url in exit_url:
            updata_sql_1 = "UPDATE web_result set updatetime=%s where web_url=%s "
            #mycursor.execute(updata_sql_1,(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),url))
            mycursor.execute(updata_sql_1,(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),url))
            mydb.commit()
            #print "__________________++++++++++++++++++__________________"
        else:
            insert_sql = "INSERT INTO web (id, domain, web_port, http_protocol, web_url, finger, screen_pic, creattime, updatetime, ext) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            mycursor.execute(insert_sql,(0,domain,port,protocol,url,"unknown finger","/pics/"+str(base64.b64encode(url.encode("utf-8")),encoding="utf-8")+".png",datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"-"))
            mydb.commit()
            mycursor.close()
            mydb.close()
            print("*********cut time" + str(time.time()-starttime))
    else:
        print(url + "__________________  NET ERR")
        pass





def get_ips():
    f = open("/root/code-server-3.4.1-linux-x86_64/workspace/skyeye/result/domains_result.txt", "r")
    ips_raw = f.readlines()
    ips = [ ip.strip() for ip in ips_raw ]
    return ips


def get_ips2():
    urls = []
    mycursor,mydb = my_mysql()
    #select_sql = 'select protocol,domain,port from port_result where (protocol="http" or "protocol=https") and p_status="open" and main_domain=%s'
    select_sql = 'select protocol,domain,port from port where p_status="open" and main_domain=%s'
    mycursor.execute(select_sql,(main_domain,))
    myresult = mycursor.fetchall()
    for x in myresult:
        if x[0] == "http" or x[0] == "https":
            print(x)
            urls.append((x[1],x[0]+"://"+x[1]+":"+str(x[2]),x[2],x[0]))
        else:
            urls.append((x[1],"http"+"://"+x[1]+":"+str(x[2]),x[2],"http"))
            urls.append((x[1],"https"+"://"+x[1]+":"+str(x[2]),x[2],"https"))
    return urls



def test():
    urls = get_ips2()
    for url in urls:
        cut_screen(url[1],url[0],url[2],url[0])
        print("\n")
    run_cmd("chmod 777 /www/wwwroot/www/pics/*")

#test()
test()
