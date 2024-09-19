from templates.ManterUsuarioUI import ManterUsuarioUI
from view import View
import streamlit as st

st.header("Doceria SweetYou")

class IndexUI:
    def MenuAdmin():
        select = st.sidebar.selectbox("Menu", ["Manter Usuário"])
        if select == "Manter Usuário": ManterUsuarioUI.Main()

    def Sidebar():
        IndexUI.MenuAdmin()


    def Main():
        IndexUI.Sidebar()

IndexUI.Main()