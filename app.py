from flask import Flask
import secrets
from flask_login import login_user, LoginManager
app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(20)




login_manager = LoginManager()
login_manager.init_app(app)

import routes