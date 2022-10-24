from app import app
from flask import request
from app.controller import LecturerController, StudentController, UserController, StudentClassController
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

@app.route('/')
def index():
    return "Holla Cules"

@app.route('/login', methods=['POST'])
def loginMhs():
    return UserController.login()

# Mahasiswa
@app.route('/register-mhs', methods=['POST'])
def registerMhs():
    return StudentController.register()

@app.route('/class-mhs/<email>', methods=['GET'])
@jwt_required()
def getclassEmail(email):
    return StudentClassController.index(email)

@app.route('/class-mhs', methods=['POST'])
@jwt_required()
def getclass():
    return StudentClassController.insert()


@app.route('/register-dsn', methods=['POST'])
def registerDsn():
    return LecturerController.register()
