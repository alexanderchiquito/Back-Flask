from flask import Blueprint, jsonify
from src.services.modeloService2 import ModeloService2
import traceback
from src.utils.Logger import Logger

main = Blueprint('entrenarModelo2_blueprint', __name__)

@main.route('/', methods=['GET'])
def entrenar_modelo():
    try:
        resultado = ModeloService2.entrenar_modelo()
        return jsonify(resultado)
    except Exception as ex:
        Logger.add_to_log("Error al entrenar el modelo", str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        return jsonify({'message': 'Ocurrió un error al entrenar el modelo', 'success': False}), 500
