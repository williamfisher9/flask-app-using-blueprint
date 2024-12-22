import logging
from flask import Blueprint

logger = logging.getLogger(__name__)

home_page_blueprint = Blueprint('home_page_blueprint', __name__)

users_blueprint = Blueprint("users_blueprint", __name__)

@home_page_blueprint.before_request
def handle_before_home_request():
    logger.info("#"*30 + " received home page request")

@home_page_blueprint.route('/')
def index():
    return "home page"

@home_page_blueprint.after_request
def bp_after_request(response):
    logger.info("*"*30 + " returned home page response")
    return response

@users_blueprint.route("/users")
def handle_users_page_request():
    return "users page"

