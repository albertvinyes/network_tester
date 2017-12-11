from flask import Blueprint
from bson.json_util import dumps, loads
from pymongo import MongoClient
import pprint

client = MongoClient('localhost', 27017)

miner = Blueprint('miner', __name__)

def cumulative_average(n, prev, v):
    avg = ((prev * n) + v) / (n+1)
    return(avg)

def format_stats(values):
    d = {
        "id": "stats",
        "max_download": str(values[0]),
        "min_download": str(values[1]),
        "avg_download": str(values[2]),
        "max_upload": str(values[3]),
        "min_upload": str(values[4]),
        "avg_upload": str(values[5]),
        "max_latency": str(values[6]),
        "min_latency": str(values[7]),
        "avg_latency": str(values[8]),
        "count": str(values[9])
    }
    return(d)

def update_stats(results):
    try:
        db = client.database
        stats_db = db.stats_collection
        stats = db.stats_collection.find_one()
        n = db.stats_collection.count()
        values = [None] * 10
        results = loads(results)
        print(n)
        if (n == 0):
            values[0], values[1], values[2] = (results["download"], )*3
            values[3], values[4], values[5] = (results["upload"], )*3
            values[6], values[7], values[8] = (results["latency_google"], )*3
            values[9] = 1
            d = format_stats(values)
            stats_db.insert_one(d)
        else:
            values[0] = max(float(results["download"]), float(stats["max_download"]))
            values[1] = min(float(results["download"]), float(stats["min_download"]))
            values[2] = cumulative_average(n, float(stats["avg_download"]), float(results["download"]))
            values[3] = max(float(results["upload"]), float(stats["max_upload"]))
            values[4] = min(float(results["upload"]), float(stats["min_upload"]))
            values[5] = cumulative_average(n, float(stats["avg_upload"]), float(results["upload"]))
            values[6] = max(float(results["latency_google"]), float(stats["max_latency"]))
            values[7] = min(float(results["latency_google"]), float(stats["min_latency"]))
            values[8] = cumulative_average(n, float(stats["avg_latency"]), float(results["latency_google"]))
            values[9] = float(stats["count"])+1.0
            d = format_stats(values)
            stats_db.update_one({"id": "stats"}, {"$set": d})
        return "Success"
    except:
        raise
        return("Error updating stats", 500)

@miner.route("/get_stats", methods=['GET'])
def get_stats():
    try:
        db = client.database
        stats = db.stats_collection.find_one({},{"id":0, "_id":0})
        return dumps(stats)
    except:
        raise
        return("Error getting results", 500)
