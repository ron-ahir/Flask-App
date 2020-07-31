from helloapp import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    qstring = db.Column(db.String(200), index=True)
    qauthor = db.Column(db.String(100), index=True)

    def __repr__(self):
        return "<User : {}>".format(self.qstring+' '+self.qauthor)
