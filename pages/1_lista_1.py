import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

ds = pd.read_csv("Question9MBcsv - Página1.csv")


st.title("Lista 1")

navigation = ["Questão 1", "Questão 2"]
selection = st.sidebar.radio("Questões", navigation)


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

    st.write(ds)
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

    elif nested_selection_1 == "Letra - B":
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

    elif nested_selection_1 == "Letra - C":
        st.subheader("Letra C")
        st.write("""Construa o histograma para as notas da variável Redação.""")
        histogram()
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

    elif nested_selection_1 == "Letra - D":
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

    elif nested_selection_1 == "Letra - E":
        st.subheader("Letra E")
        st.write(
            """(a) Após observar atentamente cada variável, e com o intuito de resumi-las, como você
                    identificaria (qualitativa ordinal ou nominal e quantitativa discreta ou contínua) cada
                    uma das 9 variáveis listadas?"""
        )

    elif nested_selection_1 == "Letra - F":
        st.subheader("Letra F")
        st.write(
            """(a) Após observar atentamente cada variável, e com o intuito de resumi-las, como você
                    identificaria (qualitativa ordinal ou nominal e quantitativa discreta ou contínua) cada
                    uma das 9 variáveis listadas?"""
        )

    elif nested_selection_1 == "Letra - G":
        st.subheader("Letra G")
        st.write(
            """(a) Após observar atentamente cada variável, e com o intuito de resumi-las, como você
                    identificaria (qualitativa ordinal ou nominal e quantitativa discreta ou contínua) cada
                    uma das 9 variáveis listadas?"""
        )


elif selection == "Questão 2":
    st.header("Descrição da questão 2")
    nested_navigation_2 = ["Subpage 1", "Subpage 2"]
    nested_selection_2 = st.sidebar.radio("Nested Navigation", nested_navigation_2)

    if nested_selection_2 == "Subpage 1":
        st.subheader("Subpage 1")
