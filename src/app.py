__author__ = 'chrisshroba'

from flask import *
from src.login.login_blueprint import login_blueprint
app = Flask(__name__)
app.config["APPLICATION_ROOT"] = "/api"

app.register_blueprint(login_blueprint)

app.run(port=1234, debug= True)