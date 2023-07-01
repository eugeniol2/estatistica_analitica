import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import csv_local
import numpy as np
import seaborn as sns

bateriasDeCarro = [
    2.2,
    4.1,
    3.5,
    4.5,
    3.2,
    3.7,
    3.0,
    2.6,
    3.4,
    1.6,
    3.1,
    3.3,
    3.8,
    3.1,
    4.7,
    3.7,
    2.5,
    4.3,
    3.4,
    3.6,
    2.9,
    3.3,
    3.9,
    3.1,
    3.3,
    3.1,
    3.7,
    4.4,
    3.2,
    4.1,
    1.9,
    3.4,
    4.7,
    3.8,
    3.2,
    2.6,
    3.9,
    3.0,
    4.2,
    3.5,
]

df = pd.DataFrame(bateriasDeCarro, columns=["Baterias"])
bins = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
frequencyBeans = pd.cut(df["Baterias"], bins=bins).sort_index()


def letter_B():
    st.subheader("Letra B")
    st.write("Faça o gráfico da distribuição de frequências relativas acumuladas.")
    st.write(frequencyBeans.value_counts().sort_index())
    plt.xticks(rotation=45, ha="right")
    fig = px.histogram(
        df,
        x="Baterias",
        nbins=len(bins),
        histnorm="percent",
        hover_data=["Baterias"],
        cumulative=True,
    )
    fig.update_layout(bargap=0.2)
    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)
