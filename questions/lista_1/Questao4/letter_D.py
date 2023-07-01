import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import csv_local
import numpy as np
import seaborn as sns


def getMidPoints(classe):
    midpoints = []
    for i in range(len(classe)):
        mid = (classe[i][0] + classe[i][1]) / 2
        midpoints.append(mid)
    return midpoints


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

classe = [[1.5, 2], [2, 2.5], [2.5, 3], [3, 3.5], [3.5, 4], [4, 4.5], [4.5, 5]]
bins = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]

df = pd.DataFrame(bateriasDeCarro, columns=["Baterias"])
frequencyBeans = pd.cut(df["Baterias"], bins=bins)
frequency_counts = frequencyBeans.value_counts().sort_index()
midPointsArray = getMidPoints(classe)
midpoints_df = pd.DataFrame(
    {"Ponto Médio": midPointsArray, "Frequencia": frequency_counts}
)
midpoints_df["Produto frequencia * ponto médio"] = (
    midpoints_df["Ponto Médio"] * midpoints_df["Frequencia"]
)
total_sum = midpoints_df["Produto frequencia * ponto médio"].sum()
total_sum_frequency = midpoints_df["Frequencia"].sum()
cumulativeMean = total_sum / total_sum_frequency


def letter_D():
    st.subheader("Letra E")
    st.write(
        "Obtenha a variância para os dados originais conforme feito para a média em c."
    )
    st.write(frequencyBeans.value_counts().sort_index(), axis=1)
    st.title("Tabela de ponto médio e frequencia")
    st.write(midpoints_df)
    st.write("Soma das frequencias")
    st.write(total_sum_frequency)
    st.write("Soma do produto frequencia * ponto médio")
    st.write(total_sum)
    st.write(
        "Portanto, a média utilizando a distribuição de frequência com os pontos médios de cada classe é"
    )
    st.write(cumulativeMean)
