import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from config import DevConfig, ProdConfig, TestConfig
from app.buleprints.main import main
from .models import db
from .errorhandlers import bad_request, not_found, method_not_allowed

# basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    # initialize app
    app = Flask(__name__)
    # config app
    if app.env == "development":
        app.config.from_object(DevConfig)
    elif app.env == "production":
        app.config.from_object(ProdConfig)
    else:
        app.config.from_object(TestConfig)
    # other initalization
    # buleprint
    app.register_blueprint(main)
    # error handlers
    app.register_error_handler(400, bad_request)
    app.register_error_handler(404, not_found)
    app.register_error_handler(405, method_not_allowed)
    # database
    db.init_app(app)
    # migrate
    migrate = Migrate(app, db)
    # CORS
    CORS(app)

    # resource-specific
    # cors = CORS(app,resources={r"api/*": {"origins":"*"}})
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type, Authorization"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET, POST, PATCH, DELETE, OPTIONS"
        )
        return response

    return app
