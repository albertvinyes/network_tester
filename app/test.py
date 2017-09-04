from controllers.manager import controller as manager
from controllers.analyzer import controller as analyzer

def run_test():
    results = analyzer.run_test()
    manager.store_results(results)
    print(results)

if __name__ == '__main__':
    run_test()
