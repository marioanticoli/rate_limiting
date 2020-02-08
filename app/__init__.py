from flask import Flask

app = Flask(__name__)

from app import routes

from waitress import serve
serve(app, host="127.0.0.1", port=8080)