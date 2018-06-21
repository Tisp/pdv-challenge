from flask import Flask, jsonify, request
from ze_delivery.model.pdv import Pdv


app = Flask(__name__)


@app.route('/')
def get_index():
    return __name__
