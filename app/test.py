from manager import controller as manager
from netspeed import controller as netspeed

manager.erase_results()
netspeed.run_test(1)
manager.print_results()
