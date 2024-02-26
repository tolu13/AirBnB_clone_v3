#!/usr/bin/python3
"""tthis is an index file """

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def api_status():
    """Return the status of the API"""
    return jsonify({"status": "OK"})
