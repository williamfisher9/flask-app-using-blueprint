import json
from flask import Flask, request, jsonify
from config.logging_config import  logging

from controller.app_controller import get_home

logger = logging.getLogger(__name__)

logger.info("Creating Flask instance and store it in the variable 'app'")

app = Flask(__name__)

logger.info("Reading flask config parameters from the file app_config.json")

app.config.from_file("config\\app_configs.json", load=json.load)

app.add_url_rule('/api/v1/users', 'get_users', get_home)

if __name__ == '__main__':
    app.run(debug=True, port=8080)