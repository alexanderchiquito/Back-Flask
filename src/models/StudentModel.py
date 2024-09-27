# src/models/student_model.py
class Student:
    def __init__(self, CARNET, NOMBRE, PROGRAMA, GENERO, SISBEN, PROMEDIO_GENERAL, MAT, RELG, PROG):
        self.CARNET = CARNET
        self.NOMBRE = NOMBRE
        self.PROGRAMA = PROGRAMA
        self.GENERO = GENERO
        self.SISBEN = SISBEN
        self.PROMEDIO_GENERAL = PROMEDIO_GENERAL
        self.MAT = MAT
        self.RELG = RELG
        self.PROG = PROG
        
    def to_json(self):
        return {
            'id': self.CARNET,
            'name': self.NOMBRE,
            'programa': self.PROGRAMA,
            'genero': self.GENERO,
            'Sisben': self.SISBEN,
            'PromedioGeneral': self.PROMEDIO_GENERAL,
            'mat': self.MAT,
            'Relg': self.RELG,
            'prog': self.PROG
                    
        }
