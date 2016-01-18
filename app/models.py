from . import db

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, unique=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    age = db.Column(db.Integer)
    sex = db.Column(db.String(80))

    def __init__(self, userid, firstname, lastname, age, sex):
        self.userid = userid
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.sex = sex

    def __repr__(self):
        return 'Profile: {} {} {} {} {}'.format(self.userid, self.firstname, self.lastname, self.age, self.sex)