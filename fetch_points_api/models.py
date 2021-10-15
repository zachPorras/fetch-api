from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid
from flask_marshmallow import Marshmallow


db = SQLAlchemy()

ma = Marshmallow()


class Transactions(db.Model):
    transaction_id = db.Column(db.String, primary_key=True)
    partner_name = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    points = db.Column(db.Integer, nullable=False)

    def __init__(self, partner_name, points):
        self.partner_name = partner_name
        self.transaction_id = self.set_id()
        self.points = points
    
    def set_id(self):
        return str(uuid.uuid4())


class TransactionsSchema(ma.Schema):
    class Meta:
        fields = ['partner_name', 'points']

transactions_schema = TransactionsSchema(many = True)