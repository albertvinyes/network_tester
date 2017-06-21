from manager import controller as manager
from netspeed import controller as netspeed

manager.erase_results()
results = netspeed.run_test()
manager.store_results(results)
manager.print_results()
