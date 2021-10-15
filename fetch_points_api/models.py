from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid
from flask_marshmallow import Marshmallow


db = SQLAlchemy()

ma = Marshmallow()

class Partner(db.Model):
    partner_id = db.Column(db.String, primary_key=True, unique=True)
    partner_name = db.Column(db.String, nullable=False, unique=True)
    points = db.Column(db.Integer, nullable=False)

    def __init__(self, partner_name, points):
        self.partner_id = self.set_id()
        self.partner_name = partner_name
        self.points = points
    
    def set_id(self):
        return str(uuid.uuid4())

class Transactions(db.Model):
    transaction_id = db.Column(db.String, primary_key=True, unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    points = db.Column(db.Integer, nullable=False)
    partner_name = db.Column(db.String, db.ForeignKey('partner.partner_name'), nullable=False)

    def __init__(self, points, partner_name):
        self.transaction_id = self.set_id()
        self.points = points
        self.partner_name = partner_name

    def set_id(self):
        return str(uuid.uuid4())



class PartnerSchema(ma.Schema):
    class Meta:
        fields = ['partner_name', 'points']

partners_schema = PartnerSchema(many = True)