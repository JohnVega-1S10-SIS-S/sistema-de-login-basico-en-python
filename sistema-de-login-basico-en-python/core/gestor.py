import json
import hashlib
import os
import re
from core import modelos

RUTA_DB = os.path.join('data', 'datos.json')

def encriptar_password(password_texto):
    """
        Encripta una contraseña utilizando SHA-256.
        
        Parametros:
            password_texto (str): Contraseña en texto plano.

        Retorna:
            str: Hash encriptado de la contraseña.
    """
    return hashlib.sha256(
        password_texto.encode('utf-8')
    ).hexdigest()

def _cargar_datos():
    if not os.path.exists(RUTA_DB):
        os.makedirs(os.path.dirname(RUTA_DB), exist_ok=True)

        with open(RUTA_DB, 'w') as f:
            json.dump({}, f)
        return {}
    
    with open(RUTA_DB, 'r') as f:
        return json.load(f)
        
def _guardar_datos(datos):
    with open(RUTA_DB, 'w') as f:
        json.dump(datos, f, indent=4)

def crear_usuario(username, password):
    """
        Registrar usuarios nuevos.

        Retorna:
            False "El usuario ya existe." si el usuario ya existe.
            True "Usuario registrado exitosamente." si se registro corectmente.
    """
    datos = _cargar_datos()

    username = username.lower()

    if username.strip() == "":
        return False, 'Campo vacio. Escriba un nombre de usuario.'
    
    pattern = r"^[a-zA-Z0-9_]{3,20}$"
    if not re.match(pattern, username):
        return False, 'Caracteres invalidos.'
 
    if username in datos:
        return False, 'El usuario ya existe.'
    
    if password.strip() == "":
        return False, 'Campo vacio. Escriba una contraseña'
    
    pass_hash = encriptar_password(password)
    nuevo_usuario = modelos.crear_plantilla_usuario(pass_hash)
    datos[username] = nuevo_usuario

    _guardar_datos(datos)

    return True, f'Usuario {username} registrado exitosamente.'
    
def login_usuario(username, password):
    """
        Registra un nuevo usuario en el sistema.
        
        Parametros:
            username (str): Nombre del usuario.
            password (str): Contraseña del usuario.
            
        Retorna:
            tuple: Estado de la operación y mensaje descriptivo.
    """
    datos = _cargar_datos()

    if username not in datos:
        return False, 'Usuario no encontrado.'
    
    hash_almacenado = datos[username]['password']
    hash_ingresado = encriptar_password(password)
    
    if hash_almacenado == hash_ingresado:
        return True, 'Inicio de sesion exitoso.'
    return False, 'Datos incorectos'

def listar_usuarios():
    """
        Mostrar usuarios registrados en el sistema.
    """
    datos = _cargar_datos()

    return [f'- {u} (Activo: {datos[u]["activo"]})'
    for u in datos]

def listar_usuarios_flet():
    datos = _cargar_datos()
    return datos

def borrar_usuario(username):
    """
        Elimina un usuario del sistema.

        Retorna:
            true: Usuario {username} eliminado.
            false: Usuario no encontrado.
    """
    datos = _cargar_datos()

    if username in datos:
        del datos[username]
        _guardar_datos(datos)
        return True, f'Usuario {username} eliminado.'
    return False, 'Usuario no encontrado.'

def eliminar_usuario(username):

    datos = _cargar_datos()

    if username not in datos:
        return False, "El usuario no existe."

    del datos[username]

    _guardar_datos(datos)

    return True, "Usuario eliminado."