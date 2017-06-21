
from app import test
from app import config

import schedule

def job():
    test.run_test()

schedule.every().hour.do(job)

while True:
    schedule.run_pending()
