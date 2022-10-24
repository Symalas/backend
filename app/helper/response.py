from flask import jsonify, make_response

def success(message, data):
    res = {
        'code': 200,
        'message': message,
        'data': data
    }

    return make_response(jsonify(res)), 200


def badRequest(message, data):
    res = {
        'code': 400,
        'message': message,
        'data': data
    }

    return make_response(jsonify(res)), 400


def notFound(message):
    res = {
        'code': 404,
        'message': message
    }

    return make_response(jsonify(res)), 404

def serverError(message):
    res = {
        'code': 501,
        'message': message
    }

    return make_response(jsonify(res)), 501