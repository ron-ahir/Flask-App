from flask import render_template
import random
from .forms import QuoteForm
from helloapp import app

quotes = [
                "By the time a man realizes that maybe his father was right, he usually has a son who thinks he's wrong.",
                "Give me six hours to chop down a tree and I will spend the first four sharpening the axe.",
                "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
                "Listen to many, speak to a few.",
                "Sometimes the fastest way to get there is to stop for the night."
        ]

@app.route('/')
@app.route('/home/')
def hello():
    return render_template('hello.html')

@app.route('/hello/<username>/')
def hello_user(username):
    quote=random.choice(quotes)
    return render_template('hello_user.html', user=username, quote=quote)

@app.route('/quotes/')
def display_quotes():
    ls=str(quotes)
    return render_template('quotes.html',quote=quotes)

@app.route('/addquote/')
def add_quote():
    form=QuoteForm()
    return render_template('addquote.html',form=form)


