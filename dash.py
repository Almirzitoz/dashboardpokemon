import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st 
import numpy as np

df = pd.read_csv("data/pokemon.csv")

geracoes = sorted(df['generation'].unique())


with st.sidebar:
    st.title("Fitro de opções")
    geracao_escolhida = st.selectbox("Selecione uma geração",geracoes)

def main():
    media_total = df[df['generation'] > 0].groupby('generation')['total'].mean()
    media_status = df[df['generation'] > 0].groupby('generation')[['hp','attack','defense','sp_attack','sp_defense','speed']].max()
    tipos_type1 = df['type1'].value_counts()
    tipos_type2 = df['type2'].value_counts()

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
     
    
    with col4:
        st.title("Tipos primários mais comuns")
        fig, grafico = plt.subplots()
        grafico.pie(tipos_type1, labels=tipos_type1.index, autopct='%1.1f%%', startangle=90)
        grafico.axis('equal')
        st.pyplot(fig)
        
        st.title("Tipo secundários mais comuns")
        fig2,graf2 = plt.subplots()
        graf2.pie(tipos_type2, labels=tipos_type2.index, autopct='%1.1f%%', startangle=90)
        graf2.axis('equal')
        st.pyplot(fig2)

def gen1():
    df_filtrado = df[df['generation'] == 1]
    
    maior_speed = df_filtrado.groupby('name')['speed'].max().sort_values(ascending=False)
    maior_attack = df_filtrado.groupby('name')['attack'].max().sort_values(ascending=False)
    maior_hp = df_filtrado.groupby('name')['hp'].max().sort_values(ascending=False)
    maior_def =df_filtrado.groupby('name')['defense'].max().sort_values(ascending=False)
    maior_spa = df_filtrado.groupby('name')['sp_attack'].max().sort_values(ascending=False)
    maior_spdef = df_filtrado.groupby('name')['sp_defense'].max().sort_values(ascending=False)
    
    tipo1 = df_filtrado['type1'].value_counts()
    tipo2 = df_filtrado['type2'].value_counts()
    
    
    col1,col2 =st.columns(2)
    col3,col4 = st.columns(2)
    
    with col1:
     st.title("Top 10 pokemons HP")
     st.bar_chart(data=maior_hp.head(10))
     st.title("Top 10 pokemons Speed")
     st.bar_chart(data=maior_speed.head(10))
    with col2:
     st.title("Top 10 pokemons attack")
     st.bar_chart(data=maior_attack.head(10))
     st.title("Top 10 pokemons special attack")
     st.bar_chart(data=maior_spa.head(10))
    with col3:
     st.title("Top 10 pokemons defense")
     st.bar_chart(data=maior_def.head(10))
     st.title("Top 10 pokemons special defense")
     st.bar_chart(data=maior_spdef.head(10))
    with col4:
     st.title("Tipos primários mais comuns")
     fig, grafico = plt.subplots()
     grafico.pie(tipo1, labels=tipo1.index, autopct='%1.1f%%', startangle=90)
     grafico.axis('equal')
     st.pyplot(fig)
        
     st.title("Tipo secundários mais comuns")
     fig2,graf2 = plt.subplots()
     graf2.pie(tipo2, labels=tipo2.index, autopct='%1.1f%%', startangle=90)
     graf2.axis('equal')
     st.pyplot(fig2)
    top_max = df_filtrado.groupby('name')['total'].max().sort_values(ascending=False)
    st.title("Top 10 pokemons status total")
    st.bar_chart(data=top_max.head(10))
     
