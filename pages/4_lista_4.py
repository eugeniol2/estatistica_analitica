import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import statistics
from scipy.special import comb
from scipy import stats
import math

st.write("Lista 4")

def calculate_probability(n, p):
    # Calculando a probabilidade de 0, 1 e 2 tubos defeituosos
    probability_0_defective = comb(n, 0) * p**0 * (1 - p)**(n - 0)
    probability_1_defective = comb(n, 1) * p**1 * (1 - p)**(n - 1)
    probability_2_defective = comb(n, 2) * p**2 * (1 - p)**(n - 2)

    # Calculando a probabilidade de não mais do que 2 tubos defeituosos
    probability_no_more_than_2_defective = probability_0_defective + probability_1_defective + probability_2_defective

    return probability_no_more_than_2_defective

def probability_of_contamination(n, p):
    # Calculando a probabilidade de sucesso em todos os estágios
    probability_success_all_stages = p**n

    # Calculando a probabilidade de contaminação
    probability_contamination = 1 - probability_success_all_stages

    return probability_contamination

def poisson_std_deviation(mean):
    # Desvio padrão da distribuição de Poisson é igual à raiz quadrada do parâmetro λ (média)
    std_deviation = math.sqrt(mean)
    return std_deviation

def poisson_probability_at_least_two(mean):
    # Usando a função de distribuição acumulada da Poisson para calcular a probabilidade de 0 e 1 ocorrências
    probability_0_or_1 = math.exp(-mean) * (1 + mean)

    # Calculando a probabilidade de pelo menos duas ocorrências (1 - probabilidade de 0 e 1 ocorrências)
    probability_at_least_two = 1 - probability_0_or_1
    return probability_at_least_two

def poisson_probability(lambda_param, x):
    # Calculando a probabilidade usando a distribuição de Poisson
    probability = (math.exp(-lambda_param) * (lambda_param**x)) / math.factorial(x)
    return probability
  
def binomial_probability(n, p, k):
    # Calculando a probabilidade usando a distribuição binomial
    probability = math.comb(n, k) * (p**k) * ((1 - p)**(n - k))
    return probability

st.subheader(":blue[1) Um inspetor de qualidade extrai uma amostra de 10 tubos aleatoriamente de uma carga muito grande de tubos que se sabe que contém 20% de tubos defeituosos. Qual é a probabilidade de que não mais do que 2 dos tubos extraídos sejam defeituosos?]")

st.title("Probabilidade de tubos defeituosos")
    
# Entrada de dados pelo usuário
n = st.number_input("Número de tubos extraídos:", min_value=1, max_value=100, value=10, step=1)
p = st.slider("Porcentagem de defeituosos na carga:", min_value=0.0, max_value=100.0, value=20.0, step=1.0) / 100.0

# Conversão da porcentagem para a probabilidade (entre 0 e 1)
p = min(max(p, 0), 1)

# Cálculo da probabilidade
probability = calculate_probability(n, p)

# Exibindo o resultado
st.write(f"A probabilidade de não mais do que 2 tubos serem defeituosos na amostra é: {probability:.4f}")

st.subheader(":blue[2) Suponha que o processo de esterilização para um experimento biológico compreenda n estágios independentes, cada um com probabilidade p de sucesso. Se uma falha em qualquer dos estágios ocasiona contaminação, qual a probabilidade desta acontecer, considerando n =10 e p = 0,99?]")

st.title("Probabilidade de Contaminação em Processo de Esterilização")
    
# Entrada de dados pelo usuário
n = st.number_input("Número de estágios independentes:", min_value=1, max_value=100, value=10, step=1)
p = st.slider("Probabilidade de sucesso em cada estágio:", min_value=0.0, max_value=1.0, value=0.99, step=0.01)

# Cálculo da probabilidade de contaminação
probability_contamination = probability_of_contamination(n, p)

# Exibindo o resultado
st.write(f"A probabilidade de contaminação é: {probability_contamination:.4f}")

st.subheader(":blue[3) Um contador eletrônico de bactérias registra, em média, cinco bactérias por cm3 de um líquido. Admitindo-se que esta variável tenha distribuição de Poisson,]")
st.title("Cálculo de Desvio Padrão e Probabilidade de Bactérias")

# Entrada de dados pelo usuário
mean = st.number_input("Média de bactérias por cm³:", min_value=0.1, value=5.0, step=0.1)

# Cálculo do desvio padrão
std_deviation = poisson_std_deviation(mean)

# Cálculo da probabilidade de pelo menos duas bactérias ocorrerem em 1 cm³
probability_at_least_two = poisson_probability_at_least_two(mean)

# Exibindo os resultados
st.write(f"Desvio padrão do número de bactérias por cm³: {std_deviation:.2f}")
st.write(f"Probabilidade de pelo menos duas bactérias ocorrerem em 1 cm³: {probability_at_least_two:.4f}")

st.subheader(":blue[4) Suponha que o número de vezes que uma pessoa fica resfriada durante um ano tem distribuição de Poisson com parâmetro λ = 4. Um novo remédio para prevenir resfriados reduz este parâmetro para λ ́ = 2 para 75% das pessoas e não faz efeito em 25% restantes. Se uma pessoa tomou este remédio durante um ano e pegou resfriado 2 vezes, qual é a probabilidade de que o remédio funciona para esta pessoa?]")
st.title("Probabilidade de Eficácia do Remédio")

# Dados do problema
lambda_before = 4  # Parâmetro λ antes de tomar o remédio
lambda_after = 2   # Parâmetro λ depois de tomar o remédio
p_effect = 0.75    # Probabilidade de o remédio funcionar
p_no_effect = 0.25 # Probabilidade de o remédio não fazer efeito
x = 2              # Número de vezes que a pessoa pegou resfriado

# Cálculo das probabilidades
p_b_given_a = poisson_probability(lambda_after, x)
p_a = p_effect
p_b = p_effect * p_b_given_a + p_no_effect * poisson_probability(lambda_before, x)

# Aplicando o Teorema de Bayes para calcular P(A | B)
p_a_given_b = (p_b_given_a * p_a) / p_b

# Exibindo o resultado
st.write(f"A probabilidade de o remédio funcionar para esta pessoa é: {p_a_given_b:.4f}")

st.subheader(":blue[5) Suponha que a probabilidade de uma família ter um filho com cabelos loiros seja 1/4. Se houverem 6 crianças na família, qual é a probabilidade de que metade delas terem cabelos loiros?]")

st.title("Probabilidade de Metade das Crianças terem Cabelos Loiros")

# Dados do problema
n_children = 6   # Número de crianças na família
p_blond = 1/4    # Probabilidade de uma criança ter cabelos loiros

# Cálculo da probabilidade de metade das crianças terem cabelos loiros
half_children = n_children // 2
probability_half_blond = binomial_probability(n_children, p_blond, half_children)

# Exibindo o resultado
st.write(f"A probabilidade de metade das crianças terem cabelos loiros é: {probability_half_blond:.4f}")