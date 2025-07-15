from datetime import datetime

class Mensaje:
    def __init__(self, remitente, destinatario, contenido):
        self.remitente = remitente  # Usuario que envía el mensaje
        self.destinatario = destinatario  # Usuario que recibe el mensaje
        self.contenido = contenido  # Contenido del mensaje
        self.fechaEnvio = datetime.now()  # Fecha y hora del envío

    def __str__(self):
        return f"Mensaje de {self.remitente.alias} a {self.destinatario.alias}: {self.contenido} - Enviado el {self.fechaEnvio.strftime('%d/%m/%Y %H:%M:%S')}"
