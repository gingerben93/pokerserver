import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'Users'
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50))
    user_password = db.Column(db.String(50))
