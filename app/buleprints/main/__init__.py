from flask.blueprints import Blueprint

main = Blueprint(name="main", import_name=__name__)

from . import routes, models
