from flask import Blueprint, jsonify, request
from src.services.desercionService2 import DesercionService2
import traceback
from src.utils.Logger import Logger

main = Blueprint('desercion2_bp', __name__)

@main.route('/', methods=['GET'])
def predecir_desercion():
    try:
        carnet = request.args.get('carnet', '').strip()
        if not carnet:
            return jsonify({"message": "El carnet es requerido"}), 400
        
        resultado = DesercionService2.predecir_desercion(carnet)
        probabilidad_desercion = round(float(resultado['probabilidad_desercion']) * 100, 2)
        
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
