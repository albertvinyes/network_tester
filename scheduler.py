
from app.controllers.manager import controller as manager
from app import test
from app import config
import time
import schedule

results = list(manager.get_results())

if len(results) == 2:
    print('There are no tests in the Database! Running initial test...')
    test.run_test()
else:
    print('Starting Scheduler! Network Tests will run automatically')

def job():
    print("Running test:", time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
    test.run_test()

schedule.every(15).minutes.do(job)
#schedule.every().hour.at(':00').do(job)

while True:
    schedule.run_pending()
    time.sleep(0.2)
