from templates.abrircontaui import AbrirContaUI
from templates.loginui import LoginUI
from templates.perfilclienteui import PerfilClienteUI
from templates.manterclienteui import ManterClienteUI
from templates.manterprofissionalui import ManterProfissionalUI
from templates.manterhorarioui import ManterHorarioUI
from templates.manterservicoui import ManterServicoUI
from service import Service
import streamlit as st

class IndexUI:

    def cliente_criar_admin():
            for c in Service.cliente_listar():
                if c.get_email() == "admin": return 
            Service.cliente_inserir("admin", "admin", "fone", "1234")

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados"])
        if op == "Meus Dados": PerfilClienteUI.main()

    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()

    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            admin = st.session_state["usuario_nome"] == "admin"
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            if admin: IndexUI.menu_admin()
            else: IndexUI.menu_cliente()
            IndexUI.sair_do_sistema()

    def main():
            IndexUI.cliente_criar_admin()
            IndexUI.sidebar()

IndexUI.main()