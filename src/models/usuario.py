from src.models.mensaje import Mensaje

class Usuario:
    def __init__(self, alias, nombre):
        self.alias = alias
        self.nombre = nombre
        self.listaContactos = []
        self.mensajesEnviados = []
        self.mensajesRecibidos = []

    def agregarContacto(self, contacto):
        self.listaContactos.append(contacto)

    def enviarMensaje(self, contacto, contenido):
        mensaje = Mensaje(self, contacto, contenido)
        self.mensajesEnviados.append(mensaje)
        contacto.recibirMensaje(mensaje)

    def recibirMensaje(self, mensaje):
        self.mensajesRecibidos.append(mensaje)
