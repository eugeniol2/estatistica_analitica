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


def letter_A():
    st.write("aaa")
    st.subheader("Medidas descritivas Corretora A:")
    st.write("Média:", meanA)
    st.write("Mediana:", medianA)
    st.write("Moda:", modeA)
    st.write("Desvio Padrão:", std_devA)

    st.subheader("Medidas descritivas Corretora B:")
    st.write("Média:", meanB)
    st.write("Mediana:", medianB)
    st.write("Moda:", modeB)
    st.write("Desvio Padrão:", std_devB)

    st.subheader("Que tipo de informação revelam esses dados?")
    st.write(
        "A média de lucro entre as duas é bastante similar, porém a corretora B possui um desvio padrão menor, o que poderia significar investimentos de menor risco"
    )
