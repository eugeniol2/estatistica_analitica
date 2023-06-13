import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import csv_local

ds = csv_local.getQuestionOneDataset()


def letter_D():
    st.subheader("Letra D")
    st.write(
        """Construa a distribuição de freqüências da variável Metodologia e faça um gráfico
            para indicar essa distribuição."""
    )
    frequency = pd.crosstab(index=ds["Metodologia"], columns="Frequency")
    col1, col2 = st.columns(2)
    with col1:
        st.header("Distribuição de frequência")
        st.write(frequency)

    with col2:
        st.header("Gráfico de frequência")
        fig = px.pie(
            frequency,
            values="Frequency",
            names=frequency.index,
            title="Distribuição de Frequência",
        )
        fig.update_layout(width=400, height=440)
        st.plotly_chart(fig)

    st.title("Código do gráfico de pizza")
    frequencyCode = """
        frequency = pd.crosstab(index=ds["Metodologia"], columns="Frequency")
        st.header("Gráfico de frequência")
        fig = px.pie(frequency, values='Frequency', names=frequency.index, title='Distribuição de Frequência')
        fig.update_layout(width=400, height=440)
        st.plotly_chart(fig)
            """
    st.code(frequencyCode, language="python")
