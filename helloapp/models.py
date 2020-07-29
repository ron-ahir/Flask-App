from helloapp import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(100), index=True)
    lname = db.Column(db.String(100), index=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return "<User : {}>".format(self.fname+' '+self.lname)
