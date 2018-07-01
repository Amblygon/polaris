from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/explore/category')
def categories():
    return "Hello cat"

@app.route('/explore/level')
def levels():
    return "Hello levels"

@app.route('/explore/contest')
def contests():
    return "Hello contest"

@app.route('/codeforces/problemset/problem/<int:pset>/<palph>')
def cf_editorial_page(pset, palph):
    #Editorial, site and others passed on as objects after reading from DB.
    return render_template('cf-editorial.html')
