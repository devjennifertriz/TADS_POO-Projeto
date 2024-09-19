import streamlit as st
import pandas as pd
from view import View
import time

class AbrirContaUI:
  def Main():
    st.header("Vamos ao seu Cadastro!")
    AbrirContaUI.Cadastrar()
  
  def Cadastrar():
    nome = st.text_input("Insira o seu Nome")
    email = st.text_input("Insira o seu e-mail")
    fone = st.text_input("Insira o seu número de telefone")
    senha = st.text_input("Insira a sua nova senha")
    if st.button("Cadastrar"):
      View.Usuario_Inserir(nome, email, fone, senha)
      st.success("Conta criada com sucesso")
      time.sleep(2)
      st.rerun()