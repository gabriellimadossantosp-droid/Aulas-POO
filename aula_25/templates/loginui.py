import streamlit as st
from service import Service

class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("E-mail: ", placeholder="digite seu email")
        senha = st.text_input("Senha: ", type="password", placeholder="digite sua senha")
        if st.button("Entrar"):
            c = Service.cliente_autenticar(email, senha)
            if c != None:
                st.session_state["usuario_id"] = c["id"]
                st.session_state["usuario_nome"] = c["nome"]
                st.session_state["usuario_tipo"] = "cliente"
                st.rerun()
 
            p = Service.profissional_autenticar(email, senha)
            if p != None:
                st.session_state["usuario_id"] = p["id"]
                st.session_state["usuario_nome"] = p["nome"]
                st.session_state["usuario_tipo"] = "profissional"
                st.rerun()
  
            if c == None and p == None: st.write("E-mail ou senha inválidos")