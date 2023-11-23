from flask import Flask
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(20)

import routes