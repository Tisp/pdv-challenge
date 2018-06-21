import os
import sys
import yaml
import json
import pymongo

from pymongo import MongoClient
from mongoframes import Frame

""" This need because have to import Pdv class when run as cli """
base_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(base_dir)

from model.pdv import Pdv

def get_config():

    conf_file = '{}/config/config.yml'.format(base_dir)

    with open(conf_file, 'r') as cf:
        try:
            config = yaml.load(cf)
        except yaml.YAMLError as e:
            print(e)
            sys.exit(1)

    env = 'DEVELOPMENT' if 'ENV' not in os.environ else os.environ['ENV'].upper()

    return config[env]


def get_migrate_data():
    data_file = '{}/migrate/pdvs.json'.format(base_dir)
    with open(data_file, 'r') as df:
        return json.load(df)


if __name__ == '__main__':
    config = get_config()

    try:
        mongo = MongoClient(config['MONGO_URI'])
        print(config['MONGO_URI'])
    except Exception as e:
        print(e)
        sys.exit(1)

    Frame._client = mongo
    Pdv.insert_many(get_migrate_data()['pdvs'])
    Pdv.get_collection().create_index([('id', pymongo.ASCENDING)], unique=True)
    Pdv.get_collection().create_index([('coverageArea', pymongo.GEOSPHERE)])

