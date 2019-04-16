# __init__.py
# initialize Falsk's app

from flask import Flask
from app import views

app = Flask(__name__)
