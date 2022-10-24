from app import db
from datetime import datetime
from app.model.student import Student
from app.model.studentClass import StudentClass

class ClassMember(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    npm = db.Column(db.String(20), db.ForeignKey(Student.npm, ondelete='CASCADE', onupdate='CASCADE'))
    class_id = db.Column(db.Integer, db.ForeignKey(StudentClass.id, ondelete='CASCADE', onupdate='CASCADE'))
    status = db.Column(db.Enum('pending', 'accepted'), default="pending", nullable=False)
    role = db.Column(db.Enum('member', 'admin', 'super_admin'), default="member", nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<ClassMember {}>".format(self.npm)
