import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from app.untils.log_builder import sys_logging
import os


scheduler = BlockingScheduler()   # 后台运行

# 设置为每日15:30:30时执行一次调度程序
@scheduler.scheduled_job("cron", day_of_week='*', hour='15', minute='30', second='30')
def run():
    os.system("./run.sh megvii.com")


if __name__ == '__main__':
    try:
        scheduler.start()
        sys_logging.debug("statistic scheduler start success")
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        sys_logging.debug("statistic scheduler start-up fail")
