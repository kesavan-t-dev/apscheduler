from apscheduler.schedulers.background import BackgroundScheduler
import time

def cron_task():
    print(f"Cron job executed at: {time.strftime('%H:%M:%S')}")

scheduler = BackgroundScheduler()
scheduler.start()

#make this job run at the 5 second for every minute
scheduler.add_job(cron_task, 'cron', second='*/5')


print("Job will execute at the 5-second mark in a minute")
print("Press Ctrl+C to exit")

try:
    while True:
        time.sleep(0.5)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
