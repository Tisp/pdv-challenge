class Config(object):
    APP_NAME = 'PDV-CHALLENGE'
    PORT = '5000'

    # Database
    MONGO_SERVER = '127.0.0.1'
    MONGO_DATABASE = 'pdv_challenge'
    MONGO_URI = 'mongodb://{}:27017/{}'.format(MONGO_SERVER, MONGO_DATABASE)
    MONGO_USERNAME = 'ze'
    MONGO_PASSWORD = 'delivery'

    JSONIFY_PRETTYPRINT_REGULAR = False


class production(Config):
    DEBUG = False
    JSONIFY_PRETTYPRINT_REGULAR = False


class development(Config):
    Debug = True
