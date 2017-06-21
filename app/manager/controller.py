from flask import Flask, flash, request, json, redirect, Blueprint
from pymongo import MongoClient
from bson.json_util import loads, dumps
import datetime
import httplib
import pprint
import re
import subprocess
import sys

client = MongoClient('localhost', 27017)

manager = Blueprint('manager', __name__)

@manager.route("/get_all_results", methods=['GET'])
def get_results():
    db = client.database
    network_results = db.network_results_collection.find()
    return dumps(network_results)

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
