import admin
#import model
#import norm
#import options

from flask import Flask
from flask_bootstrap import Bootstrap4


#nr = norm
#asdmin = admin
#db = model
#op = options

app = Flask(__name__)
app.config['TITLE'] = "Shopping Lapa - Titulos"
app.secret_key = b'guerra aos senhores'


admin.configure(app)
#nr.configure(app)
#db.configure(app)
#op.configure(app)
Bootstrap4(app)