from flask import Flask
entry_point = Flask(__name__)
from app_entry import routes
