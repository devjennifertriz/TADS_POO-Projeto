import streamlit as st
from view import View

class FazerEncomendaUI:
    def Main(): 
        st.subheader("Adicionar Encomenda")
        FazerEncomendaUI.FazerPedido()

    def FazerPedido():
        
        #atributos encomenda

        st.text("Nossos produtos:")
        produtos = View.Produto_Listar()
        st.table(produtos)

        endereco = st.text_input("Endereço de Entrega")
        status = "Pendente"
        valorT = 0
        idusuario = 0

        #idi = st.number_input("Id do Item", min_value=0)
        
        if st.button("Pedir"):
            status = "Pedido feito"
            View.Encomenda_Inserir(endereco, status, valorT, idusuario)
            
            st.success("Pedido feito com sucesso!")
            print("O número do seu pedido é:")

            