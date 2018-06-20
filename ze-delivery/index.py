from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def get_index():
    return __name__
