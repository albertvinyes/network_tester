from app.controllers.manager import controller as manager
from app.controllers.analyzer import controller as analyzer
from app.controllers.miner import controller as miner

def run_test():
    results = analyzer.run_test()
    print(results)
    manager.store_results(results)
    miner.update_stats(results)

if __name__ == '__main__':
    run_test()
