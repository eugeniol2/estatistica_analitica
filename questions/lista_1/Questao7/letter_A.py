import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import csv_local
import numpy as np
import seaborn as sns
import statistics

dados = pd.DataFrame(
    {
        "Idade": ["18-20", "20-22", "22-26", "26-30", "30-36"],
        "Frequência": [18, 12, 10, 8, 2],
        "Porcentagem": [36, 24, 20, 16, 4],
    }
)


def letter_A():
    st.subheader("(a) Determine as medidas descritivas dos dados que você conhece.")
    st.subheader("Letra A")
    st.write("Baseando-se nos resultados, a campanha produziu algum efeito?")
    st.write(
        "A idade média antes da campanha era de 22 anos. Vamos comparar com a idade média após a campanha."
    )

    idade_media = sum(dados["Frequência"] * pd.Series([19, 21, 24, 28, 33])) / sum(
        dados["Frequência"]
    )

    if idade_media > 22:
        st.write("Média após a campanha: {}".format(idade_media))
        st.write("Não houve um grande aumento após a campanha")

    st.subheader("Letra B")
    st.write("Qual a conclusão baseada nos dados?")
    st.write(
        "O pesquisador decidiu usar a regra: se a diferença x - 22 fosse maior que o valor 2dp(X)/√n, então a campanha teria surtido efeito."
    )

    dp_X = pd.Series([19, 22, 24, 28, 33]).std()
    n = sum(dados["Frequência"])

    limite = 2 * dp_X / n ** (1 / 2)

    if (idade_media - 22) > limite:
        st.write("Conclusão: A campanha teve um efeito significativo.")
    else:
        st.write(limite)
        st.write("Conclusão: A campanha não teve um efeito significativo.")

    st.subheader("Letra C")
    st.write("Histograma da distribuição:")

    fig = px.bar(
        dados, x="Idade", y="Frequência", title="Histograma da Distribuição de Idade"
    )
    st.plotly_chart(fig, use_container_width=True)
