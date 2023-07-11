import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import csv_local
import numpy as np
import seaborn as sns
import statistics


dados = pd.DataFrame({"Idades": [42, 35, 27, 21, 55, 18, 27, 30, 21, 24]})

mean = dados["Idades"].mean()
median = statistics.median(dados["Idades"])
mode = statistics.mode(dados["Idades"])
std_dev = statistics.stdev(dados["Idades"])
interval = max(dados["Idades"]) - min(dados["Idades"])


def letter_A():
    st.subheader("(a) Determine as medidas descritivas dos dados que você conhece.")
    st.write("Medidas descritivas:")
    st.write("Média:", mean)
    st.write("Mediana:", median)
    st.write("Moda:", mode)
    st.write("Desvio Padrão:", std_dev)
    st.write("Intervalo:", interval)

    st.subheader(
        """(b) Qual dessas medidas você acredita que será a mais importante para julgar o tamanho final da amostra? Por quê?"""
    )
    st.write(
        "A medida mais importante seria o desvio padrão. O desvio padrão indica a dispersão dos valores em relação à média. Quanto maior o desvio padrão, maior é a variabilidade dos dados e, portanto, uma amostra maior pode ser necessária para representar adequadamente a população."
    )
