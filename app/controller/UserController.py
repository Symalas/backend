from app.helper import response
from app.model.user import User
from app.model.student import Student
from app import app, db
from flask import request, flash
from app.helper import generateJwt

def singleObject(data):
    data = {
       
        'email': data.email,
        'role': data.role,
    }

    return data


def login():
    try:
        email = request.form.get('email')
        password = request.form.get('password')
    
    # filter(Student.userid == User.id).with_entities(User.email, User.role, User.password, Student.npm ,Student.name)
        user = db.session.query(User).filter(User.email == email).first()

        # flash(user.checkPassword(password))

        if not user:
            return response.badRequest("Email tidak ditemukan atau Password Salah", [])

        if not user.checkPassword(password):
            return response.badRequest("Email tidak ditemukan atau password salah", [])

        data= singleObject(user)


        access_token = generateJwt.getJwt(data)

        return response.success("Login Success",{
            "data" : data,
            "access_token": access_token,
        })


    except Exception as e:
        print(e)