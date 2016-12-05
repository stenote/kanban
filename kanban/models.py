from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Repo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Repo %r>' % self.name
