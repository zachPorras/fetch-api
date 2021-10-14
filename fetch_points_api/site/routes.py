from flask import Blueprint, render_template

site = Blueprint('site', __name__, template_folder='site_templates')


@site.route('/')
def home():
    return render_template('index.html')

@site.route('/balances')
def balances():
    return render_template('balances.html')

@site.route('/transactions')
def add_transactions():
    return render_template('transactions.html')

@site.route('/spend_points')
def spend_points():
    return render_template('spend_points.html')