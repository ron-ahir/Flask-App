from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class QuoteForm(FlaskForm):
   fname = StringField("First Name")
   lname = StringField("Last Name")
   email = StringField("Email")
   submit = SubmitField("Submit")