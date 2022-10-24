from app.helper import response
from app.helper.fieldValidation import Validation
from app.model.student import Student
from app.model.user import User
from app import app, db
from flask import request


def register():
    try:
        v = Validation()
        npm = request.form.get('npm', None)
        v.validate(npm, "NPM tidak boleh kosong")
        student = Student.query.filter_by(npm=npm).first()
        if student:
            return response.badRequest("NPM sudah terdaftar", [])
        name = request.form.get('name')
        v.validate(name, "Name tidak boleh kosong")
        email = request.form.get('email')
        v.validate(email, "Email tidak boleh kosong")
        email_check = User.query.filter_by(email=email).first()
        if email_check:
            return response.badRequest("Email sudah terdaftar", [])
        role = request.form.get("role")
        v.validate(role, "Role tidak boleh kosong")
        password = request.form.get('password')
        v.validate(password, "Password tidak boleh kosong")
        confirm_password = request.form.get('password_confirm')
        v.validate(confirm_password, "Confirm Password tidak boleh kosong")

        if password != confirm_password:
            return response.badRequest("Konfirmasi Password tidak sesuai", [])

        res = [{
            'npm': npm,
            'name': name,
            'email': email,
            'role': role
        }]

        
        users = User(email=email, role=role)
        users.setPassword(password)
        db.session.add(users)
        db.session.flush()

        mahasiswa = Student(npm=npm, name=name, userid=users.id)
        db.session.add(mahasiswa)
        db.session.flush()

        db.session.commit()
        return response.success("Data Berhasil Ditambahkan!!",res)
    except Exception as e:
        return response.badRequest(v.error(), [])


