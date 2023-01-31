from flask import Flask
from flask_restx import Api

from setup_db import db
from config import Config
from dao.model.framework import Framework
from views.frameworks import framework_ns


def create_app(config_object):
    """
    Функция создания Flask приложения
    """
    application = Flask(__name__)
    application.config.from_object(config_object)
    registration_extensions(application)
    return application


def registration_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(framework_ns)
    create_data(application, db)


def create_data(application, db):
    """
    Функция создания базы данных
    """
    with application.app_context():
        db.drop_all()
        db.create_all()

        f1 = Framework(pk=1, name="React", language='Javascript')
        f2 = Framework(pk=2, name="Vue", language='Javascript')
        f3 = Framework(pk=3, name="FastApi", language='Python')
        f4 = Framework(pk=4, name="Laravel", language='PHP')
        f5 = Framework(pk=5, name="Spring", language='Java')

        db.session.begin()
        db.session.add_all([f1, f2, f3, f4, f5])
        db.session.commit()


if __name__ == '__main__':
    app = create_app(Config())
    app.run(port=8000)

