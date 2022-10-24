from app import db
from datetime import datetime
from app.model.user import User

class Lecturer(db.Model):
    nidn = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    userid = db.Column(db.Integer, db.ForeignKey(User.id, ondelete='CASCADE', onupdate='CASCADE'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Lecturer {}>'.format(self.name)

    