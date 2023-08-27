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

def teste_de_hipotese(media_amostral, media_populacional, desvio_populacional, tamanho_amostra, alpha):
    # Calculando o Z-score
    z = (media_amostral - media_populacional) / (desvio_populacional / math.sqrt(tamanho_amostra))
    
    # Calculando o valor p (p-value) para um teste unilateral
    p_valor = stats.norm.cdf(z)
    
    # Comparando o valor p com o nível de significância (alpha) para tomar uma decisão
    if p_valor < alpha:
        decisao = "Rejeitar H0: Há evidência de melhoria"
    else:
        decisao = "Aceitar H0: Não há evidência de melhoria"
    
    return z, p_valor, decisao

st.title("Testes de hipótese")

st.subheader(":blue[7) A associação dos proprietários de indústrias metalúrgicas está muito preocupada com o tempo perdido com acidentes de trabalho, cuja média, nos últimos tempos, tem sido da ordem de 60 horas/homem por ano e desvio padrão de 20 horas/homem. Tentou-se um programa de prevenção de acidentes, após o qual foi tomada uma amostra de nove indústrias e medido o número de horas/homens perdidas por acidente, que foi de 50 horas. Você diria, no nível de 5%, que há evidência de melhoria?]")    
    
# Dados fornecidos
media_populacional = 60
desvio_populacional = 20
tamanho_amostra = 9
media_amostral = 50
alpha = 0.05
    
st.write(f"Média Populacional (μ): {media_populacional}")
st.write(f"Desvio Padrão Populacional (σ): {desvio_populacional}")
st.write(f"Tamanho da Amostra (n): {tamanho_amostra}")
st.write(f"Média Amostral (x̄): {media_amostral}")
st.write(f"Nível de Significância (α): {alpha}")
    
z, p_valor, resultado = teste_de_hipotese(media_amostral, media_populacional, desvio_populacional, tamanho_amostra, alpha)
valor_critico_z = stats.norm.ppf(alpha)

st.write(f"Valor Z: {z}")
st.write(f"Valor Crítico Z para um teste unilateral à esquerda: {valor_critico_z:.4f}")
st.write(f"Valor p: {p_valor}")
st.write("Resultado do Teste:")
st.write(resultado)


st.subheader(":blue[8) O salário médio dos empregados das indústrias siderúrgicas de um país é de 2,5 salários mínimos, com um desvio padrão de 0,5 salários mínimos. Uma indústria é escolhida ao acaso e desta é escolhida uma amostra de 49 empregados, resultando um salário médio de 2,3 salários mínimos. Podemos afirmar que esta indústria paga salários inferiores à média nacional, com o nível de 5%?]")
media_nacional = 2.5  # Média da população nacional
desvio_padrao = 0.5   # Desvio padrão da população
tamanho_amostra = 49  # Tamanho da amostra
nivel_significancia = 0.05

media_amostra = st.number_input("Média da Amostra:", min_value=0.0, value=2.3)

# Realiza o teste de hipótese
z = (media_amostra - media_nacional) / (desvio_padrao / np.sqrt(tamanho_amostra))
valor_critico = stats.norm.ppf(nivel_significancia)

# Exibe os resultados
st.write(f"Valor de Z calculado: {z}")
st.write(f"Valor Crítico: {valor_critico}")

if z < valor_critico:
    st.write("Conclusão: Rejeita a hipótese nula. A indústria paga salários inferiores à média nacional.")
else:
    st.write("Conclusão: Não rejeita a hipótese nula. Não há evidências para afirmar que a indústria paga salários inferiores à média nacional.")
st.subheader(":blue[9) Uma companhia de cigarros anuncia que o índice médio de nicotina dos cigarros que fabrica apresenta-se abaixo de 23 mg por cigarro. Um laboratório realiza 6 análises desse índice, obtendo: 27, 24, 21, 25, 26, 22. Sabe-se que o índice de nicotina se distribui normalmente, com variância igual a 4,86 mg2. Pode-se aceitar, no nível de 10%, a afirmação do fabricante?]")
# Inputs do usuário
media_populacional = 23  # Média populacional afirmada pelo fabricante
desvio_padrao_populacional = np.sqrt(4.86)  # Desvio padrão populacional
tamanho_amostra = 6  # Tamanho da amostra
nivel_significancia = 0.10  # Nível de significância (10%)

amostra = [27, 24, 21, 25, 26, 22]
media_amostra = st.number_input("Média da Amostra:", min_value=0.0, value=np.mean(amostra))

# Realiza o teste de hipótese
z = (media_amostra - media_populacional) / (desvio_padrao_populacional / np.sqrt(tamanho_amostra))
valor_critico = stats.norm.ppf(nivel_significancia)

# Exibe os resultados
st.write(f"Média da Amostra: {media_amostra}")
st.write(f"Valor de Z calculado: {z}")
st.write(f"Valor Crítico: {valor_critico}")

