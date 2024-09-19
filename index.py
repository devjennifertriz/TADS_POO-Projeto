from templates.LoginUI import LoginUI
from templates.AbrirContaUI import AbrirContaUI
from templates.ManterUsuarioUI import ManterUsuarioUI
from templates.ManterCategoriaUI import ManterCategoriaUI
from templates.ManterProdutoUI import ManterProdutoUI
from templates.FazerEncomendaUI import FazerEncomendaUI
from view import View
import streamlit as st

st.header("Doceria SweetYou")

class IndexUI:

    def Entrar():
        select = st.sidebar.selectbox("Entrar", ["Fazer Login", "Criar uma conta"])
        if select == "Fazer Login": LoginUI.Main()
        if select == "Criar uma conta": AbrirContaUI.Main()

    def MenuAdmin():
        select = st.sidebar.selectbox("Menu", ["Manter Usuário", "Manter Categoria", "Manter Produto"])
        if select == "Manter Usuário": ManterUsuarioUI.Main()
        if select == "Manter Categoria": ManterCategoriaUI.Main()
        if select == "Manter Produto": ManterProdutoUI.Main()

    def MenuUsuario():
        select = st.sidebar.selectbox("Minhas Encomendas", ["Fazer Encomenda", "Visualizar Encomenda"])
        if select == "Fazer Encomenda": FazerEncomendaUI.Main()
        #if select == "Visualizar Encomenda": ManterEncomendaUI.Main()

    def Sidebar():
        if 'user_nome' not in st.session_state:
            IndexUI.Entrar()   
        else:
            st.sidebar.write("Bem-vindo(a), " + st.session_state['user_nome'])
        if st.session_state['user_nome'] == 'admin': IndexUI.MenuAdmin()
        else: IndexUI.MenuUsuario() 
        IndexUI.Logout()

    def Logout():
        if st.sidebar.button("Logout"):
            del st.session_state["user_id"]
            del st.session_state["user_nome"]
            st.rerun

    def Main():
        IndexUI.Sidebar()

IndexUI.Main()