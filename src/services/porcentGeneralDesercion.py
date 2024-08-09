# src/services/desercion_service.py
import traceback
import pymysql
from src.database.db_mysql import get_connection
from src.utils.Logger import Logger
# from src.models.PorcentajeDeserGeneralModel import Desercion, DesertoresPorFacultad, DesertoresPorSisben, DesertoresPorPais, DesertoresPorGenero, DesertoresPorEtnia, DesertoresPorNivelEduPadre, DesertoresPorNivelEduMadre, TopDesercionPorFacultad
# from src.sql.sqlQuerys import GET_CANTIDAD_DESERTORES_Y_PORCEN, GET_CANT_DESERTORES_BY_FACULTAD, GET_CANT_DESERTORES_BY_SISBEN, GET_CANT_DESERTORES_BY_PAIS, GET_CANT_DESERTORES_BY_GENERO, GET_CANT_DESERTORES_BY_ETNIA, GET_CANT_DESERTORES_BY_NIVEL_EDU_PADRE, GET_CANT_DESERTORES_BY_NIVEL_EDU_MADRE, GET_PORCENTAJE_DESERTORES_BY_FACULTAD
from src.imports import *

class DesercionGeneralService:

    @classmethod
    def get_porcentaje_desercion(cls):
        try:
            connection = get_connection()
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(GET_CANTIDAD_DESERTORES_Y_PORCEN)
                resultset = cursor.fetchone()  # Se usa fetchone ya que es una sola fila
                if resultset:
                    desercion = Desercion(resultset['cantidad_estudiantes'], resultset['porcentaje_desercion'])
                    return desercion.to_json()
            connection.close()
            return {}
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return {}
    
    @classmethod
    def get_cantidad_desertores_por_facultad(cls):
        try:
            connection = get_connection()
            desertores_por_facultad = []
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(GET_CANT_DESERTORES_BY_FACULTAD)
                resultset = cursor.fetchall()
                for row in resultset:
                    Desertores = DesertoresPorFacultad(row['FACULTAD'], row['cantidad_estudiantes_desertores'])
                    desertores_por_facultad.append(Desertores.to_json())
            connection.close()
            return desertores_por_facultad
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return []
    
    @classmethod
    def get_cantidad_desertores_por_sisben(cls):
        try:
            connection = get_connection()
            desertores_por_sisben= []
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(GET_CANT_DESERTORES_BY_SISBEN)
                resultset = cursor.fetchall()
                for row in resultset:
                    Desertores = DesertoresPorSisben(row['SISBEN'], row['cantidad_estudiantes_desertores'])
                    desertores_por_sisben.append(Desertores.to_json())
            connection.close()
            return desertores_por_sisben
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return []

    @classmethod
    def get_cantidad_desertores_por_pais(cls):
        try:
            connection = get_connection()
            desertores_por_pais= []
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(GET_CANT_DESERTORES_BY_PAIS)
                resultset = cursor.fetchall()
                for row in resultset:
                    Desertores = DesertoresPorPais(row['PAIS'], row['cantidad_estudiantes_desertores'])
                    desertores_por_pais.append(Desertores.to_json())
            connection.close()
            return desertores_por_pais
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return []
        
    @classmethod
    def get_cantidad_desertores_por_genero(cls):
        try:
            connection = get_connection()
            desertores = []
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(GET_CANT_DESERTORES_BY_GENERO)
                resultset = cursor.fetchall()
                for row in resultset:
                    desertor = DesertoresPorGenero(row['GENERO'], row['cantidad_estudiantes'])
                    desertores.append(desertor.to_json())
            connection.close()
            return desertores
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return []
        
    @classmethod
    def get_cantidad_desertores_por_etnia(cls):
        try:
            connection = get_connection()
            desertores = []
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(GET_CANT_DESERTORES_BY_ETNIA)
                resultset = cursor.fetchall()
                for row in resultset:
                    desertor = DesertoresPorEtnia(row['GRUPO_ETNICO'], row['cantidad_estudiantes_desertores'])
                    desertores.append(desertor.to_json())
            connection.close()
            return desertores
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return []
        
    @classmethod
    def get_cantidad_desertores_por_nivelEduPadre(cls):
        try:
            connection = get_connection()
            desertores = []
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(GET_CANT_DESERTORES_BY_NIVEL_EDU_PADRE)
                resultset = cursor.fetchall()
                for row in resultset:
                    desertor = DesertoresPorNivelEduPadre(row['NIVEL_EDU_PADRE'], row['cantidad_estudiantes_desertores'])
                    desertores.append(desertor.to_json())
            connection.close()
            return desertores
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return []
    
    @classmethod
    def get_cantidad_desertores_por_nivelEduMadre(cls):
        try:
            connection = get_connection()
            desertores = []
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(GET_CANT_DESERTORES_BY_NIVEL_EDU_MADRE)
                resultset = cursor.fetchall()
                for row in resultset:
                    desertor = DesertoresPorNivelEduMadre(row['NIVEL_EDU_MADRE'], row['cantidad_estudiantes_desertores'])
                    desertores.append(desertor.to_json())
            connection.close()
            return desertores
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return []
        
    @classmethod
    def get_porcentaje_desertores_por_facultad(cls):
        try:
            connection = get_connection()
            desertores = []
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(GET_PORCENTAJE_DESERTORES_BY_FACULTAD)
                resultset = cursor.fetchall()
                for row in resultset:
                    desertor = TopDesercionPorFacultad(row['FACULTAD'], row['cantidad_estudiantes_desertores'], row['total_estudiantes'], row['porcentaje_desercion'])
                    desertores.append(desertor.to_json())
            connection.close()
            return desertores
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return []
    

