from flask import Blueprint
import datetime
import httplib
import pprint
import re
import subprocess
import sys

netspeed = Blueprint('netspeed', __name__)


def connected_to_internet():
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False

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
    return l

def run_test(n):
    max_down = max_up = avg_latency = 0.0
    t = datetime.datetime.now()
    t = t.strftime("%Y-%m-%d %H:%M")
    b = connected_to_internet()
    if (b):
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
        results = {"time": t, "download": max_down, "upload": max_up, "latency": avg_latency}
    else:
        results = {"time": t, "download": -1, "upload": -1, "latency": -1}
    db = client.database
    network_results = db.network_results_collection
    t = network_results.insert_one(results)
