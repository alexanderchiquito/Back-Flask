# src/routes_students.py
from flask import Blueprint, jsonify, request
import traceback
from src.services.studentService import StudentService
from src.utils.Security import Security
from src.utils.Logger import Logger

main = Blueprint('student_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_students():
    try:
        has_access = Security.verify_token(request.headers)
        if not has_access:
            return jsonify({'message': 'Unauthorized'}), 401
        
        carnet = request.args.get('carnet', '').strip()
        if not carnet:
            return jsonify({'message': 'Missing carnet parameter'}), 400
        
        students = StudentService.get_students(carnet)
        if students:
            return jsonify({'students': students, 'message': 'SUCCESS', 'success': True})
        else:
            return jsonify({'message': 'No students found for the given carnet', 'success': True}), 404

    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        return jsonify({'message': 'Internal Server Error', 'success': False}), 500
