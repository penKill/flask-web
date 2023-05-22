from flask import Blueprint
from werkzeug.exceptions import HTTPException

base = Blueprint('base', __name__, url_prefix='/base')
# base = Blueprint('base', __name__)
from ..routes import user_api
from ..routes import menu_api
from ..routes import job_api
from ..routes import test_api
