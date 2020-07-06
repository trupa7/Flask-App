""""
==========================================
 Title:  A basic “Hello World” API using Flask
 Author: Trupal Patel
 Date:   6th July 2020
==========================================
"""
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest
import logging

app = Flask(__name__)
log = logging.getLogger('werkzeug')
# to enable logging please make log.disabled = False
log.disabled = True


# accepts both a GET and a POST request to the root "/" HTTP endpoint
@app.route("/", methods=['GET', 'POST'])
def index():
    """A basic “Hello World” API"""

    # inspect the headers sent by the client
    headers = request.headers

    # check all header including default header
    for header in headers:
        header_key = header[0]
        header_value = header[1]

        # If the incoming request sets an Accept header with value application/json
        if header_key == "Accept" and header_value == "application/json":
            return jsonify(message="Hello, World")
        # If the incoming request sets an Accept header with header different then application/json.
        elif header_key == "Accept" and header_value != "*/*":
            raise BadRequest('Invalid Header Found!')


    # If the request does not send an Accept header
    return "<p>Hello, World<p>"


if __name__ == '__main__':
    app.run(debug=True)
