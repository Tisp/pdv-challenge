from flask import Flask, request
from pymongo import MongoClient
from mongoframes import *
from pdv_challenge.http.controller import PdvController

## Flask App ##
app = Flask(__name__)
app.config.from_object('pdv_challenge.settings.config.{}'.format(app.config['ENV']))

## Mongo Conection ##
app.mongo = MongoClient(app.config['MONGO_URI'])
Frame._client = app.mongo

#### Routes ####
@app.route('/')
def get_index():
    return 'Hello to {} API'.format(app.config['APP_NAME'])


@app.route('/pdv', methods=['POST'])
@app.route('/pdv/<id>', methods=['GET'])
def get_pdv(id=None):
    if request.method == 'POST':
        return PdvController.create_pdv(request.get_json())

    return PdvController.get_pdv_by_id(id)


@app.route('/search')
def get_near_pdv():
    lat = request.args.get('lat', default=None, type=float)
    lng = request.args.get('lng', default=None, type=float)

    return PdvController.get_near_pdv(lat, lng)



