import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
'''
st.markdown('# MÊS DE JANEIRO')

df = st.session_state['df_jan']

def exclui():
    del df['ENTRADA SECRETARIA']
    del df['SAÍDA  SECRETÁRIA']
    del df['STATUS SEC']
    del df['DIAS']
    del df['ENTRADA / DIVISAO DE MEDICINA ']
    del df['SAIDA / DIVISAO DE MEDICINA']
    del df['LINK DO PROC']
    del df['TELEFONE BENEFICIÁRIO']
    del df['PREC-CP']
    del df['ENTRADA  AUDITORIA']
    del df['ENTRADA ENFERMAGEM']
    del df['AUDITORIA ENFERMAGEM']
    del df['SAÍDA ENFERMAGEM']
    del df['DIAS.1']
    del df['AUDITORIA MÉDICA']
    del df['ENTRADA MÉDICA']
    del df['SAÍDA MÉDICA']
    del df['DIAS.2']
    del df['STATUS DA SOLICITAÇÃO']
    del df['DATA DA PENDÊNCIA']
    del df['RESPONSÁVEL PELA SOLUÇÃO']
    del df['OBSERVAÇÕES']
    del df['GUIA HM']
    del df['GUIA ANEST']
    del df['GUIA OPME']
    del df['GUIA HOSP']
    del df['Nº DA AUTZ']
    del df['ENTREGA SECRETARIA']
    del df['ENTREGA BENEFICIÁRIO']
    del df['OBSERVAÇÃO SECRETARIA']
    del df['TEMPO TOTAL PROCESSO']
    del df['EMAIL BENEFICIÁRIO']
    del df['NOME DO BENEFICIÁRIO']
    del df['NR']

exclui()   




col1, col2, col3, col4 = st.columns(4)

col1.markdown(f'**PROCEDIMENTO:** {df["PROCEDIMENTO"]}')
col2.markdown(f'**ESPECIALIDADE:** {df["ESPECIALIDADE"]}')
col3.markdown(f'**OCS:** {df["OCS"]}')
col4.markdown(f'**TOTAL AUTORIZADO:** {df["TOTAL AUTORIZADO"]}')
st.divider()

df_proc = df.loc(df['PROCEDIMENTO'])
df_val = df.loc(df['TOTAL AUTORIZADO'])

x1 = df_proc
y1 = df_val

plt.bar(x1, label='PROCEDIMENTOS', width=0.5, align='edge') 
plt.bar(y1, label='TOTAL AUTORIZADO', width=0.5, align='edge') 
plt.legend()
plt.show()

st.pyplot(plt)
'''







st.write(df)
