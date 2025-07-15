from datetime import datetime

class Contacto:
    def __init__(self, alias):
        self.alias = alias
        self.fechaRegistro = datetime.now()  # Fecha de registro del contacto

    def __str__(self):
        return f"Contacto: {self.alias}, Fecha de Registro: {self.fechaRegistro}"
