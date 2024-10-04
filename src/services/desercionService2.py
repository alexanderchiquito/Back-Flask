import numpy as np
import pickle
from src.services.studentService import StudentService
from src.services.modeloService2 import ModeloService2
from flask import jsonify

class DesercionService2:
    @classmethod
    def predecir_desercion(cls, carnet):
        estudiante = StudentService.get_students(carnet)
        if not estudiante:
            return {"error": "Estudiante no encontrado"}
        
        genero_map = {'F': 0, 'M': 1}
        sisben_map = {'Grupo A': 1, 'Grupo B': 2, 'Grupo C': 3, 'Grupo D': 4, 'CATEGORIA 6': 0, '[NO APLICA]': 0, '[NO TIENE SISBEN]': 0}

        datos_estudiante = estudiante[0]  
        genero = genero_map.get(datos_estudiante['genero'], -1)
        sisben = sisben_map.get(datos_estudiante['Sisben'], -1)
        
        X_input = [
            genero,
            sisben,
            float(datos_estudiante['PromedioGeneral']),
            float(datos_estudiante['mat']),
            float(datos_estudiante['Relg']),
            float(datos_estudiante['prog'])
        ]

        X_input_np = np.array([X_input])

        # Cargar el modelo entrenado
        with open(ModeloService2.MODEL_PATH, 'rb') as logistic_model_file:
            modelo_logistico = pickle.load(logistic_model_file)

        # Realizar predicción
        probabilidad_desercion = modelo_logistico.predict_proba(X_input_np)[0][1]
        deserta = probabilidad_desercion >= 0.5

        variables_influyentes = ModeloService2.obtener_coeficientes_logisticos()

        return {
            "carnet": carnet,
            "deserta": bool(deserta),
            "probabilidad_desercion": float(probabilidad_desercion),  
            "variables_influyentes": variables_influyentes
        }
