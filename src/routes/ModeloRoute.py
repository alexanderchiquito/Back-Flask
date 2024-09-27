from flask import Blueprint, jsonify, request
from src.services.modeloService import ModeloService
import traceback
from src.utils.Security import Security
from src.utils.Logger import Logger

main = Blueprint('entrenarModelo_blueprint', __name__)

@main.route('/', methods=['GET'])
def entrenar_modelo():
    try:
        resultado = ModeloService.entrenar_modelo()
        return jsonify(resultado)
    except Exception as ex:
        Logger.add_to_log("Error al entrenar el modelo", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        return jsonify({'message': 'Ocurrió un error al entrenar el modelo', 'success': False}), 500
