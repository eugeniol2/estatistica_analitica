import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


def letter_F():
    st.subheader("Letra F")
    st.write(
        """Se, em vez de um, sorteássemos dois, a probabilidade de que ambos tivessem tido A
            em Metodologia é maior ou menor do que a resposta dada em (e)?"""
    )
    st.subheader("Resposta:")
    st.write(
        """
            visto que a probabilidade de um funcionário é 28%, então, para dois casos cuja nota seja A, seria 28% vezes 28% =7.84%
            Portanto, a probabilidade é menor
            """
    )
