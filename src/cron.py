from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.combining import OrTrigger

def job_function():
        print("Hello World")

sched = BlockingScheduler()
sched.add_job(job_function, CronTrigger.from_crontab('15 2 * * *'))
sched.start()

