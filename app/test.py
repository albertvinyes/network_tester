from controllers.manager import controller as manager
from controllers.netspeed import controller as netspeed

def run_test():
    results = netspeed.run_test()
    manager.store_results(results)

if __name__ == '__main__':
    run_test()
