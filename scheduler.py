
from app import test
from app import config
import time

import schedule

def job():
    print "Running test:", time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    test.run_test()

schedule.every(15).minutes.do(job)
#schedule.every().hour.at(':00').do(job)

while True:
    schedule.run_pending()
    time.sleep(0.2)
