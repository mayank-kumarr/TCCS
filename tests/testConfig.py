import os
basedir = os.path.abspath(os.path.dirname(__file__))


class TestConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'testApp.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

