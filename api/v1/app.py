#!/usr/bin/python3
"""firts endpoint route to return api status"""
from flask import flask
from os import environ
from models import storage
from app.v1.views import app_views

app = flask (__name__)

app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_appcontext(exception):
    """ close storage """
    storage.close()

if __name__ == "__main__":
    host = environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(environ.get('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
