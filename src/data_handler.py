from src.models.usuario import Usuario
from src.models.contacto import Contacto

class DataHandler:
    def __init__(self):
        self.usuarios = []

        # Inicializar algunos usuarios con contactos
        usuario_cpaz = Usuario("cpaz", "Christian")
        usuario_lmunoz = Usuario("lmunoz", "Luisa")
        usuario_mgrau = Usuario("mgrau", "Miguel")

        # Agregar contactos
        contacto_lmunoz = Contacto("lmunoz")
        contacto_mgrau = Contacto("mgrau")
        contacto_cpaz = Contacto("cpaz")
        usuario_cpaz.agregarContacto(contacto_lmunoz)
        usuario_cpaz.agregarContacto(contacto_mgrau)
        usuario_lmunoz.agregarContacto(contacto_mgrau)
        usuario_mgrau.agregarContacto(contacto_cpaz)

        # Guardar usuarios
        self.usuarios.append(usuario_cpaz)
        self.usuarios.append(usuario_lmunoz)
        self.usuarios.append(usuario_mgrau)

    def get_usuario(self, alias):
        """Retorna un usuario dado su alias"""
        for usuario in self.usuarios:
            if usuario.alias == alias:
                return usuario
        return None  # Retorna None si no encuentra al usuario

    def agregar_usuario(self, alias, nombre):
        usuario = Usuario(alias, nombre)
        self.usuarios.append(usuario)
        return usuario

    def agregar_contacto(self, alias_usuario, alias_contacto):
        usuario = self.get_usuario(alias_usuario)
        if usuario:
            contacto = Contacto(alias_contacto)
            usuario.agregarContacto(contacto)
            return contacto
        return None
