from flask import render_template
from . import main

@main.route('/')
def index():
    render render_template('index.html')
