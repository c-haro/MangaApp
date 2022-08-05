import imp
from secrets import token_urlsafe
from flask import Flask, render_template, request, session, url_for, flash, redirect
from App.app import * 

app = Flask(__name__)
app.config['SECRET_KEY'] = token_urlsafe(16)

@app.route('/' , methods=('GET', 'POST'))
@app.route('/index', methods=('GET', 'POST'))
def index():
    response = []
    name = 'Chris'
    session['title'] = []
    if request.method == 'POST':
        mTitle = request.form['title']

        if not mTitle:
            flash('Missing title to search')
        else:
            response = titleSearch(mTitle)
            for titleName in response['data']:
                print(titleName['attributes']['title'])
            session['title'] = response
            return redirect(url_for('index'))
    return render_template('index.html', title='Welcome', username=name,result=session['title'])


