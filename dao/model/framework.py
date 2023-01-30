from marshmallow import Schema, fields

from setup_db import db


class Framework(db.Model):
    __tablename__ = 'framework'
    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    language = db.Column(db.String)


class FrameworkSchema(Schema):
    pk = fields.Int()
    name = fields.Str()
    language = fields.Str()
