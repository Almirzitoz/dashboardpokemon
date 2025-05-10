import matplotlib. pyplot as plt
import pandas as pd
import streamlit as st 

df = pd.read_csv("pokemon.csv")

grass = df[df['type1'].str.contains("grass",case=False,na=False)|
           df['type2'].str.contains("grass",case=False,na=False)]

