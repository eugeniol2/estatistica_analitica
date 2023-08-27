import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import statistics
from scipy.special import comb
from scipy import stats
from scipy.stats import norm
import math

st.title("Intervalos de confiança")

st.subheader(":blue[18) Uma amostra aleatória de 625 donos de casa revela que 70% delas preferem a marca A de detergente. Construir um intervalo de confiança para p = proporção das donas de casa preferem A com c.c. y=90%]")

# Dados da amostra
amostra_tamanho = 625
proporcao_observada = 0.70

# Nível de confiança
confianca = 0.90
z_score = stats.norm.ppf((1 + confianca) / 2)

# Cálculo do intervalo de confiança
erro_padrao = np.sqrt((proporcao_observada * (1 - proporcao_observada)) / amostra_tamanho)
intervalo_inferior = proporcao_observada - z_score * erro_padrao
intervalo_superior = proporcao_observada + z_score * erro_padrao

# Exibição dos resultados
st.write(f"Amostra Tamanho: {amostra_tamanho}")
st.write(f"Proporção Observada: {proporcao_observada}")
st.write(f"Nível de Confiança: {confianca}")
st.write(f"Intervalo de Confiança: ({intervalo_inferior:.4f}, {intervalo_superior:.4f})")

# Título do aplicativo
st.subheader(":blue[20) Intervalo de Confiança para Proporção de Eleitores Favoráveis]")

# Dados da amostra
amostra_tamanho = 100
proporcao_observada = 0.60

# Nível de confiança
confianca = 0.95
z_score = stats.norm.ppf((1 + confianca) / 2)

# Cálculo do intervalo de confiança
erro_padrao = np.sqrt((proporcao_observada * (1 - proporcao_observada)) / amostra_tamanho)
intervalo_inferior = proporcao_observada - z_score * erro_padrao
intervalo_superior = proporcao_observada + z_score * erro_padrao

# Exibição dos resultados
st.write(f"Amostra Tamanho: {amostra_tamanho}")
st.write(f"Proporção Observada: {proporcao_observada}")
st.write(f"Nível de Confiança: {confianca}")
st.write(f"Intervalo de Confiança: ({intervalo_inferior:.4f}, {intervalo_superior:.4f})")

# Título do aplicativo
st.subheader(":blue[24) Um pesquisador está estudando a resistência de um determinado material sob determina-das condições. Ele sabe que essa variável é normalmente distribuída com desvio padrão de duas unidades.]")
st.subheader(":blue[(a) Utilizando os valores 4,9; 7,0; 8,1; 4,5; 5,6; 6,8; 7,2; 5,7; 6,2 unidades, obtidos de uma amostra de tamanho 9, determine o intervalo de confiança para a resistência média com um coeficiente de confiança γ = 0,90.]")
# Dados da amostra
valores = [4.9, 7.0, 8.1, 4.5, 5.6, 6.8, 7.2, 5.7, 6.2]
amostra_tamanho = len(valores)
media_amostra = np.mean(valores)
desvio_padrao_conhecido = 2

# Nível de confiança
confianca = 0.90
z_score = stats.norm.ppf((1 + confianca) / 2)

# Cálculo do intervalo de confiança
erro_padrao = desvio_padrao_conhecido / np.sqrt(amostra_tamanho)
intervalo_inferior = media_amostra - z_score * erro_padrao
intervalo_superior = media_amostra + z_score * erro_padrao

# Exibição dos resultados
st.write(f"Valores da Amostra: {valores}")
st.write(f"Tamanho da Amostra: {amostra_tamanho}")
st.write(f"Média da Amostra: {media_amostra}")
st.write(f"Nível de Confiança: {confianca}")
st.write(f"Intervalo de Confiança: ({intervalo_inferior:.4f}, {intervalo_superior:.4f})")


st.subheader(":blue[27) Numa pesquisa de mercado para estudar a preferência da população de uma cidade em relação a um determinado produto, colheu-se uma amostra aleatória de 300 indivíduos, dos quais 180 preferiam esse produto.]")
st.subheader(":blue[(a) (a) Determine um intervalo de confiança para a proporção da população que prefere o produto em estudo; tome γ = 0,90.]")

# Dados da amostra
amostra_tamanho = 300
preferem_produto = 180
proporcao_observada = preferem_produto / amostra_tamanho

# Nível de confiança
confianca = 0.90
z_score = stats.norm.ppf((1 + confianca) / 2)

# Cálculo do intervalo de confiança
erro_padrao = np.sqrt((proporcao_observada * (1 - proporcao_observada)) / amostra_tamanho)
intervalo_inferior = proporcao_observada - z_score * erro_padrao
intervalo_superior = proporcao_observada + z_score * erro_padrao

# Exibição dos resultados
st.write(f"Amostra Tamanho: {amostra_tamanho}")
st.write(f"Preferem o Produto na Amostra: {preferem_produto}")
st.write(f"Proporção Observada: {proporcao_observada}")
st.write(f"Nível de Confiança: {confianca}")
st.write(f"Intervalo de Confiança: ({intervalo_inferior:.4f}, {intervalo_superior:.4f})")