def gen2():
    df_filtrado = df[df['generation'] == 2]
    
    maior_speed = df_filtrado.groupby('name')['speed'].max().sort_values(ascending=False)
    maior_attack = df_filtrado.groupby('name')['attack'].max().sort_values(ascending=False)
    maior_hp = df_filtrado.groupby('name')['hp'].max().sort_values(ascending=False)
    maior_def =df_filtrado.groupby('name')['defense'].max().sort_values(ascending=False)
    maior_spa = df_filtrado.groupby('name')['sp_attack'].max().sort_values(ascending=False)
    maior_spdef = df_filtrado.groupby('name')['sp_defense'].max().sort_values(ascending=False)
    
    tipo1 = df_filtrado['type1'].value_counts()
    tipo2 = df_filtrado['type2'].value_counts()
    
    col1,col2 =st.columns(2)
    col3,col4 = st.columns(2)
    
    with col1:
     st.title("Top 10 pokemons HP")
     st.bar_chart(data=maior_hp.head(10))
     st.title("Top 10 pokemons Speed")
     st.bar_chart(data=maior_speed.head(10))
    with col2:
     st.title("Top 10 pokemons attack")
     st.bar_chart(data=maior_attack.head(10))
     st.title("Top 10 pokemons special attack")
     st.bar_chart(data=maior_spa.head(10))
    with col3:
     st.title("Top 10 pokemons defense")
     st.bar_chart(data=maior_def.head(10))
     st.title("Top 10 pokemons special defense")
     st.bar_chart(data=maior_spdef.head(10))
    with col4:
     st.title("Tipos primários mais comuns")
     fig, grafico = plt.subplots()
     grafico.pie(tipo1, labels=tipo1.index, autopct='%1.1f%%', startangle=90)
     grafico.axis('equal')
     st.pyplot(fig)
        
     st.title("Tipo secundários mais comuns")
     fig2,graf2 = plt.subplots()
     graf2.pie(tipo2, labels=tipo2.index, autopct='%1.1f%%', startangle=90)
     graf2.axis('equal')
     st.pyplot(fig2)
    top_max = df_filtrado.groupby('name')['total'].max().sort_values(ascending=False)
    st.title("Top 10 pokemons status total")
    st.bar_chart(data=top_max.head(10))
    
def gen3():
    df_filtrado = df[df['generation'] == 3]
    
    maior_speed = df_filtrado.groupby('name')['speed'].max().sort_values(ascending=False)
    maior_attack = df_filtrado.groupby('name')['attack'].max().sort_values(ascending=False)
    maior_hp = df_filtrado.groupby('name')['hp'].max().sort_values(ascending=False)
    maior_def =df_filtrado.groupby('name')['defense'].max().sort_values(ascending=False)
    maior_spa = df_filtrado.groupby('name')['sp_attack'].max().sort_values(ascending=False)
    maior_spdef = df_filtrado.groupby('name')['sp_defense'].max().sort_values(ascending=False)
    
    tipo1 = df_filtrado['type1'].value_counts()
    tipo2 = df_filtrado['type2'].value_counts()
    
    col1,col2 =st.columns(2)
    col3,col4 = st.columns(2)
    
    with col1:
     st.title("Top 10 pokemons HP")
     st.bar_chart(data=maior_hp.head(10))
     st.title("Top 10 pokemons Speed")
     st.bar_chart(data=maior_speed.head(10))
    with col2:
     st.title("Top 10 pokemons attack")
     st.bar_chart(data=maior_attack.head(10))
     st.title("Top 10 pokemons special attack")
     st.bar_chart(data=maior_spa.head(10))
    with col3:
     st.title("Top 10 pokemons defense")
     st.bar_chart(data=maior_def.head(10))
     st.title("Top 10 pokemons special defense")
     st.bar_chart(data=maior_spdef.head(10))
    with col4:
     st.title("Tipos primários mais comuns")
     fig, grafico = plt.subplots()
     grafico.pie(tipo1, labels=tipo1.index, autopct='%1.1f%%', startangle=90)
     grafico.axis('equal')
     st.pyplot(fig)
        
     st.title("Tipo secundários mais comuns")
     fig2,graf2 = plt.subplots()
     graf2.pie(tipo2, labels=tipo2.index, autopct='%1.1f%%', startangle=90)
     graf2.axis('equal')
     st.pyplot(fig2)
    top_max = df_filtrado.groupby('name')['total'].max().sort_values(ascending=False)
    st.title("Top 10 pokemons status total")
    st.bar_chart(data=top_max.head(10))
     
