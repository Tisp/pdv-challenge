class Config(object):
    APP_NAME = 'ze_delivery'
    PORT = '5000'

    # Database
    MONGO_DATABASE = 'ze_delivery'
    MONGO_URI = 'mongodb://localhost:27017/{}'.format(MONGO_DATABASE)
    MONGO_USERNAME = 'ze'
    MONGO_PASSWORD = 'delivery'

    JSONIFY_PRETTYPRINT_REGULAR = False


class production(Config):
    DEBUG = False
    JSONIFY_PRETTYPRINT_REGULAR = False


class development(Config):
    Debug = True