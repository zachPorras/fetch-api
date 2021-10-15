from flask import Blueprint, render_template, request, jsonify
from fetch_points_api.forms import SpendPointsForm, AddTransactionsForm, CheckBalances
from fetch_points_api.models import db, Transactions, Partner, partners_schema

site = Blueprint('site', __name__, template_folder='site_templates')


@site.route('/')
def home():
    return render_template('index.html')

@site.route('/balances', methods=['GET'])
def balances():
    balances = Partner.query.all()
    response = jsonify(partners_schema.dump(balances))
    return response

@site.route('/add_transactions', methods=['POST', 'PUT', 'GET'])
def add_transactions():
    form = AddTransactionsForm()
    if request.method == 'POST' and form.validate_on_submit:
        points = form.points.data
        partner_name = form.partner_name.data
        print(points, partner_name)
        new_transaction = Transactions(points, partner_name)
        db.session.add(new_transaction)
        db.session.commit()

    return render_template('add_transactions.html', form = form)

@site.route('/spend_points', methods=['POST', 'PUT', 'GET'])
def spend_points():
    form = SpendPointsForm()
    if request.method == 'POST' and form.validate_on_submit:
        points = form.points.data
        print(points)

    return render_template('spend_points.html', form = form)