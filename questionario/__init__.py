from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "12345"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///questionario.db"

    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        from .models import Telefone, Respostas

        db.create_all()

    from .routes import register_routes

    register_routes(app, db)

    return app
