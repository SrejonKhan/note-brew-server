import os
from dotenv import load_dotenv

load_dotenv()

# Base Config
class Config:
    FLASK_ENV = "development"
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER = {'title': 'Note Brew API Docs', 'uiversion': 3}

# Development Config
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ['DEV_DATABASE_URI']

# Testing Config
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ['TEST_DATABASE_URI']

# Production Config
class ProductionConfig(Config):
    FLASK_ENV = "production"
    SQLALCHEMY_DATABASE_URI = os.environ['PROD_DATABASE_URI']
