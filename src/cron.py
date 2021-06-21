from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.combining import OrTrigger
import os
import mysql.connector
import time


# 数据库连接
# 解决了mysql启动前脚本启动导致崩溃问题
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




# 加载定时任务配置
def get_corn():
    mycursor,mydb = my_mysql()
    cron_rules = []
    select_sql = "select * from monitor where is_open=%s"
    mycursor.execute(select_sql,("true",))
    myresult = mycursor.fetchall()
    print(myresult, flush=True)
    for x in myresult:
        print(x, flush=True)
        cron_rules.append(x)
    return cron_rules


def run(main_domain):
    os.system("./run.sh " + main_domain)

    
print("Hello? Anyone there?", flush=True)
while True:
    crons = []
    while True:
        try:
            crons = get_corn()
            break
        except:
            time.sleep(3)
    for cron_s in crons:
        print(crons, flush=True)
        print(cron_s, flush=True)
        if cron_s[3] == "crontab":
            sched = BackgroundScheduler()
            sched.add_job(run, CronTrigger.from_crontab(cron_s[4]), args=[cron_s[2]])
            sched.start()
    time.sleep(86400)

