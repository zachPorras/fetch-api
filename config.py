import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "gimme dem points"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False