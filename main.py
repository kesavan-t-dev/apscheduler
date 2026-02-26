from scheduler import initialize_scheduler
import time

def hello_job():
    print("Hello, APScheduler!")

scheduler = initialize_scheduler()
scheduler.add_job(hello_job, 'interval', seconds=5)

try:
    # Keep the main thread alive to allow the scheduler to run
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
