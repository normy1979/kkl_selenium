"""Data models."""
from application import db

class LoginInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    site_url = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return '<LoginInfo {}>'.format(self.username)