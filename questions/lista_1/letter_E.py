import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


def letter_E():
    st.subheader("Letra E")
    st.write(
        """Sorteado ao acaso um dos 25 funcionários, qual a probabilidade de que ele tenha
obtido grau A em Metodologia?"""
    )
    st.subheader("Resposta:")
    st.write(
        """
            28%, como visto no gráfico de pizza da letra D
            """
    )
