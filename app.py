from flask import Flask, jsonify


def webserver():
    app = Flask(__name__)

    @app.route('/')
    def welcome():
        return 'Hello, World!'

    return app


if __name__ == '__main__':
    app = webserver()
    app.run()
