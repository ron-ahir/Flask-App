from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class QuoteForm(FlaskForm):
   qstring = StringField("Quote")
   qauthor = StringField("Quote Author")
   submit = SubmitField("Submit")