def gen4():
    df_filtrado = df[df['generation'] == 4]
    
    maior_speed = df_filtrado.groupby('name')['speed'].max().sort_values(ascending=False)
    maior_attack = df_filtrado.groupby('name')['attack'].max().sort_values(ascending=False)
    maior_hp = df_filtrado.groupby('name')['hp'].max().sort_values(ascending=False)
    maior_def =df_filtrado.groupby('name')['defense'].max().sort_values(ascending=False)
    maior_spa = df_filtrado.groupby('name')['sp_attack'].max().sort_values(ascending=False)
    maior_spdef = df_filtrado.groupby('name')['sp_defense'].max().sort_values(ascending=False)
    
    tipo1 = df_filtrado['type1'].value_counts()
    tipo2 = df_filtrado['type2'].value_counts()
    
    col1,col2 =st.columns(2)
    col3,col4 = st.columns(2)
    
    with col1:
     st.title("Top 10 pokemons HP")
     st.bar_chart(data=maior_hp.head(10))
     st.title("Top 10 pokemons Speed")
     st.bar_chart(data=maior_speed.head(10))
    with col2:
     st.title("Top 10 pokemons attack")
     st.bar_chart(data=maior_attack.head(10))
     st.title("Top 10 pokemons special attack")
     st.bar_chart(data=maior_spa.head(10))
    with col3:
     st.title("Top 10 pokemons defense")
     st.bar_chart(data=maior_def.head(10))
     st.title("Top 10 pokemons special defense")
     st.bar_chart(data=maior_spdef.head(10))
    with col4:
     st.title("Tipos primários mais comuns")
     fig, grafico = plt.subplots()
     grafico.pie(tipo1, labels=tipo1.index, autopct='%1.1f%%', startangle=90)
     grafico.axis('equal')
     st.pyplot(fig)
        
     st.title("Tipo secundários mais comuns")
     fig2,graf2 = plt.subplots()
     graf2.pie(tipo2, labels=tipo2.index, autopct='%1.1f%%', startangle=90)
     graf2.axis('equal')
     st.pyplot(fig2)
    top_max = df_filtrado.groupby('name')['total'].max().sort_values(ascending=False)
    st.title("Top 10 pokemons status total")
    st.bar_chart(data=top_max.head(10))
     
def gen5():
    df_filtrado = df[df['generation'] == 5]
    
    maior_speed = df_filtrado.groupby('name')['speed'].max().sort_values(ascending=False)
    maior_attack = df_filtrado.groupby('name')['attack'].max().sort_values(ascending=False)
    maior_hp = df_filtrado.groupby('name')['hp'].max().sort_values(ascending=False)
    maior_def =df_filtrado.groupby('name')['defense'].max().sort_values(ascending=False)
    maior_spa = df_filtrado.groupby('name')['sp_attack'].max().sort_values(ascending=False)
    maior_spdef = df_filtrado.groupby('name')['sp_defense'].max().sort_values(ascending=False)
    
    tipo1 = df_filtrado['type1'].value_counts()
    tipo2 = df_filtrado['type2'].value_counts()
    
    col1,col2 =st.columns(2)
    col3,col4 = st.columns(2)
    
    with col1:
     st.title("Top 10 pokemons HP")
     st.bar_chart(data=maior_hp.head(10))
     st.title("Top 10 pokemons Speed")
     st.bar_chart(data=maior_speed.head(10))
    with col2:
     st.title("Top 10 pokemons attack")
     st.bar_chart(data=maior_attack.head(10))
     st.title("Top 10 pokemons special attack")
     st.bar_chart(data=maior_spa.head(10))
    with col3:
     st.title("Top 10 pokemons defense")
     st.bar_chart(data=maior_def.head(10))
     st.title("Top 10 pokemons special defense")
     st.bar_chart(data=maior_spdef.head(10))
    with col4:
     st.title("Tipos primários mais comuns")
     fig, grafico = plt.subplots()
     grafico.pie(tipo1, labels=tipo1.index, autopct='%1.1f%%', startangle=90)
     grafico.axis('equal')
     st.pyplot(fig)
        
     st.title("Tipo secundários mais comuns")
     fig2,graf2 = plt.subplots()
     graf2.pie(tipo2, labels=tipo2.index, autopct='%1.1f%%', startangle=90)
     graf2.axis('equal')
     st.pyplot(fig2)
    top_max = df_filtrado.groupby('name')['total'].max().sort_values(ascending=False)
    st.title("Top 10 pokemons status total")
    st.bar_chart(data=top_max.head(10))
     
