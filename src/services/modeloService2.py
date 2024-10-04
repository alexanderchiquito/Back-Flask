import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from src.database.db_mysql import get_connection
from src.utils.Logger import Logger
import traceback

class ModeloService2:
    
    # Ruta del archivo del modelo guardado
    MODEL_PATH = 'src/models/modelo_logistico2.pkl'

    @staticmethod
    def obtener_datos():
        try:
            connection = get_connection()
            query = """
            SELECT m.GENERO, m.SISBEN, 
                   n.Promedio AS PROMEDIO_GENERAL, n.MAT, n.RELG, n.PROG, 
                   m.DESERTO
            FROM matriculas m
            JOIN notas n ON m.CARNET = n.CARNET
            """
            data = pd.read_sql(query, connection)
            connection.close()
            return data
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return None

    @staticmethod
    def entrenar_modelo():
        data = ModeloService2.obtener_datos()
        if data is None:
            return "Error al obtener los datos"

        # Preprocesamiento
        data['PROMEDIO_GENERAL'] = pd.to_numeric(data['PROMEDIO_GENERAL'], errors='coerce')
        data['MAT'] = pd.to_numeric(data['MAT'], errors='coerce')
        data['RELG'] = pd.to_numeric(data['RELG'], errors='coerce')
        data['PROG'] = pd.to_numeric(data['PROG'], errors='coerce')
        
        data['GENERO'] = data['GENERO'].replace({'F': 0, 'M': 1}).infer_objects()
        convertir_sisben = {'Grupo A': 1, 'Grupo B': 2, 'Grupo C': 3, 'Grupo D': 4, 'CATEGORIA 6': 0, '[NO APLICA]': 0, '[NO TIENE SISBEN]': 0}
        data['SISBEN'] = data['SISBEN'].map(convertir_sisben).fillna(0)
        data['DESERTO'] = data['DESERTO'].astype(str).str.strip()
        data['DESERTO'] = data['DESERTO'].replace({'SI': 1, 'NO': 0, 'Ausencia': 0, 'Desertor': 1})

        X = data[['GENERO', 'SISBEN', 'PROMEDIO_GENERAL', 'MAT', 'RELG', 'PROG']]
        y = data['DESERTO']
        
        X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(X, y, test_size=0.2, random_state=42)
        
        X_TRAIN = X_TRAIN.astype('float32')
        X_TEST = X_TEST.astype('float32')
        Y_TRAIN = Y_TRAIN.astype('int')
        Y_TEST = Y_TEST.astype('int')
        # Modelo de Regresión Logística
        modelo_logistico = LogisticRegression()
        modelo_logistico.fit(X_TRAIN, Y_TRAIN)

        # Guardar el modelo
        with open(ModeloService2.MODEL_PATH, 'wb') as logistic_model_file:
            pickle.dump(modelo_logistico, logistic_model_file)

        # Evaluación
        predicciones = modelo_logistico.predict(X_TEST)
        accuracy = accuracy_score(Y_TEST, predicciones)
        matriz_confusion = confusion_matrix(Y_TEST, predicciones)
        
        return {
            "accuracy": accuracy,
            "matriz_confusion": matriz_confusion.tolist()
        }

    @staticmethod
    def obtener_coeficientes_logisticos():
        try:
            with open(ModeloService2.MODEL_PATH, 'rb') as logistic_model_file:
                modelo_logistico = pickle.load(logistic_model_file)

            # Obtener los nombres de las variables del modelo
            variables_nombres = ['GENERO', 'SISBEN', 'PROMEDIO_GENERAL', 'MAT', 'RELG', 'PROG']

            # Extraer los coeficientes
            coeficientes = modelo_logistico.coef_[0]

            # Crear un diccionario con nombres de variables y sus coeficientes
            variables_coeficientes = dict(zip(variables_nombres, coeficientes))

            return variables_coeficientes
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return None
