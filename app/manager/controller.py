from flask import Flask, flash, request, json, redirect, Blueprint
from pymongo import MongoClient
from bson.json_util import loads, dumps
import json
import datetime
import httplib
import pprint
import re
import subprocess
import sys

client = MongoClient('localhost', 27017)

manager = Blueprint('manager', __name__)

@manager.route("/set_desired_qos", methods=['POST'])
def set_desired_qos():
    try:
        db = client.database
        qos = db.qos_collection
        data = json.loads(request.data)
        d = {
            "id": "desired_qos",
            "download": data["download"],
            "upload": data["upload"],
            "latency": data["latency"]
        }
        n = db.qos_collection.count()
        if (n == 0):
            qos.insert_one(d)
        else:
            qos.update_one({"id": "desired_qos"}, {"$set": d})
        return "Success"
    except:
        raise
        return("Error setting desired QoS", 500)

@manager.route("/get_desired_qos", methods=['GET'])
def get_desired_qos():
    try:
        db = client.database
        qos = db.qos_collection.find_one()
        qos.pop("id", 0)
        qos.pop("_id", 0)
        return dumps(qos)
    except:
        raise
        return("Error getting desired QoS", 500)

@manager.route("/get_all_results", methods=['GET'])
def get_results():
    try:
        db = client.database
        network_results = db.network_results_collection.find()
        return dumps(network_results)
    except:
        return("Error getting results", 500)

@manager.route("/delete_results", methods=['DELETE'])
def erase_results():
    try:
        db = client.database
        db.network_results_collection.remove()
        return("Results removed", 200)
    except:
        return("Error removing results", 400)

def store_results(res):
    try:
        db = client.database
        network_results = db.network_results_collection
        t = network_results.insert_one(loads(res))
        return True
    except:
        raise


def print_results():
    try:
        db = client.database
        network_results = db.network_results_collection
        for result in network_results.find():
            pprint.pprint(result)
        return True
    except:
        return False
