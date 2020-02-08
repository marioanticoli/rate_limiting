from flask import Flask

app = Flask(__name__)

from app import routes

from waitress import serve
serve(app, host="0.0.0.0", port=8080)