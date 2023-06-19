import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import csv_local

ds = csv_local.getQuestionOneDataset()


def histogram():
    fig = px.histogram(
        ds["Redação"],
        x="Redação",
        text_auto=True,
        labels={"Redação": "Nota da redação"},
    )
    fig.update_layout(bargap=0.2)

    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)


def letter_C():
    st.subheader("Letra C")
    st.write("""Construa o histograma para as notas da variável Redação.""")
    histogramCode = """
        def histogram():
            fig = px.histogram(ds["Redação"], x="Redação", text_auto=True, labels={"Redação": "Nota da redação"})
            fig.update_layout(bargap=0.2)
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit")
            with tab2:
                st.plotly_chart(fig, theme=None)
         """
    st.code(histogramCode, language="python")
    histogram()
