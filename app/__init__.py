from flask import Flask

app = Flask(__name__)

from app.controllers.netspeed.controller import netspeed as netspeed_module
from app.controllers.manager.controller import manager as management_module
from app.controllers.views.controller import views as views_module

app.register_blueprint(views_module)
app.register_blueprint(netspeed_module)
app.register_blueprint(management_module)
