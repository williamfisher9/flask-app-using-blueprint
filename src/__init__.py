import json
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, get_jwt_identity, create_access_token
import logging

from routes.app_routes import get_home_page
from src.config.logging_config import initialize_logging_config



if __name__ == '__main__':
    initialize_logging_config()
    logger = logging.getLogger(__name__)

    logger.info("Creating Flask instance and store it in the variable 'app'")

    app = Flask(__name__)

    logger.info("Reading flask config parameters from the file app_config.json")

    app.config.from_file("config\\app_configs.json", load=json.load)

    app.add_url_rule('/api/v1/users', 'get_home_page', get_home_page)
    app.run(debug=True, port=8080)

