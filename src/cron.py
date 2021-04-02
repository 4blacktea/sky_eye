import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import os


scheduler = BlockingScheduler()   # 后台运行

# 设置为每日15:30:30时执行一次调度程序
@scheduler.scheduled_job("cron", day_of_week='*', hour='17', minute='30', second='35')
def run():
    os.system("./run.sh megvii.com")


if __name__ == '__main__':
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
