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

st.write("Lista 5")

# Função para calcular a probabilidade usando a distribuição normal
def probabilidade_normal(x, media, desvio_padrao):
    z = (x - media) / desvio_padrao
    return stats.norm.sf(z)

# Função para calcular o intervalo de confiança simétrico
def intervalo_simetrico(media, desvio_padrao, percentil):
    z = stats.norm.ppf((1 + percentil) / 2)
    margem_erro = z * desvio_padrao
    return (media - margem_erro, media + margem_erro)
  
# Função para calcular a probabilidade usando a distribuição normal
def probabilidade_esgotada(producao, media, desvio_padrao):
    z = (producao - media) / desvio_padrao
    return stats.norm.sf(z)

def calcular_limites_de_peso(media, desvio_padrao):
    # Percentis correspondentes a cada classe
    percentis = [0.20, 0.75, 0.90, 1.00]

    limites = []
    for p in percentis:
        limite = norm.ppf(p, loc=media, scale=desvio_padrao)
        limites.append(limite)
    
    return limites

def calcular_preco_medio(media, desvio_padrao, limite_superior):
    prob_menor_igual = stats.norm.cdf(limite_superior, loc=media, scale=desvio_padrao)
    prob_maior_que = 1 - prob_menor_igual
    quantidade_anel_5 = int(prob_maior_que * 1000)  # 1000 anéis no exemplo
    quantidade_anel_10 = 1000 - quantidade_anel_5
    preco_medio = (quantidade_anel_5 * 5 + quantidade_anel_10 * 10) / 1000
    return quantidade_anel_5, quantidade_anel_10, preco_medio

# Configurações iniciais
media = 170
desvio_padrao = 5

st.subheader(":blue[17) As alturas de 10.000 alunos de um colégio têm distribuição aproximadamente normal, com média 170 cm e desvio padrão 5 cm.]")

# Problema (a)
st.header("(a) Qual o número esperado de alunos com altura superior a 165 cm?")
altura_limite = 165
prob_superior_165 = probabilidade_normal(altura_limite, media, desvio_padrao)
num_alunos_superior_165 = round(prob_superior_165 * 10000)
st.write(f"Número esperado de alunos com altura superior a 165 cm: {num_alunos_superior_165}")

# Problema (b)
st.header("(b) Qual o intervalo simétrico em torno da média que conterá 75% das alturas dos alunos?")
percentil_75 = 0.75
intervalo_confianca = intervalo_simetrico(media, desvio_padrao, percentil_75)
st.write(f"Intervalo simétrico que contém 75% das alturas dos alunos: {intervalo_confianca[0]} cm a {intervalo_confianca[1]} cm")

st.subheader(":blue[18)As vendas de determinado produto têm distribuição aproximadamente normal, com média 500 unidades e desvio padrão 50 unidades. Se a empresa decide fabricar 600 unidades no mês em estudo, qual é a probabilidade de que não possa atender a todos os pedidos desse mês, por estar com a produção esgotada?]")

# Configurações iniciais
media = 500
desvio_padrao = 50
# Input para a quantidade de produção
producao = st.number_input("Quantidade de Produção:", min_value=0, value=600)

# Calculando a probabilidade
prob_esgotada = probabilidade_esgotada(producao, media, desvio_padrao)
prob_esgotada_percent = prob_esgotada * 100

# Exibindo a probabilidade
st.write(f"A probabilidade de produção esgotada é de {prob_esgotada_percent:.2f}%")

st.subheader(":blue[34) O peso bruto de latas de conserva é uma v.a. normal, com média 1.000 g e desvio padrão 20 g.]")

# Configurações iniciais
media = 1000
desvio_padrao = 20

# Problema (a)
st.header("(a) Qual a probabilidade de uma lata pesar menos de 980 g?")
peso_a = 980
z_a = (peso_a - media) / desvio_padrao
prob_a = norm.cdf(z_a)
st.write(f"Probabilidade de uma lata pesar menos de 980 g: {prob_a:.4f}")

# Problema (b)
st.header("(b) Qual a probabilidade de uma lata pesar mais de 1.010 g?")
peso_b = 1010
z_b = (peso_b - media) / desvio_padrao
prob_b = norm.sf(z_b)
st.write(f"Probabilidade de uma lata pesar mais de 1010 g: {prob_b:.4f}")

st.subheader(":blue[35) A distribuição dos pesos de coelhos criados numa granja pode muito bem ser representada por uma distribuição normal, com média de 5 kg e desvio padrão de 0,8 kg. Um abatedouro comprará 5.000 coelhos e pretende classificá-los de acordo com o peso, do seguinte modo: 20% dos leves como pequenos, os 55% seguintes como médios, os 15% seguintes como grandes e os 10% mais pesados como extras. Quais os limites de peso para cada classe?]")

# Configuração do Streamlit
st.title("Cálculo de Limites de Peso para Classes de Coelhos")

# Parâmetros da distribuição normal
media = 5.0
desvio_padrao = 0.8

# Calcular os limites de peso para cada classe
limites = calcular_limites_de_peso(media, desvio_padrao)

# Exibir os limites de peso
st.write("Limites de Peso para Cada Classe:")
st.write(f"Pequenos (20%): Menos de {limites[0]:.2f} kg")
st.write(f"Médios (55%): {limites[0]:.2f} kg a {limites[1]:.2f} kg")
st.write(f"Grandes (15%): {limites[1]:.2f} kg a {limites[2]:.2f} kg")
st.write(f"Extras (10%): Mais de {limites[2]:.2f} kg")

# Plotar distribuição normal com os limites
x = np.linspace(media - 3 * desvio_padrao, media + 3 * desvio_padrao, 100)
y = norm.pdf(x, loc=media, scale=desvio_padrao)

fig, ax = plt.subplots()
ax.plot(x, y, label='Distribuição Normal')
ax.axvline(x=limites[0], color='r', linestyle='--', label='Limite Pequenos')
ax.axvline(x=limites[1], color='g', linestyle='--', label='Limite Médios')
ax.axvline(x=limites[2], color='b', linestyle='--', label='Limite Grandes')
ax.legend()

st.pyplot(fig)

st.subheader(":blue[37) O diâmetro de certo tipo de anel industrial é uma v.a. com distribuição normal, de média 0,10 cm e desvio padrão 0,02 cm. Se o diâmetro de um anel diferir da média em mais que 0,03 cm, ele é vendido por 5,00; caso contrário, é vendido por 10,00. Qual o preço médio de venda de cada anel?")

# Configuração do Streamlit
st.title("Exemplo executado com 1000 aneis exemplares")

# Parâmetros da distribuição normal
media = st.number_input("Média do Diâmetro (cm)", value=0.10, step=0.01)
desvio_padrao = st.number_input("Desvio Padrão do Diâmetro (cm)", value=0.02, step=0.01)
limite_superior = media + 0.03

# Calcular o preço médio de venda
quantidade_anel_5, quantidade_anel_10, preco_medio = calcular_preco_medio(media, desvio_padrao, limite_superior)

# Exibir resultados
st.write(f"Quantidade de anéis vendidos por $5,00: {quantidade_anel_5}")
st.write(f"Quantidade de anéis vendidos por $10,00: {quantidade_anel_10}")
st.write(f"Preço médio de venda de cada anel: ${preco_medio:.2f}")