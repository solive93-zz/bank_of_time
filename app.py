from flask import Flask
from backend.api_routes import api
from client.site_routes import site


def webserver():
    app = Flask(__name__)
    app.register_blueprint(api)
    app.register_blueprint(site)

    return app


if __name__ == '__main__':
    app = webserver()
    app.run()
