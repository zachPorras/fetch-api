from flask import Blueprint, render_template, request, jsonify, redirect
from flask.helpers import url_for
from fetch_points_api.forms import SpendPointsForm, AddTransactionsForm, CheckBalances
from fetch_points_api.models import db, Transactions, transactions_schema
from sqlalchemy.sql import func

site = Blueprint('site', __name__, template_folder='site_templates')


@site.route('/')
def home():
    return render_template('index.html')

@site.route('/balances', methods=['GET'])
def balances():
    balances = db.session.query(Transactions.partner_name, func.sum(Transactions.points).label("total points"))
    balances = balances.group_by(Transactions.partner_name).all()
    print(balances)
    balances_dict = dict(balances)
    return balances_dict

@site.route('/add_transactions', methods=['POST', 'PUT', 'GET'])
def add_transactions():
    form = AddTransactionsForm()
    if request.method == 'POST' and form.validate_on_submit:
        points = form.points.data
        partner_name = form.partner_name.data
        new_transaction = Transactions(partner_name, points)
        db.session.add(new_transaction)
        db.session.commit()
        return redirect(url_for('site.add_transactions', form = form))

    return render_template('add_transactions.html', form = form)

@site.route('/spend_points', methods=['POST', 'PUT', 'GET'])
def spend_points():
    form = SpendPointsForm()
    if request.method == 'POST' and form.validate_on_submit:
        points = form.points.data
        print(points)

    return render_template('spend_points.html', form = form)