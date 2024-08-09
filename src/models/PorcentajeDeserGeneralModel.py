# src/models/desercion_model.py
class Desercion:
    def __init__(self, cantidad_estudiantes, porcentaje_desercion):
        self.cantidad_estudiantes = cantidad_estudiantes
        self.porcentaje_desercion = porcentaje_desercion

    def to_json(self):
        return {
            'cantidad_estudiantes': self.cantidad_estudiantes,
            'porcentaje_desercion': self.porcentaje_desercion
        }
    
class DesertoresPorFacultad:
    def __init__(self, FACULTAD, cantidad_estudiantes_desertores):
        self.FACULTAD = FACULTAD
        self.cantidad_estudiantes_desertores = cantidad_estudiantes_desertores

    def to_json(self):
        return {
            'facultad': self.FACULTAD,
            'cantidad_estudiantes_desertores': self.cantidad_estudiantes_desertores
        }

class DesertoresPorSisben:
    def __init__(self, SISBEN, cantidad_estudiantes_desertores):
        self.SISBEN = SISBEN
        self.cantidad_estudiantes_desertores = cantidad_estudiantes_desertores

    def to_json(self):
        return {
            'sisben': self.SISBEN,
            'cantidad_estudiantes_desertores': self.cantidad_estudiantes_desertores
        }

class DesertoresPorPais:
    def __init__(self, PAIS, cantidad_estudiantes_desertores):
        self.PAIS = PAIS
        self.cantidad_estudiantes_desertores = cantidad_estudiantes_desertores

    def to_json(self):
        return {
            'pais': self.PAIS,
            'cantidad_estudiantes_desertores': self.cantidad_estudiantes_desertores
        }
        
class DesertoresPorGenero:
    def __init__(self, GENERO, cantidad_estudiantes):
        self.GENERO = GENERO
        self.cantidad_estudiantes = cantidad_estudiantes

    def to_json(self):
        return {
            'genero': self.GENERO,
            'cantidad_estudiantes': self.cantidad_estudiantes
        }

class DesertoresPorEtnia:
    def __init__(self, GRUPO_ETNICO, cantidad_estudiantes_desertores):
        self.GRUPO_ETNICO = GRUPO_ETNICO
        self.cantidad_estudiantes_desertores = cantidad_estudiantes_desertores

    def to_json(self):
        return {
            'grupo_etnico': self.GRUPO_ETNICO,
            'cantidad_estudiantes_desertores': self.cantidad_estudiantes_desertores
        }
        
class DesertoresPorNivelEduPadre:
    def __init__(self, NIVEL_EDU_PADRE, cantidad_estudiantes_desertores):
        self.NIVEL_EDU_PADRE = NIVEL_EDU_PADRE
        self.cantidad_estudiantes_desertores = cantidad_estudiantes_desertores

    def to_json(self):
        return {
            'nivel_edu_padre': self.NIVEL_EDU_PADRE,
            'cantidad_estudiantes_desertores': self.cantidad_estudiantes_desertores
        }
        
class DesertoresPorNivelEduMadre:
    def __init__(self, NIVEL_EDU_MADRE, cantidad_estudiantes_desertores):
        self.NIVEL_EDU_MADRE = NIVEL_EDU_MADRE
        self.cantidad_estudiantes_desertores = cantidad_estudiantes_desertores

    def to_json(self):
        return {
            'nivel_edu_madre': self.NIVEL_EDU_MADRE,
            'cantidad_estudiantes_desertores': self.cantidad_estudiantes_desertores
        }

class TopDesercionPorFacultad:
    def __init__(self, FACULTAD, cantidad_estudiantes_desertores, total_estudiantes, porcentaje_desercion):
        self.FACULTAD = FACULTAD
        self.cantidad_estudiantes_desertores = cantidad_estudiantes_desertores
        self.total_estudiantes = total_estudiantes
        self.porcentaje_desercion = porcentaje_desercion

    def to_json(self):
        return {
            'facultad': self.FACULTAD,
            'cantidad_estudiantes_desertores': self.cantidad_estudiantes_desertores,
            'total_estudiantes': self.total_estudiantes,
            'porcentaje_desercion': self.porcentaje_desercion
        }

