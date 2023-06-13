import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


def letter_B():
    st.subheader("Letra B")
    st.write(
        """Compare e indique as diferenças existentes entre as distribuições das variáveis Direito,
Política e Estatística."""
    )
    st.subheader("Resposta:")
    st.write(
        """
            A forma de variação é diferente, enquanto direito não possui variação, mas é dito que é uma nota então deve variar de 0 a 10,
            A política varia sempre de 0.5 em 0.5.
            E a estatística possui variação inteira, sempre de 1 em 1.
            Todas são quantitativas discretas, pois, seguindo a lógica de variação delas, possuem conjunto finito de valores.
            """
    )
