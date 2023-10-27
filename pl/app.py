import admin
import shareholder

import model

from flask import Flask
from flask_bootstrap import Bootstrap4


db = model


app = Flask(__name__)
app.config['TITLE'] = "Shopping Lapa - Titulos"
app.secret_key = b'guerra aos senhores'


admin.configure(app)
shareholder.configure(app)
db.configure(app)

Bootstrap4(app)