import streamlit as st
from view import View
import time

class LoginUI:
  def Main():
    st.header("Seja Bem-Vindo a Doceria SweetYou!")
    LoginUI.SistemaEntrar()

  def SistemaEntrar():
    email = st.text_input("Insira o e-mail para fazer Login")
    senha = st.text_input("Insira a senha para fazer Login")

    if st.button("Entrar"):
      
      user = View.Usuario_Login(email, senha) 
      if user is not None:
        st.success("Você está logado no sistema!")
        st.success("Bem-vindo(a), " + user.get_nome())
        st.session_state["user_id"] = user.get_id()
        st.session_state["user_nome"] = user.get_nome()
      else:
        st.error("Usuário ou senha inválido(s).")
      time.sleep(2)
      st.rerun()      