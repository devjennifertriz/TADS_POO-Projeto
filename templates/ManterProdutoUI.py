import streamlit as st
import pandas as pd
from view import View
import time

class ManterProdutoUI:
    def Main():
        st.header("Gerenciar Produtos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar Produtos", "Inserir Produtos", "Atualizar Produtos", "Excluir Produtos"])
        with tab1: 
            ManterProdutoUI.ListarProduto()
        with tab2:
            ManterProdutoUI.InserirProduto()
        with tab3:
            ManterProdutoUI.AtualizarProduto()
        with tab4:
            ManterProdutoUI.ExcluirProduto()

    def ListarProduto():
        produto = View.Produto_Listar()
        if len(produto) == 0:
            st.write("Nenhum produto encontrado.")
        else:
            dict = []
            for obj in produto: dict.append(obj.__dict__)
            df = pd.DataFrame(dict)
            st.dataframe(df)
    
    def InserirProduto():
        nome = st.text_input("Insira o nome do produto: ")
        valor = st.number_input("Insira o valor do produto: ")
        idCategoria = st.text_input("Insira a categoria: ")
        if st.button("Inserir"):
            try:
                View.Produto_Inserir(nome, valor, idCategoria)
                st.success("Produto cadastrado com sucesso!")
                time.sleep(1)
                st.rerun()
            except ValueError:
                st.write("Dados inválidos.")
    
    def AtualizarProduto():
        produto = View.Produto_Listar()
        if len(produto) == 0:
            st.write("Nenhum produto encontrado.")
        else: 
            select = st.selectbox("Atualizar Cadastro", produto)
            nome = st.text_input("Insira a nova categoria: ", select.get_nome())
            valor = st.number_input("Insira um novo valor para o produto: ", select.get_valor())
            idCategoria = st.text_input("Insira a categoria: ")
            if st.button("Atualizar"):
                id = select.get_id()
                View.Produto_Atualizar(id, nome, valor, idCategoria)
                st.success("Produto atualizado com sucesso!")
                time.sleep(1)
                st.rerun()
    
    def ExcluirProduto():
        produto = View.Produto_Listar()
        if len(produto) == 0:
            st.write("Nenhum produto encontrado.")
        else:
            select = st.selectbox("Excluir Cadastro", produto)
            if st.button("Excluir"):
                id = select.get_id()
                View.Produto_Excluir(id)
                st.success("Produto excluído com sucesso!")
                time.sleep(1)
                st.rerun()