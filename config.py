from abc import ABCMeta
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class AppBaseConfig(metaclass=ABCMeta):
    SECRET_KEY = 'a secret key'
    PROPAGATE_EXCEPTIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(AppBaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ''

class TestingConfig(AppBaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = ''

class ProdConfig(AppBaseConfig):
    SQLALCHEMY_DATABASE_URI = ''

class SQLiteConfig(AppBaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'sample.sqlite')

def create_config(config_name):
    config = {
        'sqlite': SQLiteConfig,
        'development': DevConfig,
        'testing': TestingConfig,
        'production': ProdConfig,
        'default': SQLiteConfig
    }

    return config[config_name]
