import logging
from flask import Blueprint

logger = logging.getLogger(__name__)

home_page_blueprint = Blueprint('home_page_blueprint', __name__)

@home_page_blueprint.route('/')
def index():
    return "This is an example app"