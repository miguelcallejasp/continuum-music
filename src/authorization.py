import requests
import logging
import sys
import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

def auth_flow():
    uri='https://accounts.spotify.com/authorize?client_id=e274800bab804d90862360fe3363a785&response_type=code&redirect_uri=http%3A%2F%2Flocalhost:8080%2Fcallback&scope=user-read-private%20user-read-email'
    r = requests.get(uri)
    print(r.content)
    print(r.status_code)
    print(r.headers)
    return r

@app.route('/v1/auth', methods=["GET"])
def start():
    #Validation
    next = auth_flow()

    return next.content, next.status_code

@app.route('/callback', methods=["GET"])
def callback():
    #Validation
    return "callback here", 200

if __name__ == '__main__':
    logging.info("Starting Service")
    app.run(host='0.0.0.0', port=8080, debug=True)
