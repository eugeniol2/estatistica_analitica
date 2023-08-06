import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import statistics
from scipy.special import comb
from scipy import stats

def componentes_defeituosos_esperados(n, p):
    return n * p

def custo_reparo_esperado(componentes_defeituosos, custo_reparo_por_componente):
    return componentes_defeituosos * custo_reparo_por_componente
  
def lucro_esperado(probabilidade_compra, lucro_por_venda, probabilidade_sem_compra, custo_sem_compra):
    return (probabilidade_compra * lucro_por_venda) - (probabilidade_sem_compra * custo_sem_compra)

def valor_esperado(vp_lucro, probabilidade):
    return np.sum(vp_lucro * probabilidade)

def variancia(vp_lucro, probabilidade, valor_esperado):
    return np.sum(probabilidade * (vp_lucro - valor_esperado) ** 2)

st.subheader(":blue[1) A Companhia Beta comprou 80 componentes eletrônicos de um fornecedor que declara que somente 2 %  dos componentes que ele vende são defeituosos e que os componentes defeituosos são misturados  aleatoriamente com os componentes bons. Cada componente defeituoso custará a Beta US$ 250 em custos  de reparo. Se o fornecedor está certo, qual será o número esperado de componentes defeituosos? E qual  é o custo esperado de reparo?]")

st.title("Resposta:")
st.subheader("Companhia Beta - Calculadora de Componentes Defeituosos e Custo de Reparo Esperado")

n_componentes = st.number_input("Número de Componentes Comprados", value=80, min_value=1)
p_defeituosos = st.number_input("Probabilidade de um Componente Ser Defeituoso (em decimal)", value=0.02, min_value=0.0, max_value=1.0)
custo_reparo_por_componente = st.number_input("Custo de Reparo por Componente Defeituoso", value=250, min_value=0)

componentes_defeituosos = componentes_defeituosos_esperados(n_componentes, p_defeituosos)
custo_reparo = custo_reparo_esperado(componentes_defeituosos, custo_reparo_por_componente)

st.subheader("Resultados:")
st.write(f"Número Esperado de Componentes Defeituosos: {componentes_defeituosos:.2f}")
st.write(f"Custo de Reparo Esperado: R${custo_reparo:.2f}")


st.subheader(":blue[2) Um vendedor de carros oferece a todos os seus clientes potenciais uma corrida de 30 milhas no tipo de  carro que o cliente está interessado em comprar, mais um almoço ou jantar gratuitos. Todos estes custos  são cerca de US$ 50. Se o cliente não compra o carro, o vendedor perde US 50, mas se o cliente comprar  o carro, o lucro médio do vendedor é de cerca de US 500 (dos quais os custos da corrida e da refeição  devem ser deduzidos). No passado, 20 % dos clientes compraram o carro depois da corrida e da refeição  gratuita. Qual é o lucro esperado para o vendedor nessa situação? ]")
st.title("Resposta:")
st.subheader("Vendedor de Carros - Calculadora de Lucro Esperado")

probabilidade_compra = st.number_input("Probabilidade de um Cliente Comprar um Carro (em decimal)", value=0.2, min_value=0.0, max_value=1.0)
lucro_por_venda = st.number_input("Lucro por Venda de Carro", value=500, min_value=0)
probabilidade_sem_compra = 1 - probabilidade_compra
custo_sem_compra = st.number_input("Custo por Não Venda (se o cliente não comprar)", value=50, min_value=0)

lucro = lucro_esperado(probabilidade_compra, lucro_por_venda, probabilidade_sem_compra, custo_sem_compra)

st.subheader("Resultado:")
st.write(f"Lucro Esperado: R${lucro:.2f}")

st.subheader(":blue[3) O presidente da Martin Corporation está considerando duas alternativas de investimento X e Y. Se cada  uma das alternativas for levada adiante há 4 possibilidades de resultado. O valor presente líquido e sua  respectiva probabilidade de ocorrência são mostrados abaixo: ]")
st.title("Resposta:")
    # Investimento X
vp_lucro_x = np.array([20, 8, 10, 3])
probabilidade_x = np.array([0.2, 0.3, 0.4, 0.1])
valor_esperado_x = valor_esperado(vp_lucro_x, probabilidade_x)
variancia_x = variancia(vp_lucro_x, probabilidade_x, valor_esperado_x)

    # Investimento Y
vp_lucro_y = np.array([12, 9, 16, 11])
probabilidade_y = np.array([0.1, 0.3, 0.1, 0.5])
valor_esperado_y = valor_esperado(vp_lucro_y, probabilidade_y)
variancia_y = variancia(vp_lucro_y, probabilidade_y, valor_esperado_y)

st.subheader("Investimento X:")
st.write(f"Valor Esperado do VPL: {valor_esperado_x:.2f}")
st.write(f"Variância do VPL: {variancia_x:.2f}")

st.subheader("Investimento Y:")
st.write(f"Valor Esperado do VPL: {valor_esperado_y:.2f}")
st.write(f"Variância do VPL: {variancia_y:.2f}")


st.subheader("A oportunidade mais interessante é o investimento Y, pois tem um valor esperado de VPL ligeiramente maior do que o investimento X. Isso significa que, em média, o investimento Y tem maior potencial de lucro em comparação com o investimento X.")
