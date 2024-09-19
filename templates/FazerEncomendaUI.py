import streamlit as st
from view import View

class FazerEncomendaUI:
    def Main(): 
        st.subheader("Adicionar Encomenda")
        FazerEncomendaUI.FazerPedido()

    def FazerPedido():
        
        #atributos encomenda

        #id = st.number_input("Id da encomenda", min_value=0)
        st.text("Nossos produtos:")
        itens = View.Item_Listar()

        item = st.selectbox("", itens)
        endereco = st.text_input("Endereço de Entrega")
        status = "Pendente"
        valorT = st.number_input("Valor total", min_value=0.0)
        #idusuario = st.number_input("Id do usuário", min_value=0)
        idusuario = 0

        #item = View.Item_Listar()
        #op = st.selectbox("", item)
        #atributos item
        #idi = st.number_input("Id do Item", min_value=0)
        quantidade = st.text_input("Quantidade")
        valor = st.number_input("Valor do produto")
        idencomenda = 0
        idproduto = st.multiselect(item)
        
        if st.button("Pedir"):
            status = "Pedido feito"
            View.Item_Inserir(quantidade, valor, idencomenda, idproduto)
            View.Encomenda_Inserir(endereco, status, valorT, idusuario)
            
            st.success("Pedido feito com sucesso!")
            print("O número do seu pedido é:")

            
            #item = View.Item_Listar()
            #op = st.selectbox("", item)