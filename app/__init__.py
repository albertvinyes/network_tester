from flask import Flask

app = Flask(__name__)

from app.netspeed.controller import netspeed as netspeed_module
from app.manager.controller import manager as management_module
from app.views.controller import views as views_module

app.register_blueprint(views_module)
app.register_blueprint(netspeed_module)
app.register_blueprint(management_module)
