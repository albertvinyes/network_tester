from flask import Flask, render_template
from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def main():
    return render_template('index.html')
