import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import csv_local
import numpy as np
import seaborn as sns
import statistics
from questions.lista_1 import Questao1

df = Questao1.ds


def calculate_zscore(column):
    mean = df[column].mean()
    std = df[column].std()
    zscores = (df[column] - mean) / std
    return zscores


def insertZcolumns():
    right = calculate_zscore("Direito")
    statistic = calculate_zscore("Estatíst.")
    politics = calculate_zscore("Política")
    df["z_Direito"] = right
    df["z_Estatíst."] = statistic
    df["z_Política"] = politics


def letter_A():
    insertZcolumns()
    st.write(df)
    estatistica_zscores = calculate_zscore("Estatíst.")

    mean_zscore = estatistica_zscores.mean()
    std_zscore = estatistica_zscores.std()

    outliers = estatistica_zscores[
        (estatistica_zscores > 2 * std_zscore) | (estatistica_zscores < -2 * std_zscore)
    ]

    st.subheader("Letra A")
    st.write(
        "O valor Z significa, nesse contexto, se um determinado funcionário está acima ou abaixo da média"
    )

    # letra B
    st.subheader(
        "(b) Calcule as notas padronizadas dos funcionários para o exame de Estatística."
    )
    st.write(
        "Foram adicionaras ao final da tabela de dados z_direito, z_estatíst e z_política"
    )

    # letra C
    st.subheader("Letra C")
    st.write("Média", mean_zscore)
    st.write("Desvio padrão", std_zscore)

    # letra D
    st.subheader("Letra D")
    if outliers.empty:
        st.write("Não há casos atípicos.")
    else:
        st.write("Existem casos atípicos:", outliers)
    # Letra E

    score_direito = 9.0
    score_estatistica = 9.0
    score_politica = 9.0

    mean_direito = df["Direito"].mean()
    std_direito = df["Direito"].std()
    zscore_direito = (score_direito - mean_direito) / std_direito

    mean_estatistica = df["Estatíst."].mean()
    std_estatistica = df["Estatíst."].std()
    zscore_estatistica = (score_estatistica - mean_estatistica) / std_estatistica

    mean_politica = df["Política"].mean()
    std_politica = df["Política"].std()
    zscore_politica = (score_politica - mean_politica) / std_politica

    st.subheader(
        "(e) O funcionário 1 obteve 9,0 em Direito, em Estatística e em Política. Em que disciplina o seu desempenho relativo foi melhor?"
    )

    st.write("Estatistica:", zscore_estatistica)
    st.write("Politica:", zscore_politica)
    st.write("Direito:", zscore_direito)
    st.write("Portanto o melhor desempenho foi política")