def gen6():
    df_filtrado = df[df['generation'] == 6]
    
    maior_speed = df_filtrado.groupby('name')['speed'].max().sort_values(ascending=False)
    maior_attack = df_filtrado.groupby('name')['attack'].max().sort_values(ascending=False)
    maior_hp = df_filtrado.groupby('name')['hp'].max().sort_values(ascending=False)
    maior_def =df_filtrado.groupby('name')['defense'].max().sort_values(ascending=False)
    maior_spa = df_filtrado.groupby('name')['sp_attack'].max().sort_values(ascending=False)
    maior_spdef = df_filtrado.groupby('name')['sp_defense'].max().sort_values(ascending=False)
    
    tipo1 = df_filtrado['type1'].value_counts()
    tipo2 = df_filtrado['type2'].value_counts()
    
    col1,col2 =st.columns(2)
    col3,col4 = st.columns(2)
    
    with col1:
     st.title("Top 10 pokemons HP")
     st.bar_chart(data=maior_hp.head(10))
     st.title("Top 10 pokemons Speed")
     st.bar_chart(data=maior_speed.head(10))
    with col2:
     st.title("Top 10 pokemons attack")
     st.bar_chart(data=maior_attack.head(10))
     st.title("Top 10 pokemons special attack")
     st.bar_chart(data=maior_spa.head(10))
    with col3:
     st.title("Top 10 pokemons defense")
     st.bar_chart(data=maior_def.head(10))
     st.title("Top 10 pokemons special defense")
     st.bar_chart(data=maior_spdef.head(10))
    with col4:
     st.title("Tipos primários mais comuns")
     fig, grafico = plt.subplots()
     grafico.pie(tipo1, labels=tipo1.index, autopct='%1.1f%%', startangle=90)
     grafico.axis('equal')
     st.pyplot(fig)
        
     st.title("Tipo secundários mais comuns")
     fig2,graf2 = plt.subplots()
     graf2.pie(tipo2, labels=tipo2.index, autopct='%1.1f%%', startangle=90)
     graf2.axis('equal')
     st.pyplot(fig2)
    top_max = df_filtrado.groupby('name')['total'].max().sort_values(ascending=False)
    st.title("Top 10 pokemons status total")
    st.bar_chart(data=top_max.head(10))
     
