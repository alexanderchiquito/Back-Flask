# src/imports.py
import traceback
import pymysql
from src.database.db_mysql import get_connection
from src.utils.Logger import Logger
from src.models.PorcentajeDeserGeneralModel import (
    Desercion, 
    DesertoresPorFacultad, 
    DesertoresPorSisben, 
    DesertoresPorPais, 
    DesertoresPorGenero, 
    DesertoresPorEtnia, 
    DesertoresPorNivelEduPadre, 
    DesertoresPorNivelEduMadre, 
    TopDesercionPorFacultad
)
from src.sql.sqlQuerys import (
    GET_CANTIDAD_DESERTORES_Y_PORCEN, 
    GET_CANT_DESERTORES_BY_FACULTAD, 
    GET_CANT_DESERTORES_BY_SISBEN, 
    GET_CANT_DESERTORES_BY_PAIS, 
    GET_CANT_DESERTORES_BY_GENERO, 
    GET_CANT_DESERTORES_BY_ETNIA, 
    GET_CANT_DESERTORES_BY_NIVEL_EDU_PADRE, 
    GET_CANT_DESERTORES_BY_NIVEL_EDU_MADRE, 
    GET_PORCENTAJE_DESERTORES_BY_FACULTAD,
    GET_AUTH_LOGIN
)
