import sys
sys.path.append('..')
from core import gestor
import flet as ft
import flet_datatable2 as fdt

def main(page: ft.Page):
    """
        Muestrar una interfaz de escritorio usando Flet que permita registrar usuarios e iniciar sesión
        con una UI moderna
    """
    page.title = 'Login App'

    def registrar_click(e):
        """
            Registrar usuarios nuevos.

            Retorna:
                False "El usuario ya existe." si el usuario ya existe.
                True "Usuario registrado exitosamente." si se registro corectmente.
        """
        exito, msg = gestor.crear_usuario(
            user_input.value, pass_input.value)
        page.show_dialog(ft.SnackBar(ft.Text(msg)))
        actualizar_tabla()
        page.update()

    def login_click(e):
        """
            Registra un nuevo usuario en el sistema.
            
            Parametros:
                username (str): Nombre del usuario.
                password (str): Contraseña del usuario.
                
            Retorna:
                tuple: Estado de la operación y mensaje descriptivo.
        """
        exito, msg = gestor.login_usuario(
            user_input.value, pass_input.value)
        page.show_dialog(ft.SnackBar(ft.Text(msg)))
        page.update()
    
    def actualizar_tabla():

        usuarios = gestor.listar_usuarios_flet()

        rows = []

        for username, info in usuarios.items():

            rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(cell_text(username)),
                        ft.DataCell(cell_text(str(info["activo"]))),

                        ft.DataCell(
                            ft.IconButton(
                                icon=ft.Icons.DELETE,
                                icon_color="red",

                                on_click=lambda e, u=username: eliminar_usuario(u)
                            )
                        ),
                    ]
                )
            )
        tabla.rows = rows

    def eliminar_usuario(username):

        exito, msg = gestor.eliminar_usuario(username)

        page.show_dialog(
            ft.SnackBar(ft.Text(msg))
        )

        actualizar_tabla()
        page.update()
    
    def cell_text(value: str) -> ft.Text:
        """
            A helper to truncate any overflowing cell text with an ellipsis.
        """
        return ft.Text(value, overflow=ft.TextOverflow.ELLIPSIS, max_lines=1)
    
    usuarios = gestor.listar_usuarios_flet()

    rows = []

    for username, info in usuarios.items():

        rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(cell_text(username)),
                    ft.DataCell(cell_text(str(info["activo"]))),
                ]
            )
        )
        
    user_input = ft.TextField(label='Usuario')
    pass_input = ft.TextField(label='Contrasena', password=True, can_reveal_password=True)
    
    tabla = fdt.DataTable2(
        expand=True,
        min_width=600,

        columns=[
            fdt.DataColumn2(label=ft.Text("Usuario")),
            fdt.DataColumn2(label=ft.Text("Activo")),
            fdt.DataColumn2(label=ft.Text("Acciones")),
        ],

        rows=[],
    )

    actualizar_tabla()

    page.add(ft.Column([
        ft.Text('Sistema de Usuarios', size=30),
        user_input, pass_input,
        ft.Row([
            ft.Button('Registrar', on_click=registrar_click),
            ft.Button('Login', on_click=login_click)]),
        ], alignment=ft.MainAxisAlignment.CENTER))
    page.add(
        ft.SafeArea(
            expand=True,
            content=tabla
        )
    )
ft.run(main)