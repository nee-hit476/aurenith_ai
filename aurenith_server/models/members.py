from uuid import uuid4
from models.extensions import db

class Members(db.Model):
    __tablename__ = "members"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    username = db.Column(db.String(90), unique=True, nullable=False)
    email = db.Column(db.String(130), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(15), unique=True, nullable=False)
    isAttending = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"<Members {self.username}>"