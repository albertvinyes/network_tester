from flask import Flask, render_template
from flask import Blueprint
from app import config

views = Blueprint('views', __name__)

@views.route('/')
def main():
    return render_template('index.html', port=config.PORT)
