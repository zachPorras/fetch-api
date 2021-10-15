from flask import Blueprint, render_template, request
from fetch_points_api.forms import SpendPointsForm, AddTransactionsForm

site = Blueprint('site', __name__, template_folder='site_templates')


@site.route('/')
def home():
    return render_template('index.html')

@site.route('/balances', methods=['GET'])
def balances():
    return render_template('balances.html')

@site.route('/add_transactions', methods=['POST', 'PUT', 'GET'])
def add_transactions():
    form = AddTransactionsForm()
    if request.method == 'POST' and form.validate_on_submit:
        points = form.points.data
        payer = form.payer.data
        print(points, payer)

    return render_template('add_transactions.html', form = form)

@site.route('/spend_points', methods=['POST', 'PUT', 'GET'])
def spend_points():
    form = SpendPointsForm()
    if request.method == 'POST' and form.validate_on_submit:
        points = form.points.data
        print(points)

    return render_template('spend_points.html', form = form)