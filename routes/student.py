from __main__ import app

from flask import request
from controllers.student import create_student_controller, delete_student_controller, get_all_students_controller, get_student_controller, restore_student_controller, update_student_controller

from decorators.auth import token_required

# route for query logs in params
@app.route('/student/list', methods=['GET'])
@token_required
def get_all_students_route(current_user):
    return get_all_students_controller()

# route for getting a specific student by ID
@app.route('/student/<string:id>', methods=['GET'])
@token_required
def get_student_by_id_route(current_user, id):
    return get_student_controller(id)

# route for creating a new student
@app.route('/student', methods=['POST'])
@token_required
def create_student_route(current_user):
    data = request.get_json()
    return create_student_controller(data)

# route for updating an existing student
@app.route('/student/<string:id>', methods=['PUT'])
@token_required
def update_student_route(current_user, id):
    data = request.get_json()
    return update_student_controller(id, data)

# route for deleting a student
@app.route('/student/<string:id>', methods=['DELETE'])
@token_required
def delete_student_route(current_user, id):
    return delete_student_controller(id)

# route for restoring a deleted student
@app.route('/student/restore/<string:id>', methods=['PUT'])
@token_required
def restore_student_route(current_user, id):
    return restore_student_controller(id)