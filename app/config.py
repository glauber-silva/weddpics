import os


class Config:
    DEBUG = True
    PRODUCTION = False
    SECRECT_KEY = 'my_precious'
    BASE_URL = 'http://localhost:5000'
    # MONGODB_HOST = os.environ.get('MONGODB_HOST')
    MONGODB_SETTINGS = {
        'db': os.environ.get('MONGODB_DATABASE'),
        'host': os.environ.get('MONGODB_HOST'),
        'port': 27017,
        'username': os.environ.get('MONGODB_USERNAME'),
        'password': os.environ.get('MONGODB_PASSWORD')
    }
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    Testing = True


class ProductionConfig(Config):
    DEBUG = False
    PRODUCTION = True
