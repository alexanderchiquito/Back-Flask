from flask import Blueprint, jsonify, request
from src.services.desercionService import DesercionService
import traceback
from src.utils.Security import Security
from src.utils.Logger import Logger


# Definir un Blueprint para las rutas relacionadas con la deserción
main = Blueprint('desercion_bp', __name__)

# Ruta para predecir la deserción basado en el carnet del estudiante
@main.route('/', methods=['GET'])
def predecir_desercion():
    try:
        # Obtener el parámetro 'carnet' de la query string
        carnet = request.args.get('carnet', '').strip()
        
        # Validar si el carnet fue proporcionado
        if not carnet:
            return jsonify({"message": "El carnet es requerido"}), 400
        # Llamamos al servicio de predicción de deserción
        resultado = DesercionService.predecir_desercion(carnet)
        probabilidad_desercion = round(float(resultado['probabilidad_desercion']) * 100, 2)
        # variables_influyentes = [round(float(x), 2) for x in resultado['variables_influyentes']]
        
        if isinstance(resultado, dict):
            return jsonify({
                "carnet": resultado['carnet'],
                "deserta": bool(resultado['deserta']),
                "probabilidad_desercion": f"{probabilidad_desercion}%",
                "variables_influyentes": resultado['variables_influyentes']
            })
        else:
            return jsonify({'message': 'No students found for the given carnet', 'success': True}), 404

    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        return jsonify({'message': 'Internal Server Error', 'success': False}), 500