def gen7():
    df_filtrado = df[df['generation'] == 7]
    
    maior_speed = df_filtrado.groupby('name')['speed'].max().sort_values(ascending=False)
    maior_attack = df_filtrado.groupby('name')['attack'].max().sort_values(ascending=False)
    maior_hp = df_filtrado.groupby('name')['hp'].max().sort_values(ascending=False)
    maior_def =df_filtrado.groupby('name')['defense'].max().sort_values(ascending=False)
    maior_spa = df_filtrado.groupby('name')['sp_attack'].max().sort_values(ascending=False)
    maior_spdef = df_filtrado.groupby('name')['sp_defense'].max().sort_values(ascending=False)
    
    tipo1 = df_filtrado['type1'].value_counts()
    tipo2 = df_filtrado['type2'].value_counts()
    
    col1,col2 =st.columns(2)
    col3,col4 = st.columns(2)
    
    with col1:
     st.title("Top 10 pokemons HP")
     st.bar_chart(data=maior_hp.head(10))
     st.title("Top 10 pokemons Speed")
     st.bar_chart(data=maior_speed.head(10))
    with col2:
     st.title("Top 10 pokemons attack")
     st.bar_chart(data=maior_attack.head(10))
     st.title("Top 10 pokemons special attack")
     st.bar_chart(data=maior_spa.head(10))
    with col3:
     st.title("Top 10 pokemons defense")
     st.bar_chart(data=maior_def.head(10))
     st.title("Top 10 pokemons special defense")
     st.bar_chart(data=maior_spdef.head(10))
    with col4:
     st.title("Tipos primários mais comuns")
     fig, grafico = plt.subplots()
     grafico.pie(tipo1, labels=tipo1.index, autopct='%1.1f%%', startangle=90)
     grafico.axis('equal')
     st.pyplot(fig)
        
     st.title("Tipo secundários mais comuns")
     fig2,graf2 = plt.subplots()
     graf2.pie(tipo2, labels=tipo2.index, autopct='%1.1f%%', startangle=90)
     graf2.axis('equal')
     st.pyplot(fig2)
    top_max = df_filtrado.groupby('name')['total'].max().sort_values(ascending=False)
    st.title("Top 10 pokemons status total")
    st.bar_chart(data=top_max.head(10))
     
def gen8():
    df_filtrado = df[df['generation'] == 8]
    
    maior_speed = df_filtrado.groupby('name')['speed'].max().sort_values(ascending=False)
    maior_attack = df_filtrado.groupby('name')['attack'].max().sort_values(ascending=False)
    maior_hp = df_filtrado.groupby('name')['hp'].max().sort_values(ascending=False)
    maior_def =df_filtrado.groupby('name')['defense'].max().sort_values(ascending=False)
    maior_spa = df_filtrado.groupby('name')['sp_attack'].max().sort_values(ascending=False)
    maior_spdef = df_filtrado.groupby('name')['sp_defense'].max().sort_values(ascending=False)
    
    tipo1 = df_filtrado['type1'].value_counts()
    tipo2 = df_filtrado['type2'].value_counts()
    
    col1,col2 =st.columns(2)
    col3,col4 = st.columns(2)
    
    with col1:
     st.title("Top 10 pokemons HP")
     st.bar_chart(data=maior_hp.head(10))
     st.title("Top 10 pokemons Speed")
     st.bar_chart(data=maior_speed.head(10))
    with col2:
     st.title("Top 10 pokemons attack")
     st.bar_chart(data=maior_attack.head(10))
     st.title("Top 10 pokemons special attack")
     st.bar_chart(data=maior_spa.head(10))
    with col3:
     st.title("Top 10 pokemons defense")
     st.bar_chart(data=maior_def.head(10))
     st.title("Top 10 pokemons special defense")
     st.bar_chart(data=maior_spdef.head(10))
    with col4:
     st.title("Tipos primários mais comuns")
     fig, grafico = plt.subplots()
     grafico.pie(tipo1, labels=tipo1.index, autopct='%1.1f%%', startangle=90)
     grafico.axis('equal')
     st.pyplot(fig)
        
     st.title("Tipo secundários mais comuns")
     fig2,graf2 = plt.subplots()
     graf2.pie(tipo2, labels=tipo2.index, autopct='%1.1f%%', startangle=90)
     graf2.axis('equal')
     st.pyplot(fig2)
    top_max = df_filtrado.groupby('name')['total'].max().sort_values(ascending=False)
    st.title("Top 10 pokemons status total")
    st.bar_chart(data=top_max.head(10))
    
if geracao_escolhida == 0:
    main()
elif geracao_escolhida == 1:
    gen1()
elif geracao_escolhida == 2:
    gen2()
elif geracao_escolhida == 3:
    gen3()
elif geracao_escolhida == 4:
    gen4()
elif geracao_escolhida == 5:
    gen5()
elif geracao_escolhida == 6:
    gen6()
elif geracao_escolhida == 7:
    gen7()
elif geracao_escolhida == 8:
    gen8()