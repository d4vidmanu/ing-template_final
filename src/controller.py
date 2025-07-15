from flask import Flask, jsonify, request
from src.data_handler import DataHandler

app = Flask(__name__)  # Definimos la instancia de la aplicación aquí

data_handler = DataHandler()

# Ruta GET: Obtener los contactos de un usuario
@app.route('/mensajeria/contactos', methods=['GET'])
def get_contactos():
    """Obtener los contactos de un usuario"""
    mialias = request.args.get('mialias')
    usuario = data_handler.get_usuario(mialias)

    if usuario:
        # Crear la respuesta en el formato esperado por el profesor
        contactos = [f"{contacto.alias}: {data_handler.get_usuario(contacto.alias).nombre}" for contacto in
                     usuario.listaContactos]
        return "\n".join(contactos)  # Imprimir cada contacto en una nueva línea
    return jsonify({"error": "Usuario no encontrado"}), 404


# Ruta POST: Aniadir un contacto a un usuario
@app.route('/mensajeria/contactos/<alias>', methods=['POST'])
def add_contacto(alias):
    data = request.get_json()
    contacto = data['contacto']
    usuario = data_handler.get_usuario(alias)
    if usuario:
        new_contact = data_handler.agregar_contacto(alias, contacto)
        return jsonify({"message": f"Contacto {contacto} aniadido"}), 201
    return jsonify({"error": "Usuario no encontrado"}), 404

# Ruta POST: Enviar un mensaje de un usuario a otro
@app.route('/mensajeria/enviar', methods=['POST'])
def enviar_mensaje():
    data = request.get_json()
    usuario = data_handler.get_usuario(data['usuario'])
    destinatario = data_handler.get_usuario(data['contacto'])
    if usuario and destinatario:
        usuario.enviarMensaje(destinatario, data['mensaje'])
        return jsonify({"message": "Mensaje enviado"}), 200
    return jsonify({"error": "Usuario o contacto no encontrado"}), 404

# Ruta GET: Obtener los mensajes recibidos por un usuario
@app.route('/mensajeria/recibidos', methods=['GET'])
def get_mensajes_recibidos():
    mialias = request.args.get('mialias')  # Obtener el alias del usuario desde los parametros
    usuario = data_handler.get_usuario(mialias)  # Buscar al usuario por alias

    if usuario:
        # Crear la respuesta en el formato esperado por el profesor
        mensajes = [
            f"{data_handler.get_usuario(msg.remitente.alias).nombre} te escribió “{msg.contenido}” el {msg.fechaEnvio.strftime('%d/%m/%Y')}."
            for msg in usuario.mensajesRecibidos  # Recorrer los mensajes recibidos
        ]
        return "\n".join(mensajes)  # Imprimir cada mensaje en una nueva línea
    return jsonify({"error": "Usuario no encontrado"}), 404
