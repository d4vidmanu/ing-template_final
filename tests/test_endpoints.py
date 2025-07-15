import pytest
from src.controller import app

@pytest.fixture
def client():
    """Fixture para usar el cliente de prueba de Flask"""
    with app.test_client() as client:
        yield client

def test_crear_usuario(client):
    """Prueba de la ruta POST para crear un usuario"""
    response = client.post('/mensajeria/contactos/cpaz', json={
        "contacto": "lmunoz",
        "nombre": "Luisa"
    })
    assert response.status_code == 201
    assert "Contacto lmunoz aniadido" in response.data.decode()

def test_agregar_contacto(client):
    """Prueba de la ruta POST para agregar un contacto a un usuario"""
    response = client.post('/mensajeria/contactos/cpaz', json={
        "contacto": "mgrau",
        "nombre": "Miguel"
    })
    assert response.status_code == 201
    assert "Contacto mgrau aniadido" in response.data.decode()

def test_enviar_mensaje(client):
    """Prueba de la ruta POST para enviar un mensaje"""
    response = client.post('/mensajeria/enviar', json={
        "usuario": "cpaz",
        "contacto": "lmunoz",
        "mensaje": "Hola, ¿cómo estás?"
    })
    assert response.status_code == 200
    assert "Mensaje enviado" in response.data.decode()

def test_ver_mensajes(client):
    """Prueba de la ruta GET para ver los mensajes recibidos"""
    response = client.get('/mensajeria/recibidos?mialias=lmunoz')
    assert response.status_code == 200
    assert "Christian te escribió" in response.data.decode()

def test_agregar_contacto_usuario_no_existente(client):
    """Prueba de error: Agregar un contacto a un usuario no existente"""
    response = client.post('/mensajeria/contactos/usuario_inexistente', json={
        "contacto": "lmunoz",
        "nombre": "Luisa"
    })
    assert response.status_code == 404
    assert "Usuario no encontrado" in response.data.decode()

def test_enviar_mensaje_contacto_no_existente(client):
    """Prueba de error: Enviar mensaje a un contacto no existente"""
    response = client.post('/mensajeria/enviar', json={
        "usuario": "cpaz",
        "contacto": "contacto_inexistente",
        "mensaje": "Mensaje a un contacto no existente"
    })
    assert response.status_code == 404
    assert "Usuario o contacto no encontrado" in response.data.decode()

def test_ver_mensajes_usuario_no_existente(client):
    """Prueba de error: Ver mensajes de un usuario no existente"""
    response = client.get('/mensajeria/recibidos?mialias=usuario_inexistente')
    assert response.status_code == 404
    assert "Usuario no encontrado" in response.data.decode()
