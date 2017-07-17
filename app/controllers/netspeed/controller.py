from flask import Blueprint
from bson.json_util import dumps
import pyspeedtest
import datetime
import http.client
import pprint
import re
import subprocess
import sys

netspeed = Blueprint('netspeed', __name__)

def connected_to_internet():
    conn = http.client.HTTPConnection("www.google.com", timeout=5)
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
    output = subprocess.check_output(("awk", "-F", "/", "END {print $5}"), stdin=ps.stdout)[:-1]
    ps.stdout.close()
    return output.decode("utf-8") 

def bandwidth_test():
    st = pyspeedtest.SpeedTest()
    l = [None] * 2
    l[0] = st.download()
    l[1] = st.upload()
    return l

@netspeed.route("/run_test", methods=['GET'])
def run_test():
    # TODO: keep just 4 decimals
    t = datetime.datetime.now()
    t = t.strftime("%Y-%m-%d %H:%M")
    b = connected_to_internet()
    if (b):
        nums = bandwidth_test()
        latency = latency_test()
        results = {"time": t, "download": nums[0], "upload": nums[1], "latency": latency}
    else:
        results = {"time": t, "download": -1, "upload": -1, "latency": -1}
    return dumps(results)
