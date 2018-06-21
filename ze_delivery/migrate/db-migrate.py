import os
import sys
import json
import pymongo

from pymongo import MongoClient
from mongoframes import Frame

""" This need because have to import Pdv class when run as cli """
base_dir = os.path.abspath(os.path.dirname(__file__)).replace('/migrate', '')
sys.path.append(base_dir)

from model.pdv import Pdv
from settings import config


def get_migrate_data():
    data_file = '{}/migrate/pdvs.json'.format(base_dir)
    with open(data_file, 'r') as df:
        return json.load(df)


if __name__ == '__main__':
    conf = config.development
    if 'FLASK_ENV' in os.environ and os.environ['FLASK_ENV'] == 'production':
        conf = config.production

    try:
        mongo = MongoClient(conf.MONGO_URI)
        Frame._client = mongo
        Pdv.insert_many(get_migrate_data()['pdvs'])
        Pdv.get_collection().create_index([('id', pymongo.ASCENDING)], unique=True)
        Pdv.get_collection().create_index([('coverageArea', pymongo.GEOSPHERE)])
    except Exception as e:
        print(e)
        sys.exit(1)



