import numpy as np
import tensorflow as tf
import statsmodels.api as sm
from src.services.studentService import StudentService
from src.services.modeloService import ModeloService
from flask import jsonify

class DesercionService:
    @classmethod
    def predecir_desercion(cls, carnet):
        # Obtener los datos del estudiante
        estudiante = StudentService.get_students(carnet)
        if not estudiante:
            return {"error": "Estudiante no encontrado"}
        
        # Mapas de conversión para variables categóricas
        genero_map = {'F': 0, 'M': 1}
        sisben_map = {'Grupo A': 1, 'Grupo B': 2, 'Grupo C': 3, 'Grupo D': 4, 'CATEGORIA 6': 0, '[NO APLICA]': 0, '[NO TIENE SISBEN]': 0}

        # Convertir los datos del estudiante en un formato adecuado para el modelo
        datos_estudiante = estudiante[0]  # Suponemos que solo hay un estudiante con ese carnet

        # Usar el mapeo para convertir las variables categóricas a numéricas
        genero = genero_map.get(datos_estudiante['genero'], -1)  # -1 para valores desconocidos
        sisben = sisben_map.get(datos_estudiante['Sisben'], -1)  # -1 para valores desconocidos
        
        # Crear la lista de entrada con las variables convertidas
        X_input = [
            genero,
            sisben,
            float(datos_estudiante['PromedioGeneral']),
            float(datos_estudiante['mat']),
            float(datos_estudiante['Relg']),
            float(datos_estudiante['prog'])
        ]

        # Convertir en array NumPy
        X_input_np = np.array([X_input])

        # Cargar el modelo entrenado
        modelo = tf.keras.models.load_model(ModeloService.MODEL_PATH)

        # Realizar predicción
        probabilidad_desercion = modelo.predict(X_input_np)[0][0]
        deserta = probabilidad_desercion >= 0.5

        # Obtener las variables más influyentes (en el caso del modelo logístico)
        # modelo_logistico = sm.load(ModeloService.LOGIT_PATH)
        # influencias = modelo_logistico.params  # Parámetros que indican influencia de cada variable
        variables_influyentes = ModeloService.obtener_coeficientes_logisticos()
        if variables_influyentes:
            variables_influyentes = {var: round(float(coef), 2) for var, coef in variables_influyentes.items()}

        # Devolver resultados
        resultado = {
            "carnet": carnet,
            "deserta": bool(deserta),
            "probabilidad_desercion": float(probabilidad_desercion),  # Convertir a float estándar
            "variables_influyentes": variables_influyentes if variables_influyentes is not None else {}
        }

        return resultado
