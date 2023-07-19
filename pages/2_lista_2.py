import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import csv_local
import numpy as np
import seaborn as sns
import statistics

st.title("Lista 2")
st.subheader("1) Três companhias A, B e C disputam a obtenção do contrato de fabricação. A chefia do departamento de vendas de A estima que sua companhia tem probabilidade igual à da companhia B de obter o contrato, mas que por sua vez é igual a duas vezes a probabilidade de C obter o mesmo contrato. Determine a probabilidade de A ou C obter o contrato.")
st.subheader("Resposta: ")

st.write("A compania A e B possuem a mesma chance, porém é duas vezes maior que a compania C")
st.write("Então, assumindo que A e B tenham 2 de chance de ganhar, e deve ser o dobro de c, logo:")
st.write("A e B = 4, C = 2")
st.write("Então, para A ou C ganhar, soma-se as probabilidades, que resulta: 6, ou 60%")

st.subheader("2) Um lote A contém 10 peças, sendo 4 defeituosas e 6 perfeitas; outro lote B possui 15 peças, sendo 5 defeituosas e 10 perfeitas. Uma peça é escolhida, aleatoriamente, de cada lote. Calcule a probabilidade de:")
st.subheader("Resposta: ")
st.subheader("a) pelo menos uma das peças escolhidas ser perfeita")
st.write("lote A possui 6/10 peças perfeitas, e o lote B 10/15 o que resulta: 60/150 = 6/15 = 3/5")
st.subheader("b) ambas as peças escolhidas serem defeituosas")
st.write("Lote A possui 4/10, lote B possui 5/15, portanto: 20/150 = 2/15")
st.subheader("c) uma peça escolhida ser perfeita e a outra defeituosa.")
st.write("Basta multiplicar 6/10 * 5/15 = 30/150 = 3/15 = 1/5")

st.subheader("3) Suponha que temos dois lotes nas seguintes condições: O primeiro com 200 peças, onde 10 tem defeito de fabricação, e o segundo com 300 peças, onde 12 tem defeito de fabricação. Se uma peça for retirada de cada lote, qual é a probabilidade de que:")
st.subheader("Resposta: ")
st.write("lote 1 possui: 190/200 peças perfeitas | lote 2 possui: 288/300 peças perfeitas")
st.subheader("a) nenhuma delas tenha defeito de fabricação?")
st.write("Então: 190/200 * 288/300 = 0.912 ou 91,2% de chance de que nenhuma peça tenha defeito")
st.subheader("b) apenas a peça do primeiro lote tenha defeito de fabricação?")
st.write("Então: 10/200 * 288/300 = 0.048 ou 4,8%")


st.subheader("4) Numa cidade 20% dos carros são da marca K, 30% dos carros são táxis e 40% dos táxis são da marca K. Se um carro é escolhido, ao acaso, determinar a probabilidade de:")
st.write("Definiremos os seguintes valores P(B): 20% | P(A): 30% | P(B|A): 40%")
st.subheader("a) ser táxi e ser da marca K")
st.write("Se 30% dos carros são taxis e desses 30% apenas 40% são da marca K então: 0.40 * 0.30 = 0.12 ou 12%")
st.subheader("b) ser táxi e não ser da marca K")
st.write("Probabilidade de não ser da marca K = 80%")
st.write("Probabilidade de um carro ser taxi = 30%")
st.write("Então: 0.8 * 0.3 = 0.24 ou 24%")
st.write("Aplicando a formula da probabilidade condicional temos que:")
st.write("P(A e B) = probabilidade de ser táxi e ser da marca K, que foi 12%")
st.write("Negando A temos: P(-A e B) = P(B) - P(A e B) = 0.2 - 0.12 = 0.08")
st.write("aplicando P(- A e B) = P(-A e B)/p(B)")
st.write("Temos: p(-A e B) = 0.08/0.2 = 0.4 ou 40%")

st.subheader("d) não ser táxi e não ser da marca K")
st.write("A probabilidade de um carro não ser taxi é 70% e a probabilidade de não ser da marca K é 80%")
st.write("Temos: 0.7 * 0.8 = 0.56 ou 56%")

st.subheader("e) não ser táxi e ser da marca K.")
st.write("P(B)−P(A e B) temos: 0.2 - 0.12 = 0.08 ou 8%")