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


def letter_C():
    # Letra c
    new_labels = ["Média", "Mediana", "Variância", "Desvio padrão"]
    st.subheader("Letra C")
    st.subheader(
        "c) Para o período: média, variância, desvio-padrão, erro-padrão da média, CV;"
    )
    full_period_with_values = full_period.iloc[:].agg(["mean", "median", "var", "std"])
    full_period_with_values.loc["Moda"] = full_period.iloc[:, 0].mode().iloc[0]
    full_period_with_values = full_period_with_values.rename(
        index=dict(zip(full_period_with_values.index, new_labels))
    )
    full_period_erro_padrao = full_period.sem()
    exams_stats_erro_padrao = full_period.rename(
        index=dict(zip(full_period.index, new_labels))
    )
    st.write(full_period_with_values)
    st.write("Erro padrão")
    st.write(full_period_erro_padrao)
    st.write("CV")
    st.write(2.6325 / 5.425)
