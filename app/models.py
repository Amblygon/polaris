from datetime import datetime
from app import db

class Editorial(db.Model):
    id = db.Column(db.String(10), primary_key = True)
    pcode = db.Column(db.String(10), unique=True)
    title = db.Column(db.String(60), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    statement = db.Column(db.String(1000))
    hints = db.Column(db.String(1000))
    solution = db.Column(db.String(1000))

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('editorials', lazy=True))

    def __repr__(self):
        return '<Editorial {}>'.format(self.title)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name
