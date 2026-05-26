import sys
sys.path.append('..')
from core import gestor
import streamlit as st
import pandas as pd

st.title('Modulo de Login Seguro')

menu = st.sidebar.selectbox('Menu', ['Login', 'Registrar', 'Ver Usuarios'])

if menu == 'Registrar':

    st.subheader('Crear nueva cuenta')
    user = st.text_input('Usuario')
    pwd = st.text_input('Contrasena', type='password')

    if st.button('Registrar'):
        if user and pwd:
            exito, msg = gestor.crear_usuario(user, pwd)
            if exito:
                st.success(msg)
            else:
                st.error(msg)
        else:
            st.warning('Rellene todos los campos')
elif menu == 'Login':

    st.subheader('Iniciar Sesion')
    user = st.text_input('Usuario').lower()
    pwd = st.text_input('Contrasena', type='password')

    if st.button('Entrar'):
        exito, msg = gestor.login_usuario(user, pwd)

        if exito:
            st.balloons()
            st.success(msg)
        else:
            st.error(msg)
elif menu == 'Ver Usuarios':
    
    st.subheader('Usuarios Registrados')
    usuarios = gestor.listar_usuarios_flet()

    data = []

    for username, info in usuarios.items():

        data.append({
            "Usuario": username,
            "Activo": info["activo"]
        })
    
    df = pd.DataFrame(data)

    st.table(df)

    usuario_eliminar = st.selectbox(
    "Selecciona un usuario",
    df["Usuario"])

    if st.button("Eliminar Usuario"):

        exito, msg = gestor.eliminar_usuario(
            usuario_eliminar
        )

        if exito:
            st.success(msg)
            st.rerun()

        else:
            st.error(msg)