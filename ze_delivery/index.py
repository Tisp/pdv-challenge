from flask import Flask, jsonify, request
from pymongo import MongoClient
from mongoframes import *
from ze_delivery.model.pdv import Pdv

## Flask App ##
app = Flask(__name__)
app.config.from_object('ze_delivery.settings.config.{}'.format(app.config['ENV']))

## Mongo Conection ##
app.mongo = MongoClient(app.config['MONGO_URI'])
Frame._client = app.mongo

@app.route('/')
def get_index():
    return 'Hello to {} API'.format(app.config['APP_NAME'])


@app.route('/pdv/<int:id>')
def get_pdv(id):
    pdv = Pdv.one(Q.id == str(id), projection={'_id': False})
    if pdv is None:
        return '', 404
    return jsonify(pdv.to_json_type())


@app.route('/search')
def get_near_pdf():
    lat = request.args.get('lat', default=None, type=float)
    lng = request.args.get('lng', default=None, type=float)

    if lat is None or lng is None:
        return '', 404

    pdv = Pdv.one({'coverageArea': {'$near': {'$geometry': {'type': "Point", 'coordinates': [lng, lat]}}}},
                  projection={'_id': False})

    return jsonify(pdv.to_json_type())



