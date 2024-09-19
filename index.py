from templates.ManterUsuarioUI import ManterUsuarioUI
from templates.ManterCategoriaUI import ManterCategoriaUI
from templates.ManterProdutoUI import ManterProdutoUI
from view import View
import streamlit as st

st.header("Doceria SweetYou")

class IndexUI:
    def MenuAdmin():
        select = st.sidebar.selectbox("Menu", ["Manter Usuário", "Manter Categoria", "Manter Produto"])
        if select == "Manter Usuário": ManterUsuarioUI.Main()
        if select == "Manter Categoria": ManterCategoriaUI.Main()
        if select == "Manter Produto": ManterProdutoUI.Main()

    def Sidebar():
        IndexUI.MenuAdmin()

    def Main():
        IndexUI.Sidebar()

IndexUI.Main()