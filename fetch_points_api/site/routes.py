from flask import Blueprint, render_template, request, jsonify, redirect
from flask.helpers import url_for
from fetch_points_api.forms import SpendPointsForm, AddTransactionsForm, CheckBalances
from fetch_points_api.models import db, Transactions, Partner, partners_schema
from sqlalchemy.sql import func

site = Blueprint('site', __name__, template_folder='site_templates')


@site.route('/')
def home():
    return render_template('index.html')

@site.route('/balances', methods=['GET'])
def balances():
    balances = db.session.query(Transactions)
    response = jsonify(partners_schema.dump(balances))
    return response

@site.route('/add_transactions', methods=['POST', 'PUT', 'GET'])
def add_transactions():
    form = AddTransactionsForm()
    if request.method == 'POST' and form.validate_on_submit:
        points = form.points.data
        partner_name = form.partner_name.data
        partner_exists = Partner.query.filter(Partner.partner_name == partner_name).first()
        print(f'this partner exists: {partner_exists}')
        if partner_exists:
            new_transaction = Transactions(points, partner_name)
            db.session.add(new_transaction)
            db.session.commit()
            return redirect(url_for('site.add_transactions', form = form))
        else:
            new_partner = Partner(partner_name, points)
            db.session.add(new_partner)
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