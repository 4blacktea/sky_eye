from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.combining import OrTrigger
import os

def run():
    os.system("./run.sh megvii.com")

sched = BlockingScheduler()
sched.add_job(run, CronTrigger.from_crontab('5 3 * * *'))
sched.start()

