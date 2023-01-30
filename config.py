class Config(object):
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./frameworks.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_ALLOWED_ORIGINS = ['http://127.0.0.1:5000']
