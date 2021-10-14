from flask import Blueprint, render_template
from fetch_points_api.forms import SpendPointsForm, TransactionForm

site = Blueprint('site', __name__, template_folder='site_templates')


@site.route('/')
def home():
    return render_template('index.html')

@site.route('/balances', methods=['GET'])
def balances():
    return render_template('balances.html')

@site.route('/transactions', methods=['POST'])
def add_transactions():
    form = TransactionForm()
    return render_template('transactions.html', form = form)

@site.route('/spend_points', methods=['POST', 'PUT', 'GET'])
def spend_points():
    form = SpendPointsForm()
    return render_template('spend_points.html', form = form)