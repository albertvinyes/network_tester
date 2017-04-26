from flask import Flask, flash, request, json, redirect, Blueprint
from pymongo import MongoClient
import datetime
import httplib
import pprint
import re
import subprocess
import sys

client = MongoClient('localhost', 27017)

manager = Blueprint('manager', __name__)

def get_results():
    db = client.database
    network_results = db.network_results_collection.find()
    return network_results

def erase_results():
    try:
        db = client.database
        db.network_results_collection.remove()
        return True
    except:
        return False

def print_results():
    try:
        db = client.database
        network_results = db.network_results_collection
        for result in network_results.find():
            pprint.pprint(result)
        return True
    except:
        return False
