import streamlit as st
import pandas as pd
from service import Service

class ListarAgendaProfissionalUI:
    def main():
        st.header('Agenda do Profissional')
        profissionais = Service.profissional_listar()
        
        if len(profissionais) == 0:
            st.write('Nenhum profissional cadastrado')
        else:
            def formatar_nome(p):
                return p.get_nome()
            prof = st.selectbox('Selecione o profissional', profissionais, format_func=formatar_nome)
            
            if prof != None:
                horarios = Service.profissional_visualizar_minha_agenda(prof.get_id())
                
                if len(horarios) == 0:
                    st.write('Nenhum horário cadastrado')
                else:
                    list_dic = []
                    for obj in horarios:
                        cliente = Service.cliente_listar_id(obj.get_id_cliente())
                        servico = Service.servico_listar_id(obj.get_id_servico())
                        
                        if cliente != None: cliente = cliente.get_nome()
                        if servico != None: servico = servico.get_descricao()
                        
                        list_dic.append({
                            'id': obj.get_id(),
                            'data': obj.get_data(),
                            'cliente': cliente,
                            'serviço': servico
                        })
                    df = pd.DataFrame(list_dic)
                    st.dataframe(df)