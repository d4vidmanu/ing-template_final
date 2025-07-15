from datetime import datetime

class Contacto:
    def __init__(self, alias):
        self.alias = alias
        self.fechaRegistro = datetime.now()  # Fecha de registro del contacto

    def __str__(self):
        # Cambiar el formato de la fecha para solo mostrar día/mes/año
        return f"Contacto: {self.alias}, Fecha de Registro: {self.fechaRegistro.strftime('%d/%m/%Y')}"
