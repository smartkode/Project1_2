from . import db

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, unique=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    age = db.Column(db.Integer)
    sex = db.Column(db.String(80))
    added = db.Column(db.String(80))
    highscore = db.Column(db.String(80), default="")
    tdollars = db.Column(db.String(80), default="")
    image = db.Column(db.String(240))

    def __init__(self, userid, firstname, lastname, age, sex, added, image):
        self.userid = userid
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.sex = sex
        self.added = added
        self.image = image

    def __repr__(self):
        return 'Profile: {} {} {} {} {} {}'.format(self.userid, self.firstname, self.lastname, self.age, self.sex, self.image)