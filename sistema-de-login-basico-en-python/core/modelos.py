def crear_plantilla_usuario(password_encriptada):
    """
        Define la estructura de datos para un nuevo usuario.
        Retorna un diccionario (estructura de datos).
    """
    return {
        'password': password_encriptada,
        'activo': True
    }