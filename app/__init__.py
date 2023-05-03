from flask import Flask
from flask_babel import Babel

#Create the flask app
app = Flask(__name__)

# a function which at the moment returns a 2 letter string code for a locale
def get_locale():
    return 'en'
#Hook Babel into your app and pass the local returned by get_locale to it
babel = Babel(app, locale_selector=get_locale)

#If we are using session then we need to set a secret key
app.secret_key='a secret key'


#Import your routes (you need to configure these in routes.py)
from app import routes
