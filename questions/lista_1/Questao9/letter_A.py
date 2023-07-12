import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import csv_local
import numpy as np
import seaborn as sns
import statistics

corretoraA = pd.DataFrame(
    {
        "Corretora A": [
            45,
            60,
            54,
            62,
            55,
            70,
            38,
            48,
            64,
            55,
            56,
            55,
            54,
            59,
            48,
            65,
            55,
            60,
        ]
    }
)
corretoraB = pd.DataFrame(
    {
        "Corretora B": [
            57,
            55,
            58,
            50,
            52,
            59,
            59,
            55,
            56,
            61,
            52,
            53,
            57,
            57,
            50,
            55,
            58,
            54,
            59,
            51,
            56,
        ]
    }
)

meanA = corretoraA["Corretora A"].mean()
medianA = statistics.median(corretoraA["Corretora A"])
modeA = statistics.mode(corretoraA["Corretora A"])
std_devA = statistics.stdev(corretoraA["Corretora A"])
intervalA = max(corretoraA["Corretora A"]) - min(corretoraA["Corretora A"])


meanB = corretoraB["Corretora B"].mean()
medianB = statistics.median(corretoraB["Corretora B"])
modeB = statistics.mode(corretoraB["Corretora B"])
std_devB = statistics.stdev(corretoraB["Corretora B"])
intervalB = max(corretoraB["Corretora B"]) - min(corretoraB["Corretora B"])

numeroAcoesB = len(corretoraB["Corretora B"])
numeroAcoesA = len(corretoraA["Corretora A"])


def tValue(mediaA, mediaB, numeroAcoesA, numeroAcoesB, varianciaA, varianciaB):
    s = (((numeroAcoesA - 1) * varianciaA) + ((numeroAcoesB - 1) * varianciaB)) / (
        numeroAcoesA + numeroAcoesB - 2
    )
    t = (mediaA - mediaB) / (s * (((1 / numeroAcoesA) + (1 / numeroAcoesB)) ** (1 / 2)))
    return t


def letter_A():
    st.subheader("Resposta")
    st.write(
        "O resultado abaixo representa um numero abaixo de 2, logo, são semelhantes"
    )
    st.write(tValue(meanA, meanB, numeroAcoesA, numeroAcoesB, std_devA, std_devB))
