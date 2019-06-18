import os
from os.path import join, dirname
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))

# Create .flaskenv file path
dotenv_path = join(dirname(__file__), '.flaskenv')
# Load file from path
load_dotenv(dotenv_path)
class Config(object):
    FLASK_APP = os.environ.get('FLASK_APP') or 'microblog.py'
    #DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['hector@localhost']

# Environment obj not usable yet
class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True