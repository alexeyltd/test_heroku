from flask import Flask, jsonify, render_template, request
from hashlib import md5
from database.Database import Database

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='static')

# db = Database('db.db')


# admin
@app.route('/admin/login')
def admin_login():
    return render_template('index.html')


# user
# user DATABASE: id, first_name, last_name, email, password, role, business_name, confirm_status: code/0 0=confirmed
@app.route('/account/login')
def account_login():
    return render_template('index.html')


@app.route('/account/registration')
def account_registration():
    return render_template('index.html')


@app.route('/account/confirm')
def account_confirm_registration():
    return render_template('index.html')


@app.route('/account/update')
def account_update():
    return render_template('index.html')


# frontend index page
@app.route('/')
def index():
    return render_template('index.html')


# all to vue router
@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
