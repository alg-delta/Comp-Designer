from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Sti(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(230), nullable=True)
    price = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(230), nullable=True)


class Moni(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(230), nullable = True)
    price = db.Column(db.Integer, nullable = False)
    image =  db.Column(db.String(230), nullable = True)

class Arls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(230), nullable=True)

class Dop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(230), nullable=True)


