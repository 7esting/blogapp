from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Hector'}
    posts = [
        {
            'author': {'username': 'Fanti'},
            'body': 'If you educate a man you educate an individual, but if you educate a woman you educate a family (nation)'
        },
        {
            'author': {'username': 'Chilavert'},
            'body': 'Humilde pero no sumiso.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
'''
@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)
'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember me={}'.format(
            form.username.data, form.remember_me.data))
        #return redirect('/index')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

