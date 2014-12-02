from app import db


class User(db.Model):
    id_no = db.Column(db.String(6), primary_key = True)
    password = db.Column(db.String(10))
    role = db.Column(db.Integer)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    phone_no = db.Column(db.String)
    email = db.Column(db.String)
    title = db.Column(db.String)
    rank = db.Column(db.String)
    ocu = db.Column(db.String)
    specialisations = db.Column(db.String)
    cv = db.Column(db.String)
    mentor = db.Column(db.Integer)
    coffee = db.Column(db.Integer)
    phone_chat = db.Column(db.Integer)
    email_chat = db.Column(db.Integer)


    def __repr__(self):
        return '<User %r>' % (self.id)

    def get_id(self):
        return unicode(self.id)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False