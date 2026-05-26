import sys
sys.path.append('..')
from core import gestor

def menu_principal():
    """
        Muestrar una interfaz de usuario por consola que permita interactuar con el sistema de login. El
        programa muestrar un menú con las opciones de registrar usuario, iniciar sesión, listar usuarios y salir.
    """
    while True:
        print('\n' + '='*30)
        print(' SISTEMA DE LOGIN (PYTHON PURO) ')
        print('='*30)
        print('1. Registrar Usuario')
        print('2. Iniciar Sesion')
        print('3. Lista Usuarios')
        print('4. Eliminar Usuarios')
        print('5. Salir')
        print('-' * 30)

        opcion = input('Seleccione una opcion: ')

        if opcion == '1':

            user = input('Nuevo Usuario: ').lower()
            pwd = input('Nueva Contrasena: ')
            exito, msg = gestor.crear_usuario(user, pwd)
            print(f'\n>> {msg}')
        elif opcion == '2':

            user = input('Usuario: ').lower()
            pwd = input('Contrasena: ')
            exito, msg = gestor.login_usuario(user, pwd)
            print(f'\n>> {msg}')
        elif opcion == '3':

            print('\n--- Lista de Usuarios ---')
            lista = gestor.listar_usuarios()
            for u in lista:
                print(u)
        elif opcion == '4':

            user = input('Nombre del Usuario a eliminar: ').lower()
            exito, msg = gestor.borrar_usuario(user)
            print(f'\n>> {msg}')
        elif opcion == '5':

            print('Hasta luego!')
            break
        else:

            print('Opcion no valida.')