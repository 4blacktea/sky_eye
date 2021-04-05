from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.combining import OrTrigger
import os
import mysql.connector


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


# 加载定时任务配置
def get_corn():
    mycursor,mydb = my_mysql()
    cron_rules = []
    select_sql = "select * from monitor where is_open=%s"
    mycursor.execute(select_sql,("true",))
    myresult = mycursor.fetchall()
    for x in myresult:
        cron_rules.append(x[0])
    return cron_rules




def run():
    os.system("./run.sh megvii.com")

crons = get_corn():
forn cron_s in crons:
    if cron_s[3] == "crontab"
    sched = BlockingScheduler()
    sched.add_job(run, CronTrigger.from_crontab(cron_s[4]))
    sched.start()

