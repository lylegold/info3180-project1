from . import db
from werkzeug.security import generate_password_hash

class PropertyProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'property_profiles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    bedrooms = db.Column(db.String(8))
    bathrooms = db.Column(db.String(6))
    price = db.Column(db.String(50))
    location = db.Column(db.String(40))
    type_ = db.Column(db.String(12), unique=True)
    description = db.Column(db.String(255))
    photo = db.Column(db.String(80))


    def __init__(self, title, bedrooms, bathrooms, price, location, type_, description, photo):
        self.title = title
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.price = price
        self.location = location
        self.type_ = type_
        self.description = description
        self.photo = photo
        
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
