import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import csv_local
import numpy as np
import seaborn as sns


Question9dataset = pd.read_csv("csv_local/midpointsListOneQuestionFour.csv")


def letter_F():
    st.subheader("Letra F")
    st.write(
        "Obtenha a variância a partir da distribuição de frequência conforme feito para a média no item d."
    )
    st.write("Resposta")
    st.write(Question9dataset)
    st.write("Variância da frequencia")
    st.write(Question9dataset.var()["Frequencia"])
