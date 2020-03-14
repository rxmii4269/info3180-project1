from . import db



class User(db.Model):

    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer,primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    gender = db.Column(db.String(6))
    email = db.Column(db.String(255),unique=True)
    location = db.Column(db.String(80))
    biography = db.Column(db.Text())
    profile_pic_id = db.Column(db.String(255))
    created_on = db.Column(db.Date())


    def __init__(self,firstname,lastname,gender,email,location,biography,profile_pic_id,created_on):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.email = email
        self.location = location
        self.biography = biography
        self.profile_pic_id = profile_pic_id
        self.created_on = created_on




    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id) # python 3 support

    def __repr__(self):
        return '<User %r >' % self.id

