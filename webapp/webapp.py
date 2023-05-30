import os

from flask import request
from flask import make_response


if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "Hello World!"
    
    @app.route('/health')
    def health():
        resp = make_response ('', 200)
        resp.status_code = 200
        return resp

    @app.route('/message')
    def message():
        MESSAGE = os.environ.get('MESSAGE')
        return MESSAGE

    app.run(host='0.0.0.0', port='5000')
