import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


def letter_A():
    st.subheader("Letra A")
    st.write(
        """Após observar atentamente cada variável, e com o intuito de resumi-las, como você
                    identificaria (qualitativa ordinal ou nominal e quantitativa discreta ou contínua) cada
                    uma das 9 variáveis listadas?"""
    )
    variables = [
        "Seção",
        "Administr",
        "Direito",
        "Redação",
        "Estatíst",
        "Inglês",
        "Metodologia",
        "Política",
        "Economia",
    ]
    answer = [
        "Qualitativa nominal",
        "Quantitativa discreta",
        "Quantitativa discreta",
        "Quantitativa contínua",
        "Quantitativa discreta",
        "Qualitativa ordinal",
        "Qualitativa ordinal",
        "Quantitativa discreta",
        "Quantitativa contínua",
    ]
    st.subheader("Resposta:")
    answerTable = pd.DataFrame(
        {"Variáveis": variables, "Tipo de variável(resposta)": answer}
    )
    st.table(answerTable)
