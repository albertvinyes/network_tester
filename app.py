from pymongo import MongoClient
import datetime
import re
import subprocess
import sys

client = MongoClient('localhost', 27017)

def latency_test():
    n = "20"
    host = "8.8.8.8"
    ps = subprocess.Popen(('ping', '-i', '0.2','-c', n, host), stdout=subprocess.PIPE)
    output = subprocess.check_output(("awk", "-F", "/", "END {print $5}"), stdin=ps.stdout)
    ps.stdout.close()
    return output

def bandwidth_test():
    r = subprocess.check_output(["speedtest-cli", "--simple"]).split("\n")
    l = [None] * 3
    l[0] = r[1].split(":")[1][1:]
    l[1] = r[2].split(":")[1][1:]
    l[2] = r[0].split(":")[1][1:]
    return l

def main():
    n = int(sys.argv[1])
    max_down = max_up = avg_latency = 0
    for index in range(n):
        print "Running test number", index+1, "..."
        run = bandwidth_test()
        nums = re.findall(r'([\d.]+)', str(run))
        if (float(nums[0]) > max_down):
            max_down = float(nums[0])
        if (float(nums[1]) > max_up):
            max_up = float(nums[1])
        avg_latency += float(latency_test())
    avg_latency /= n
    print "Download: ", str(max_down), " Upload: ", str(max_up), " Latency: ", str(avg_latency)
    # TODO: Build JSON containing the date and results
    # TODO: Store JSON in Database
    # db = client.database
    # hosts = db.host_collection
    # t = hosts.update_one(
    #                     {"email": email},
    #                     {"$addToSet": {"hosts": {"host_name": host_name, "host_nickname": host_nickname, "notified": False}}})

if __name__ == "__main__":
    main()
