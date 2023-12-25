from __main__ import app

from flask import jsonify, make_response, request
from services.auth import login_service, register_service
from services.student import create_student_service, get_all_students_service, get_student_service, update_student_service, delete_student_service, restore_student_service

# Create a student
def create_student_controller(student_data):
    # Validate required fields
    if not student_data or not student_data['name'] or not student_data['id'] or not student_data['age']:
        return make_response('Missing params', 400, {})

    # Save the student to the database
    result = create_student_service(student_data['id'], student_data['name'], student_data['age'])

    # Return success response
    return make_response(jsonify({'message': 'Student created successfully'}), result['code'], {})

# Get all students
def get_all_students_controller():
    # Retrieve all students from the database
    students = get_all_students_service()

    # Return the list of students
    return make_response(jsonify(students), students['code'], {})

# Get a specific student by ID
def get_student_controller(student_id):
    # Retrieve the student from the database based on the ID
    student = get_student_service(student_id)

    # Return the student
    return make_response(jsonify(student), student['code'], {})

# Update a student
def update_student_controller(student_id, student_data):
    # Validate required fields
    if not student_data or not student_data['name'] or not student_data['age']:
        return make_response('Missing params', 400, {})

    # Update the student in the database
    student = update_student_service(student_id, student_data['name'], student_data['age'])

    # Return success response
    return make_response(jsonify(student), student['code'], {})

# Delete a student
def delete_student_controller(student_id):
    # Delete the student from the database based on the ID
    student = delete_student_service(student_id)

    # Return success response
    return make_response(jsonify(student), student['code'], {})

# Restore a student
def restore_student_controller(student_id):
    # Restore the student in the database based on the ID
    student = restore_student_service(student_id)

    # Return success response
    return make_response(jsonify(student), student['code'], {})

