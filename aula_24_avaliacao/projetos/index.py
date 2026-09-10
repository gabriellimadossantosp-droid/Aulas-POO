from templates.manterclienteui import ManterClienteUI
from templates.manterconvenioui import ManterConvenioUI
import streamlit as st

class IndexUI:
    def main():
        op = st.sidebar.selectbox("Menu", ["Clientes", "Convênios"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Serviços": ManterConvenioUI.main()

IndexUI.main()