from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    # __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    mail = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False)

    favorites = db.relationship("Favorite", lazy=True)

    def __repr__(self):
        return "<User %r>" % self.user_name

    def serialize(self):
        return {"user": self.user_name, "mail": self.mail}

    def full_serialize(self):
        return {
            "user": self.user_name,
            "mail": self.mail,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "active": self.is_active,
        }


class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    elements = db.relationship("Element", lazy=True)

    def __repr__(self):
        return "<Category %r>" % self.name

    def serialize(self):
        return {"user": self.user_name, "mail": self.mail}


class Element(db.Model):
    __tablename__ = "elements"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(Category.id))
    details = db.Column(db.String)

    favorites = db.relationship("Favorite", lazy=True)

    def __repr__(self):
        return "<Element %r>" % self.name

    def serialize(self):
        return {
            "name": self.name,
            "category": self.category_id,
            "details": self.details,
        }


class Favorite(db.Model):
    __tablename__ = "favorites"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    element_id = db.Column(db.Integer, db.ForeignKey(Element.id))

    def __repr__(self):
        return "<Favorite %r>" % self.element_id

    def serialize(self):
        return {"favorite": self.element_id}