if z < valor_critico:
    st.write("Conclusão: Não rejeita a hipótese nula. Não há evidências para afirmar que o índice médio de nicotina dos cigarros está abaixo de 23 mg por cigarro.")
else:
    st.write("Conclusão: Rejeita a hipótese nula. Há evidências para afirmar que o índice médio de nicotina dos cigarros está abaixo de 23 mg por cigarro.")
st.subheader(":blue[11) O consumidor de um certo produto acusou o fabricante, dizendo que mais de 20% das unidades fabricadas apresentam defeito. Para confirmar sua acusação, ele usou uma amostra de tamanho 50, onde 27% das peças eram defeituosas. Mostre como o fabricante poderia refutar a acusação. Utilize um nível de significância de 10%.]")
# Introdução e explicação do teste
st.write("Nesta aplicação, você pode realizar um teste de hipótese para refutar a acusação do consumidor sobre a proporção de peças defeituosas.")

# Inputs do usuário
proporcao_alegada = 0.20  # Proporção alegada pelo consumidor (20%)
tamanho_amostra = 50  # Tamanho da amostra
proporcao_amostra = st.number_input("Proporção de Peças Defeituosas na Amostra (em decimal):", min_value=0.0, max_value=1.0, value=0.27)
nivel_significancia = 0.10  # Nível de significância (10%)

# Realiza o teste de hipótese
z = (proporcao_amostra - proporcao_alegada) / np.sqrt((proporcao_alegada * (1 - proporcao_alegada)) / tamanho_amostra)
valor_critico = stats.norm.ppf(1 - nivel_significancia)

# Exibe os resultados
st.write(f"Proporção de Peças Defeituosas na Amostra: {proporcao_amostra}")
st.write(f"Valor de Z calculado: {z}")
st.write(f"Valor Crítico: {valor_critico}")

if z > valor_critico:
    st.write("Conclusão: Rejeita a hipótese nula. Há evidências para sugerir que a proporção real de peças defeituosas é maior que 20%.")
else:
    st.write("Conclusão: Não rejeita a hipótese nula. Não há evidências para sugerir que a proporção real de peças defeituosas é maior que 20%.")
st.subheader(":blue[12) Um fabricante garante que 90% dos equipamentos que fornece a uma fábrica estão de acordo com as especificações exigidas. O exame de uma amostra de 200 peças desse equipamento revelou 25 defeituosas. Teste a afirmativa do fabricante, nos níveis de 5% e 1%.]")

# Inputs do usuário
proporcao_alegada = 0.90  # Proporção alegada pelo fabricante (90%)
tamanho_amostra = 200  # Tamanho da amostra
numero_defeituosos = 25  # Número de equipamentos defeituosos na amostra

nivel_significancia_5 = 0.05  # Nível de significância de 5%
nivel_significancia_1 = 0.01  # Nível de significância de 1%

# Calcular a proporção de equipamentos não defeituosos
proporcao_nao_defeituosos = 1 - (numero_defeituosos / tamanho_amostra)

# Realiza o teste de hipótese para o nível de 5%
z_5 = (proporcao_nao_defeituosos - proporcao_alegada) / np.sqrt((proporcao_alegada * (1 - proporcao_alegada)) / tamanho_amostra)
valor_critico_5 = stats.norm.ppf(nivel_significancia_5)

# Realiza o teste de hipótese para o nível de 1%
z_1 = (proporcao_nao_defeituosos - proporcao_alegada) / np.sqrt((proporcao_alegada * (1 - proporcao_alegada)) / tamanho_amostra)
valor_critico_1 = stats.norm.ppf(nivel_significancia_1)

# Exibe os resultados para o nível de 5%
st.write("Resultados para o nível de 5%:")
st.write(f"Proporção de Equipamentos Não Defeituosos na Amostra: {proporcao_nao_defeituosos}")
st.write(f"Valor de Z calculado: {z_5}")
st.write(f"Valor Crítico (5%): {valor_critico_5}")

if z_5 < valor_critico_5:
    st.write("Conclusão: Rejeita a hipótese nula. Há evidências para sugerir que a proporção real de equipamentos não defeituosos não é igual a 90% (nível de 5%).")
else:
    st.write("Conclusão: Não rejeita a hipótese nula. Não há evidências para sugerir que a proporção real de equipamentos não defeituosos não é igual a 90% (nível de 5%).")

# Exibe os resultados para o nível de 1%
st.write("Resultados para o nível de 1%:")
st.write(f"Valor de Z calculado: {z_1}")
st.write(f"Valor Crítico (1%): {valor_critico_1}")

if z_1 < valor_critico_1:
    st.write("Conclusão: Rejeita a hipótese nula. Há evidências fortes para sugerir que a proporção real de equipamentos não defeituosos não é igual a 90% (nível de 1%).")
else:
    st.write("Conclusão: Não rejeita a hipótese nula. Não há evidências para sugerir que a proporção real de equipamentos não defeituosos não é igual a 90% (nível de 1%).")