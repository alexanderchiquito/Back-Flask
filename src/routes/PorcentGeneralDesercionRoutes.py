# src/routes_desercion.py
from flask import Blueprint, jsonify, request

import traceback
from src.services.porcentGeneralDesercion import DesercionGeneralService
from src.utils.Security import Security
from src.utils.Logger import Logger

main = Blueprint('desercion_blueprint', __name__)

@main.route('/general', methods=['GET'])
def get_porcentaje_desercion():
    try:
        # Verificar token de acceso
        has_access = Security.verify_token(request.headers)
        if not has_access:
            return jsonify({'message': 'Unauthorized'}), 401
        
        # Obtener datos de deserción
        desercion_data = DesercionGeneralService.get_porcentaje_desercion()
        if desercion_data:
            return jsonify({'desercion': desercion_data, 'message': 'SUCCESS', 'success': True})
        else:
            return jsonify({'message': 'No data found', 'success': True}), 404
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        return jsonify({'message': 'Internal Server Error', 'success': False}), 500


@main.route('/facultades', methods=['GET'])
def get_cantidad_desertores_por_facultad():
    try:
        has_access = Security.verify_token(request.headers)
        if not has_access:
            return jsonify({'message': 'Unauthorized'}), 401
        
        desertores_por_facultad = DesercionGeneralService.get_cantidad_desertores_por_facultad()
        if desertores_por_facultad:
            return jsonify({'desertores_por_facultad': desertores_por_facultad, 'message': 'SUCCESS', 'success': True})
        else:
            return jsonify({'message': 'No data found', 'success': True}), 404
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        return jsonify({'message': 'Internal Server Error', 'success': False}), 500
    
@main.route('/sisben', methods=['GET'])
def get_cantidad_desertores_por_sisben():
    try:
        has_access = Security.verify_token(request.headers)
        if not has_access:
            return jsonify({'message': 'Unauthorized'}), 401
        
        desertores_por_sisben = DesercionGeneralService.get_cantidad_desertores_por_sisben()
        if desertores_por_sisben:
            return jsonify({'desertores_por_sisben': desertores_por_sisben, 'message': 'SUCCESS', 'success': True})
        else:
            return jsonify({'message': 'No data found', 'success': True}), 404
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        return jsonify({'message': 'Internal Server Error', 'success': False}), 500
    
@main.route('/pais', methods=['GET'])
def get_cantidad_desertores_por_pais():
    try:
        has_access = Security.verify_token(request.headers)
        if not has_access:
            return jsonify({'message': 'Unauthorized'}), 401
        
        desertores_por_pais = DesercionGeneralService.get_cantidad_desertores_por_pais()
        if desertores_por_pais:
            return jsonify({'desertores_por_pais': desertores_por_pais, 'message': 'SUCCESS', 'success': True})
        else:
            return jsonify({'message': 'No data found', 'success': True}), 404
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        return jsonify({'message': 'Internal Server Error', 'success': False}), 500

@main.route('/genero', methods=['GET'])
def get_cantidad_desertores_por_genero():
    try:
        
        has_access = Security.verify_token(request.headers)
        if not has_access:
            return jsonify({'message': 'Unauthorized'}), 401
        
        desertores = DesercionGeneralService.get_cantidad_desertores_por_genero()
        if desertores:
            return jsonify({'desertores_por_genero': desertores, 'message': 'SUCCESS', 'success': True})
        else:
            return jsonify({'message': 'No data found', 'success': True}), 404
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        return jsonify({'message': 'Internal Server Error', 'success': False}), 500

@main.route('/etnia', methods=['GET'])
def get_cantidad_desertores_por_etnia():
    try:
        has_access = Security.verify_token(request.headers)
        if not has_access:
            return jsonify({'message': 'Unauthorized'}), 401
        
        desertores = DesercionGeneralService.get_cantidad_desertores_por_etnia()
        if desertores:
            return jsonify({'desertores_por_etnia': desertores, 'message': 'SUCCESS', 'success': True})
        else:
            return jsonify({'message': 'No data found', 'success': True}), 404
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        return jsonify({'message': 'Internal Server Error', 'success': False}), 500

@main.route('/padre', methods=['GET'])
def get_cantidad_desertores_por_nivelEduPadre():
    try:
        has_access = Security.verify_token(request.headers)
        if not has_access:
            return jsonify({'message': 'Unauthorized'}), 401
        
        desertores = DesercionGeneralService.get_cantidad_desertores_por_nivelEduPadre()
        if desertores:
            return jsonify({'desertores_por_nivel_educativo_padre': desertores, 'message': 'SUCCESS', 'success': True})
        else:
            return jsonify({'message': 'No data found', 'success': True}), 404
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        return jsonify({'message': 'Internal Server Error', 'success': False}), 500

@main.route('/madre', methods=['GET'])
def get_cantidad_desertores_por_nivelEduMadre():
    try:
        
        has_access = Security.verify_token(request.headers)
        if not has_access:
            return jsonify({'message': 'Unauthorized'}), 401
        
        desertores = DesercionGeneralService.get_cantidad_desertores_por_nivelEduMadre()
        if desertores:
            return jsonify({'desertores_por_nivel_educativo_madre': desertores, 'message': 'SUCCESS', 'success': True})
        else:
            return jsonify({'message': 'No data found', 'success': True}), 404
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        return jsonify({'message': 'Internal Server Error', 'success': False}), 500
    
@main.route('/topFacultad', methods=['GET'])
def get_porcentaje_desertores_por_facultad():
    try:
        has_access = Security.verify_token(request.headers)
        if not has_access:
            return jsonify({'message': 'Unauthorized'}), 401
        
        desertores = DesercionGeneralService.get_porcentaje_desertores_por_facultad()
        if desertores:
            return jsonify({'porcentaje_desertores_por_facutad': desertores, 'message': 'SUCCESS', 'success': True})
        else:
            return jsonify({'message': 'No data found', 'success': True}), 404
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        return jsonify({'message': 'Internal Server Error', 'success': False}), 500