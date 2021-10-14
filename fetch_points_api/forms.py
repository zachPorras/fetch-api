from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired

class TransactionForm(FlaskForm):
    payer = StringField('Payer', validators=[DataRequired()])
    points = IntegerField('Points', validators=[DataRequired()])
    # timestamp is added when sent to DB, to be used later
    submit_button = SubmitField()

class SpendPointsForm(FlaskForm):
    points = IntegerField('Points', validators=[DataRequired()])
    submit_button = SubmitField()