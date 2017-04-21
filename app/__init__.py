from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
#app.config.from_object('config')
client = MongoClient('localhost', 27017)

from app.netspeed.controller import netspeed as netspeed_module
app.register_blueprint(netspeed_module)
