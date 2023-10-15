from flask.blueprints import Blueprint

api = Blueprint(name="api", import_name=__name__)

from . import routes, models
