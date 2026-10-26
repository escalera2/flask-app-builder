from flask import Flask, render_template
from flask_appbuilder import AppBuilder
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
appbuilder = AppBuilder()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("config")

    db.init_app(app)

    with app.app_context():
        appbuilder.init_app(app, db.session)

        from . import models, views

        db.create_all()

    @app.errorhandler(404)
    def page_not_found(e):
        return (
            render_template(
                "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
            ),
            404,
        )

    return app
