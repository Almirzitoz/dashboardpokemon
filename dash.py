import matplotlib. pyplot as plt
import pandas as pd
import streamlit as st 
import numpy as np

df = pd.read_csv("pokemon.csv")

media_total = df[df['generation'] > 0].groupby('generation')['total'].mean()
media_status = df[df['generation'] > 0].groupby('generation')[['hp','attack','defense','sp_attack','sp_defense','speed']].max()
tipos_type1 = df[df['generation'] > 0].groupby('generation')['type1'].agg(lambda x: x.mode()[0])  # Most common type1 per generation
tipos_type2 = df[df['generation'] > 0].groupby('generation')['type2'].agg(lambda x: x.mode()[0])  # Most common type2 per generation


with st.sidebar:
    st.title("Fitro de opções")

def main():
    col1,col2 =st.columns(2)
    col3,col4 = st.columns(2)
    with col1:
        st.title("Media dos status base por geração")
        grafico_linha = st.line_chart(data=media_status)
    with col2:
     st.title("Media dos status base por geração")
     st.scatter_chart(data=media_status)
    with col3:
     st.title("Media do status total por geração")
     grafico_colula =st.bar_chart(data= media_total)
     
    tipos_comuns = pd.concat([tipos_type1, tipos_type2]).value_counts()
    
    with col4:
        st.title("Tipos mais comuns em todas as gerações")
        fig, grafico = plt.subplots()
        grafico.pie(tipos_comuns, labels=tipos_comuns.index, autopct='%1.1f%%', startangle=90)
        grafico.axis('equal')
        st.pyplot(fig)
main()
