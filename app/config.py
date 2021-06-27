import os


class Config:
    DEBUG = True
    PRODUCTION = False
    BASE_URL = 'http://localhost:5000'
    # MONGODB_HOST = os.environ.get('MONGODB_HOST')
    MONGODB_SETTINGS = {
        'db': os.environ.get('MONGODB_DATABASE'),
        'host': os.environ.get('MONGODB_HOST'),
        'port': 27017,
        'username': os.environ.get('MONGODB_USERNAME'),
        'password': os.environ.get('MONGODB_PASSWORD')
    }

    SECRECT_KEY = os.urandom(32)
    S3_BUCKET = os.environ.get("S3_BUCKET_NAME")
    S3_KEY = os.environ.get("S3_ACCESS_KEY")
    S3_SECRET = os.environ.get("S3_SECRET_ACCESS_KEY")
    S3_LOCATION = f"https://{S3_BUCKET}.s3.amazonaws.com/"

    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    Testing = True


class ProductionConfig(Config):
    DEBUG = False
    PRODUCTION = True
