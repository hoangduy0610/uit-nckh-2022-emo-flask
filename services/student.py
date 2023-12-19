from datetime import datetime, timedelta
from flask import json, jsonify
from  werkzeug.security import generate_password_hash, check_password_hash
import jwt

from common.constants import SECRET_KEY
from repositories.student import createNewStudent, deleteStudent, getAllStudentsIncludingDeleted, getStudentById, getStudentByIdIncludingDeleted, restoreStudent, updateStudent

def get_all_students_service():
    students = getAllStudentsIncludingDeleted()
    return {
        'status': True,
        'message': 'Successfully',
        'code': 200,
        'data': [student.serialize() for student in students]
    }

def create_student_service(student_id, name, age):
    student = getStudentById(student_id)

    if student:
        # returns 400 if student exist
        return {
            'status': False,
            'message': 'Student already exist',
            'code': 400
        }
  
    student = createNewStudent(student_id, name, age)
    return {
        'status': True,
        'message': 'Successfully created',
        'code': 200,
        'data': student.serialize()
    }

def get_student_service(student_id):
    student = getStudentById(student_id)

    if not student:
        # returns 404 if student does not exist
        return {
            'status': False,
            'message': 'Student does not exist',
            'code': 404
        }
  
    return {
        'status': True,
        'message': 'Successfully retrieved',
        'code': 200,
        'data': student.serialize(has_log=True)
    }

def update_student_service(student_id, name, age):
    student = getStudentById(student_id)

    if not student:
        # returns 404 if student does not exist
        return {
            'status': False,
            'message': 'Student does not exist',
            'code': 404
        }

    check = updateStudent(student_id, name, age)
    if not check:
        # returns 500 if student failed to update
        return {
            'status': False,
            'message': 'Failed to update',
            'code': 400
        }
    return {
        'status': True,
        'message': 'Successfully updated',
        'code': 200,
        'data': student.serialize()
    }

def delete_student_service(student_id):
    student = getStudentById(student_id)

    if not student:
        # returns 404 if student does not exist
        return {
            'status': False,
            'message': 'Student does not exist',
            'code': 404
        }

    check = deleteStudent(student_id)
    if not check:
        # returns 500 if student failed to update
        return {
            'status': False,
            'message': 'Failed to update',
            'code': 400
        }
    return {
        'status': True,
        'message': 'Successfully updated',
        'code': 200,
        'data': student.serialize()
    }

def restore_student_service(student_id):
    student = getStudentByIdIncludingDeleted(student_id)

    if not student:
        # returns 404 if student does not exist
        return {
            'status': False,
            'message': 'Student does not exist',
            'code': 404
        }

    check = restoreStudent(student_id)
    if not check:
        # returns 500 if student failed to update
        return {
            'status': False,
            'message': 'Failed to update',
            'code': 400
        }
    return {
        'status': True,
        'message': 'Successfully updated',
        'code': 200,
        'data': student.serialize()
    }