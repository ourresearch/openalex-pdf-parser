from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["JSON_SORT_KEYS"] = False
