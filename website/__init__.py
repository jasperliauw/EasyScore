from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Jasper2oo8$'

    from .views import views
    from .auth import authentication

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(authentication, url_prefix='/')

    return app