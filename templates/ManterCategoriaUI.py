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
        cat = View.Categoria_Listar()
        if len(cat) == 0:
            st.write("Nenhuma categoria encontrada.")
        else:
            dict = []
            for obj in cat: dict.append(obj.__dict__)
            df = pd.DataFrame(dict)
            st.dataframe(df)
    
    def InserirCategoria():
        nome = st.text_input("Insira o nome da categoria: ")
        desc = st.text_input("Descreva a categoria: ")
        if st.button("Inserir"):
            try:
                View.Categoria_Inserir(nome, desc)
                st.success("Categoria cadastrada com sucesso!")
                time.sleep(1)
                st.rerun()
            except ValueError:
                st.write("Dados inválidos.")
    
    def AtualizarCategoria():
        cat = View.Categoria_Listar()
        if len(cat) == 0:
            st.write("Nenhuma categoria encontrada.")
        else: 
            select = st.selectbox("Atualizar Cadastro", cat)
            nome = st.text_input("Insira a nova categoria: ", select.get_nome())
            desc = st.text_input("Insira uma nova descrição para a categoria: ", select.get_desc())
            if st.button("Atualizar"):
                id = select.get_id()
                View.Categoria_Atualizar(id, nome, desc)
                st.success("Categoria atualizada com sucesso!")
                time.sleep(1)
                st.rerun()
    
    def ExcluirCategoria():
        cat = View.Categoria_Listar()
        if len(cat) == 0:
            st.write("Nenhuma categoria encontrada.")
        else:
            select = st.selectbox("Excluir Cadastro", cat)
            if st.button("Excluir"):
                id = select.get_id()
                View.Categoria_Excluir(id)
                st.success("Categoria excluída com sucesso!")
                time.sleep(1)
                st.rerun()