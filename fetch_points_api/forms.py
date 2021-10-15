from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired

class AddTransactionsForm(FlaskForm):
    partner_name = StringField('Partner Name', validators=[DataRequired()])
    points = IntegerField('Points', validators=[DataRequired()])
    # timestamp is added when sent to DB, to be used later
    submit_button = SubmitField()

class SpendPointsForm(FlaskForm):
    points = IntegerField('Points', validators=[DataRequired()])
    submit_button = SubmitField()

class CheckBalances(FlaskForm):
    submit_button = SubmitField()