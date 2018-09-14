from flask import Blueprint
from bson.json_util import dumps
import speedtest
import datetime
import http.client
import pprint
import re
import subprocess
import sys

analyzer = Blueprint('netspeed', __name__)

def connected_to_internet():
    conn = http.client.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False

def latency_google_test():
    n = "20"
    host = "8.8.8.8"
    ps = subprocess.Popen(('ping', '-i', '0.2','-c', n, host), stdout=subprocess.PIPE)
    output = subprocess.check_output(("awk", "-F", "/", "END {print $5}"), stdin=ps.stdout)[:-1]
    ps.stdout.close()
    return output.decode("utf-8")

def speed_test():
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    st = s.results.dict()
    l = [None] * 3
    l[0] = st['download']
    l[1] = st['upload']
    l[2] = st['ping']
    return l

@analyzer.route("/run_test", methods=['GET'])
def run_test():
    # TODO: keep just 4 decimals
    t = datetime.datetime.now()
    t = t.strftime("%Y-%m-%d %H:%M")
    b = connected_to_internet()
    if (b):
        nums = speed_test()
        latency_google = latency_google_test()
        results = {
                    "time": t,
                    "download": nums[0],
                    "upload": nums[1],
                    "latency_google": latency_google,
                    "latency_speednet": nums[2]
                }
    else:
        results = {
                    "time": t,
                    "download": -1,
                    "upload": -1,
                    "latency_google": -1,
                    "latency_speednet": -1
                }
    return dumps(results)
