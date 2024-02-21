import pandas as pd
import streamlit as st
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
'''
if 'df_jan' not in st.session_state:
    df = pd.read_excel('datasets/fusex.xlsx', sheet_name='JAN 23')
    st.session_state['df_jan'] = df
    sns.barplot(
        x= df['PROCEDIMENTO'],
        y= df['TOTAL AUTORIZADO']
    )

st.markdown("# ANALISE DE DADOS 2023 " )
'''

st.title('# ANALISE DE DADOS 2023')

date_column = 'date/time'
#data_url = ('https://docs.google.com/spreadsheets/d/1Ec1-dsyPX98Xv4OFQxLt2-umkn7OLfGf/edit?usp=drive_link&ouid=118393292491497779885&rtpof=true&sd=true')
#new = ('datasets/fusex.xlsx', sheet_name='JAN 23')

def load_data(nrwos):
    data = pd.read_excel('datasets/fusex.xlsx', sheet_name='JAN 23', nrows=nrwos)
    def lowercase(x): return str(x).lower()
    data.rename(lowercase, axis='columns', inplace='True')
    #data[date_column] = pd.to_datetime(data[date_column])
    return data


data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text('Loading data... done')

@st.cache_data

def load_data(nrows):
    data_load_state.text('Done! (using st.cache_data)')


st.subheader('Raw data')
st.write(data)

st.subheader('PRIMEIRA ANALISE')

#hist_values = np.histogram(data, density=True)[3]

#st.mapa(data)
ocs = data['ocs']

fig, ax = plt.subplots()
ax.hist(ocs, bins=20)
st.pyplot(fig)