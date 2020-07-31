from flask import render_template, request
import random
from .forms import QuoteForm
from .models import Quotes
from helloapp import app, db

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
    allquotes=Quotes.query.all()
    return render_template('quotes.html',allquotes=allquotes)

@app.route('/addquote/', methods=['GET','POST'])
def add_quote():
    form=QuoteForm()
    if request.method == 'POST':
        qt = Quotes(qstring=form.qstring.data, qauthor=form.qauthor.data)
        try:
            db.session.add(qt)
            db.session.commit()
        except Exception:
            db.session.rollback()
        return render_template('addquote_confirmation.html', title='Add Quote Confirmation', quote=form.qstring.data)
    return render_template('addquote.html',form=form)


