import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Config:
    # Base config
    FLASK_APP = "app"
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    # secret_key
    SECRET_KEY = os.getenv("SECRET_KEY")
    # database URI
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")


class DevConfig(Config):
    # Development config
    DEBUG = True


class ProdConfig(Config):
    # production config
    DEBUG = False


class TestConfig(Config):
    # Development config
    DEBUG = True
