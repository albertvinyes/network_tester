from flask import Blueprint
import pyspeedtest
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
    st = pyspeedtest.SpeedTest()
    l = [None] * 2
    d = st.download()
    u = st.upload()
    l[0] = d
    l[1] = u
    return l

@netspeed.route("/run_test", methods=['GET'])
def run_test():
    # TODO: keep just 4 decimals
    max_down = max_up = avg_latency = 0.0
    t = datetime.datetime.now()
    t = t.strftime("%Y-%m-%d %H:%M")
    b = connected_to_internet()
    if (b):
        nums = bandwidth_test()
        max_down = float(nums[0])
        max_up = float(nums[1])
        latency = float(latency_test())
        results = {"time": t, "download": max_down, "upload": max_up, "latency": latency}
    else:
        results = {"time": t, "download": -1, "upload": -1, "latency": -1}
    return results
