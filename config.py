import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    HOST = str(os.environ.get("DB_HOST"))
    USERNAME = str(os.environ.get("DB_USERNAME"))
    PASSWORD = str(os.environ.get("DB_PASSWORD"))
    DATABASE = str(os.environ.get("DB_DATABASE"))

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DATABASE
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_RECORD_QUERIES = True

    JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET"))