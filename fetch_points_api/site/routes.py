from flask import Blueprint, render_template, request, jsonify, redirect
from flask.helpers import url_for
from fetch_points_api.forms import SpendPointsForm, AddTransactionsForm, CheckBalances
from fetch_points_api.models import db, Transactions, transactions_schema
from sqlalchemy.sql import func
from sqlalchemy import asc, update

site = Blueprint('site', __name__, template_folder='site_templates')


@site.route('/')
def home():
    return render_template('index.html')

@site.route('/balances', methods=['GET'])
def balances():
    balances = db.session.query(Transactions.partner_name, func.sum(Transactions.points))
    balances = balances.group_by(Transactions.partner_name).all()
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

@site.route('/spend_points', methods=['POST', 'PUT', 'GET', 'DELETE'])
def spend_points():
    form = SpendPointsForm()
    if form.validate_on_submit:
        points = form.points.data
        print(f'points:{points}')

        # sort transactions by date, ascending
        spent_points = db.session.query(Transactions.partner_name, Transactions.points)
        spent_points = spent_points.order_by(asc(Transactions.timestamp)).all()
        first_partner = spent_points[0][1]
        print(f'first partner points before: {first_partner}')

        # if first_partner >= points:
        # if point total <= oldest transaction, subtract from oldest transaction & delete if at zero
        #     updated_points = Transactions.query.order_by(Transactions.timestamp)
        #     print(updated_points)
        #     db.session.commit()
        #     print(spent_points)
        # conditionals for whether point total will bring partner total to zero
        # if point total is higher than oldest transaction, move on to deduct the rest from the next transaction
        # if partner point total reaches zero, move on to next transaction
        # return receipt of point transactions in each response

    return render_template('spend_points.html', form = form)