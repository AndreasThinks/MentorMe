from app import db

class User(db.Model):
    id = db.Column(db.String(6), primary_key = True)
    password = db.Column(db.String(10))
    role = db.Column(db.Integer)

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