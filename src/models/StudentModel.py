# src/models/student_model.py
class Student:
    def __init__(self, CARNET, NOMBRE, PROGRAMA):
        self.CARNET = CARNET
        self.NOMBRE = NOMBRE
        self.PROGRAMA = PROGRAMA

    def to_json(self):
        return {
            'id': self.CARNET,
            'name': self.NOMBRE,
            'programa': self.PROGRAMA
        }
