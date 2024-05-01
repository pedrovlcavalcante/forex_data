import streamlit as st
from quote import get_currency_list
from historical_data import load_historical_data, separate
import pandas as pd
import plotly.express as px

currency_list = get_currency_list()
historical_data = load_historical_data()

def display_label(x):
    label = x[0:3]+'/'+x[3:6]
    return label

dias = st.number_input('Nº de dias para mostrar no gráfico', value=50, max_value=300)
option = st.selectbox(
    'Escolher cotação',
    (currency['symbol'] for currency in currency_list),
    format_func=display_label)

symbol = separate(historical_data, option)
df = pd.DataFrame(symbol)

fig = px.line(df.loc[:dias], x="date", y="close", title='Close')

st.plotly_chart(figure_or_data=fig)

l1 = option[:3]
l2 = option[3:]

close = df['close'][0]

c1 = st.sidebar.number_input(f'Valor em {l1}', value=1.0, step=.01)
c2 = st.sidebar.number_input(f'Valor em {l2}', value=c1*close, step=.01, disabled=True)
