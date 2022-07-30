from flask import Flask, request
from flask_migrate import Migrate

from app.config import Config


app = Flask(__name__) 

