# Add any model classes for Flask-SQLAlchemy here
from . import db
from datetime import datetime

class PropertyProfile(db.Model):
    __tablename__ = 'Movies'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(260), nullable=False)
    poster=db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def _init_(self,id,title,description,poster,created_at):
        self.id=id
        self.title=title
        self.description=description
        self.poster = poster
        self.created_at = created_at

def _repr_(self):
    return f"Movie(id={self.id}, title='{self.title}', description='{self.description}', poster={self.poster}, created_at={self.created_at}')"