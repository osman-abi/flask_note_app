from flask import Flask
from .views import views

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'a05b431f418220f7996f1af66bfe218db441d003'

    app.register_blueprint(views, url_prefix='/')

    return app