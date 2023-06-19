import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from questions.lista_1 import Questao1
from questions.lista_1 import Questao2


st.title("Lista 1")

navigation = ["Questão 1", "Questão 2"]
selection = st.sidebar.radio("Questões", navigation)

if selection == "Questão 1":
    st.header("[Livro-texto] Cap. 2: ex. 9 ")
    st.write(
        """A MB Indústria e Comércio, desejando melhorar o nível de seus funcionários em cargos
            de chefia, montou um curso experimental e indicou 25 funcionários para a primeira
            turma. Os dados referentes à seção a que pertencem, notas e graus obtidos no curso
            estão na tabela a seguir. Como havia dúvidas quanto à adoção de um único critério de
            avaliação, cada instrutor adotou seu próprio sistema de aferição. Usando dados daquela
            tabela, responda às questões:"""
    )

    st.write(Questao1.ds)
    nested_navigation_1 = [
        "Letra - A",
        "Letra - B",
        "Letra - C",
        "Letra - D",
        "Letra - E",
        "Letra - F",
        "Letra - G",
    ]
    nested_selection_1 = st.sidebar.radio("Letras", nested_navigation_1)

    row1_space1, row1_space2 = st.columns((2))

    if nested_selection_1 == "Letra - A":
        Questao1.letter_A()

    elif nested_selection_1 == "Letra - B":
        Questao1.letter_B()

    elif nested_selection_1 == "Letra - C":
        Questao1.letter_C()

    elif nested_selection_1 == "Letra - D":
        Questao1.letter_D()

    elif nested_selection_1 == "Letra - E":
        Questao1.letter_E()

    elif nested_selection_1 == "Letra - F":
        Questao1.letter_F()

    elif nested_selection_1 == "Letra - G":
        Questao1.letter_G()

elif selection == "Questão 2":
    st.header("""[Livro-texto] Cap. 2: ex. 11""")
    st.write(
        """Dispomos de uma relação de 200 aluguéis de imóveis urbanos e uma relação de 100
aluguéis rurais."""
    )
    nested_navigation_2 = ["Letra - A e B", "Letra - C"]
    nested_selection_2 = st.sidebar.radio("Letras", nested_navigation_2)

    if nested_selection_2 == "Letra - A e B":
        Questao2.letter_A()
