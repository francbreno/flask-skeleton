from abc import ABCMeta
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class AppBaseConfig(metaclass=ABCMeta):
    PROPAGATE_EXCEPTIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')

class DevConfig(AppBaseConfig):
    DEBUG = True

class TestingConfig(AppBaseConfig):
    TESTING = True

class ProdConfig(AppBaseConfig):
    TESTING = False
    DEBUG = False

def create_config(config_name):
    config = {
        'development': DevConfig,
        'testing': TestingConfig,
        'production': ProdConfig,
        'default': DevConfig
    }

    return config[config_name]
