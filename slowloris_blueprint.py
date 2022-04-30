from flask import Blueprint

slowloris_blueprint = Blueprint('slowloris_blueprint', __name__)


@slowloris_blueprint.route('/')
def index():
    return "Hello, world!"
