from app import db
from app.model.student import Student
from app.model.studentClass import StudentClass
from app.model.classMember import ClassMember
from app.helper import response
from app.helper.fieldValidation import Validation
from flask import request
from app.helper.generateCode import randomCode
from app.model.user import User


def formatArray(datas):
    array = []

    for i in datas:
        array.append(singleObject(i))

    return array

def singleObject(data):
    data = {
        'id' : data.id,
        'name' : data.name,
        'code' : data.code,
    }
    return data

def index(email):
    try:
        studentClass = db.session.query(StudentClass).filter(User.email == email).filter(ClassMember.npm == Student.npm).filter(ClassMember.class_id == StudentClass.id).with_entities(StudentClass.id, StudentClass.name, StudentClass.code)
        data = formatArray(studentClass)
        if not data:
            return response.notFound("Data Kosong!")

        return response.success("OK", data)
    except Exception as e:
        print(e)
        # return response.serverError("Server Bermasalah")


def insert():
    try:
        v = Validation()
        name = request.form.get('name')
        v.validate(name, "Nama Kelas tidak bole kosong")
        npm = request.form.get('npm')
        v.validate(npm, "NPM tidak bole kosong")

        code = randomCode()
        print(code)
        status = "accepted"
        role = "super_admin"


        studentClass = StudentClass(name=name, code=code)
        db.session.add(studentClass)
        db.session.flush()

        class_id = studentClass.id
        res = [{
            'id': class_id,
            'class_name': name,
            'class_code': code
        }]

        member = ClassMember(npm=npm, class_id=class_id, status=status, role=role)
        db.session.add(member)
        db.session.flush()
        db.session.commit()
        return response.success("Data Berhasil Di tambah", res)
    except Exception:
        return response.badRequest(v.error(), [])

        


