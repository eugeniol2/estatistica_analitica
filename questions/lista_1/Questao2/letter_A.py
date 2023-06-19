import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import csv_local
import numpy as np

UrbanDs, RuralDs = csv_local.getQuestionTwoDataset()


def histogram(ds, table, histogramTitle):
    fig = px.histogram(
        ds[table],
        x=table,
        histnorm="percent",
        text_auto=True,
        labels={table: histogramTitle},
    )
    fig.update_layout(bargap=0.2)

    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)


def letter_A():
    st.subheader("Letra A e B")
    st.write("""Construa os histogramas das duas distribuições.""")
    st.subheader("Resposta:")
    col1, col2 = st.columns(2)
    with col1:
        st.header("Zona urbana")
        st.write(UrbanDs.describe())
    with col2:
        st.header("Zona rural")
        st.write(RuralDs.describe())
    st.header("Zona urbana em porcentagem")
    histogram(UrbanDs, "Zona urbana", "Zona urbanas")
    st.header("Zona rural em porcentagem")
    histogram(RuralDs, "Zona rural", "Zona rural")
    st.header("Conclusão - letra B")
    st.write(
        "Dada a comparação entre gráficos, é possível notar que 40% dos alugueis na zona urbana são da classe 5-7, e na zona rural 50% dos alugueis são 3-5"
    )
