import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import csv_local
import numpy as np
import seaborn as sns
import statistics


Question9dataset = pd.read_csv("csv_local/midpointsListOneQuestionFour.csv")

midpoints_df = pd.DataFrame(
    {
        "Estudantes": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "1a": [2.5, 2.0, 8.5, 3.5, 3.0, 6.0, 8.0, 1.5, 7.5, 5.5],
        "2a": [4.5, 8.5, 10.0, 5.5, 5.0, 3.0, 1.5, 2.0, 8.0, 4.5],
        "3a": [5.0, 7.0, 9.0, 8.5, 6.0, 4.0, 2.0, 1.0, 8.5, 5.0],
        "4a": [6.0, 3.0, 8.5, 7.5, 4.5, 5.0, 9.0, 2.5, 10.0, 4.5],
        "Optativa": [7.0, 5.0, 0, 6.5, 5.0, 2.0, 5.0, 0, 0, 2.5],
    }
)

full_period = pd.DataFrame(
    {
        "Periodo": [
            2.5,
            2.0,
            8.5,
            3.5,
            3.0,
            6.0,
            8.0,
            1.5,
            7.5,
            5.5,
            4.5,
            8.5,
            10.0,
            5.5,
            5.0,
            3.0,
            1.5,
            2.0,
            8.0,
            4.5,
            5.0,
            7.0,
            9.0,
            8.5,
            6.0,
            4.0,
            2.0,
            1.0,
            8.5,
            5.0,
            6.0,
            3.0,
            8.5,
            7.5,
            4.5,
            5.0,
            9.0,
            2.5,
            10.0,
            4.5,
        ]
    }
)


def replace_min_with_optativa(row):
    min_value = np.nanmin(row[1:])
    if not np.isnan(min_value) and min_value != 0:
        min_index = np.where(row[1:] == min_value)[0][0] + 1
        row[min_index] = row["Optativa"]
    return row


midpoints_df_refined = midpoints_df.apply(replace_min_with_optativa, axis=1)
midpoints_df_refined["Média de cada estudante"] = midpoints_df_refined.iloc[
    :, 1:-1
].mean(axis=1)


def letter_B():
    st.subheader("Letra B")
    new_labels = ["Média", "Mediana", "Variância", "Desvio padrão"]
    st.subheader(
        "B Para cada prova: média, moda, mediana, variância, desvio-padrão, erro-padrão da média e CV;"
    )
    exams_stats = midpoints_df_refined.iloc[:, 1:5].agg(
        ["mean", "median", "var", "std"]
    )
    exams_stats.loc["Moda"] = midpoints_df_refined.iloc[:, 1:5].mode().iloc[0]
    exams_stats1 = exams_stats.sem(axis=1)
    exams_stats = exams_stats.rename(index=dict(zip(exams_stats.index, new_labels)))
    exams_stats_erro_padrao = exams_stats1.rename(
        index=dict(zip(exams_stats1.index, new_labels))
    )

    st.write(exams_stats)
    st.write("Erro padrão")
    st.write(exams_stats_erro_padrao)
    st.write("CV")
    st.write(
        exams_stats_erro_padrao["Desvio padrão"] / exams_stats_erro_padrao["Média"]
    )
