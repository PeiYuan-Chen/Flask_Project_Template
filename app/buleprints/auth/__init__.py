from flask.blueprints import Blueprint

auth = Blueprint(name="auth", import_name=__name__)

from . import routes, models
