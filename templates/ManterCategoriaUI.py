import streamlit as st
import pandas as pd
from view import View
import time

class ManterCategoriaUI:
    def Main():
        st.header("Gerenciar Categorias")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar Categoria", "Inserir Categoria", "Atualizar Categoria", "Excluir Categoria"])
        with tab1: 
            ManterCategoriaUI.ListarCategoria()
        with tab2:
            ManterCategoriaUI.InserirCategoria()
        with tab3:
            ManterCategoriaUI.AtualizarCategoria()
        with tab4:
            ManterCategoriaUI.ExcluirCategoria()

    def ListarCategoria():
        user = View.Usuario_Listar()
        if len(user) == 0:
            st.write("Nenhum usuário encontrado.")
        else:
            dict = []
            for obj in user: dict.append(obj.__dict__)
            df = pd.DataFrame(dict)
            st.dataframe(df)
    
    def InserirCategoria():
        nome = st.text_input("Insira o seu nome: ")
        email = st.text_input("Insira o seu endereço de e-mail")
        fone = st.text_input("Insira o seu número de telefone: ")
        senha = st.text_input("Insira uma senha: ")
        if st.button("Inserir"):
            try:
                View.Usuario_Inserir(nome, email, fone, senha)
                st.success("Usuário cadastrado com sucesso!")
                time.sleep(1)
                st.rerun()
            except ValueError:
                st.write("Dados inválidos.")
    
    def AtualizarCategoria():
        user = View.Usuario_Listar()
        if len(user) == 0:
            st.write("Nenhum usuário encontrado.")
        else: 
            select = st.selectbox("Atualizar Cadastro", user)
            nome = st.text_input("Insira o seu novo nome: ", select.get_nome())
            email = st.text_input("Insira o seu novo endereço de e-mail: ", select.get_email())
            fone = st.text_input("Insira o seu novo número de telefone: ", select.get_fone())
            senha = st.text_input("Insira a sua nova senha: ")
            if st.button("Atualizar"):
                id = select.get_id()
                View.Usuario_Atualizar(id, nome, email, fone, senha)
                st.success("Cadastro de usuário atualizado com sucesso!")
                time.sleep(1)
                st.rerun()
    
    def ExcluirCategoria():
        user = View.Usuario_Listar()
        if len(user) == 0:
            st.write("Nenhum usuário encontrado.")
        else:
            select = st.selectbox("Excluir Cadastro", user)
            if st.button("Excluir"):
                id = select.get_id()
                View.Usuario_Excluir(id)
                st.success("Usuário excluído com sucesso!")
                time.sleep(1)
                st.rerun()