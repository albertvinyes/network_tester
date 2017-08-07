from flask import Flask
from app.controllers.analyzer.controller import analyzer as analysis_module
from app.controllers.manager.controller import manager as management_module
from app.controllers.views.controller import views as views_module

app = Flask(__name__)
app.register_blueprint(views_module)
app.register_blueprint(analysis_module)
app.register_blueprint(management_module)
