import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from questions.lista_1 import Questao1
from questions.lista_1 import Questao2
from questions.lista_1 import Questao3
from questions.lista_1 import Questao4


st.title("Lista 1")

navigation = ["Questão 1", "Questão 2", "Questão 3", "Questão 4"]
selection = st.sidebar.radio("Questões", navigation)
st.set_option("deprecation.showPyplotGlobalUse", False)

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
    nested_navigation_2 = ["Letra - A e B"]
    nested_selection_2 = st.sidebar.radio("Letras", nested_navigation_2)

    if nested_selection_2 == "Letra - A e B":
        Questao2.letter_A()

elif selection == "Questão 3":
    st.header(
        """Um artigo retirado da revista Technometrics (Vol. 19, 1977, p. 425) apresenta os seguintes dados sobre a taxa de octanagem de várias misturas de gasolina"""
    )
    nested_navigation_3 = ["Letra - B", "Letra - C", "Letra - D"]
    nested_selection_3 = st.sidebar.radio("Letras", nested_navigation_3)

    if nested_selection_3 == "Letra - B":
        Questao3.letter_B()
    if nested_selection_3 == "Letra - C":
        Questao3.letter_C()
    if nested_selection_3 == "Letra - D":
        Questao3.letter_D()

elif selection == "Questão 4":
    st.header(
        """O seguinte conjunto de dados representa as “vidas” de 40 baterias de carro da mesmamarca e mesmas características com aproximação até décimos do ano. As baterias tinham 	garantia para 3 anos."""
    )
    nested_navigation_4 = [
        "Letra - A",
        "Letra - B",
        "Letra - C",
        "Letra - D",
        "Letra - E",
        "Letra - F",
    ]
    nested_selection_4 = st.sidebar.radio("Letras", nested_navigation_4)

    if nested_selection_4 == "Letra - A":
        Questao4.letter_A()
    if nested_selection_4 == "Letra - B":
        Questao4.letter_B()
        pass
    if nested_selection_4 == "Letra - C":
        Questao4.letter_C()
        pass
    if nested_selection_4 == "Letra - D":
        Questao4.letter_D()
        pass
    if nested_selection_4 == "Letra - E":
        Questao4.letter_E()
        pass
    if nested_selection_4 == "Letra - F":
        Questao4.letter_F()
        pass
