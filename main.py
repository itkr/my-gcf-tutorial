import os

import yaml
from flask import Flask, request
from google.cloud import storage

from environment import update_environ


def hello_world(request):
    """Responds to any HTTP request.

    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    update_environ()

    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return str(os.environ)


def main():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return hello_world(request)

    app.run('127.0.0.1', 8000, debug=True)


if __name__ == '__main__':
    main()
