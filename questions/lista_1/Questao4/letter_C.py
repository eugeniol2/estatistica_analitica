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


def letter_C():
    st.subheader("Letra C")
    st.write("Calcule a média aritmética dos dados originais")
    st.write("Resposta")
    st.write("Media aritmética, encontra-se na linha mean")
    st.write(df.describe())
