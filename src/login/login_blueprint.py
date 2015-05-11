__author__ = 'chrisshroba'

from flask.blueprints import Blueprint
from flask import request

from login_exception import *

login_blueprint = Blueprint("login", __name__, url_prefix="/login")

@login_blueprint.route("/login", methods=["POST"])
def signup_route():

    try:
        form_data = request.form
        username = form_data.get("user")
        password = form_data.get("pass")
        login(username, password)

    except LoginException as e:
        pass