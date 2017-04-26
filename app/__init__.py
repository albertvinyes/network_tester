from flask import Flask

app = Flask(__name__)
#app.config.from_object('config')

from app.netspeed.controller import netspeed as netspeed_module
app.register_blueprint(netspeed_module)
