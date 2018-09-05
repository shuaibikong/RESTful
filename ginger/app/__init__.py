from .app import Flask

def register_blueprint(app):
    from app.api.v1 import create_blurprint_v1
    app.register_blueprint(create_blurprint_v1(),url_prefix='/v1')

def register_plugin(app):
    from app.models.base import db
    db.init_app(app)
    db.create_all(app=app)

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    register_blueprint(app)
    register_plugin(app)


    return app