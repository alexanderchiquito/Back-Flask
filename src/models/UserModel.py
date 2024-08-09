class User():

    def __init__(self, USUARIO_ACCESO, CLAVE_ACCESO) -> None:
        self.USUARIO_ACCESO = USUARIO_ACCESO
        self.CLAVE_ACCESO = CLAVE_ACCESO
        
    def to_json(self):
        return {
            'USUARIO_ACCESO': self.USUARIO_ACCESO,
            'CLAVE_ACCESO': self.CLAVE_ACCESO
        }