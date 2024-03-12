from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    grades = db.relationship(
        "Grade", backref=db.backref("student_reference"), lazy=True
    )

    def __repr__(self):
        return f"Student({self.name}, {self.last_name})"


class Grade(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    mark = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.String, nullable=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id_"), nullable=False)

    def __repr__(self):
        return f"Grade({self.mark}, {self.subject}, {self.student_id})"
