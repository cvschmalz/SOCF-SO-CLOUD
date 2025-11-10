from flask import Flask
import json

APP = Flask(__name__)

@APP.get("/info")
def info():
    return json.dumps([
        {
            'integrantes': [
                'Christine von Schmalz'
            ]
        }
    ])
