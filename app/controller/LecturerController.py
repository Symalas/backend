from app.helper import response
from app.model.lecturer import Lecturer
from app.model.user import User
from app import app, db
from flask import request

def register():
    try:
        nidn = request.form.get('nidn')
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('password')
        role = request.form.get('role')

        if password != confirm_password:
            return response.badRequest([], "Konfirmasi Password tidak sesuai")

        res = [{
            'nidn': nidn,
            'name': name,
            'email': email
        }]

        
        users = User(email=email, role=role)
        users.setPassword(password)
        db.session.add(users)
        db.session.flush()

        dosen = Lecturer(nidn=nidn, name=name, userid=users.id)
        db.session.add(dosen)
        db.session.flush()

        db.session.commit()
        return response.success(res, "Data Berhasil Ditambahkan!!")
    except Exception as e:
        print(e)

    
