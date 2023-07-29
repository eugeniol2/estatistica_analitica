import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import csv_local
import numpy as np
import seaborn as sns
import statistics
from scipy.special import comb
from scipy import stats

def probabilidade_mesma_cor():
    # Número total de bolas na caixa após a primeira retirada
    total_bolas_apos_primeira_retirada = 8 + 3  # 5 bolas brancas + 3 bolas pretas + 3 bolas azuis

    # Número de bolas brancas, pretas e azuis após a primeira retirada
    bolas_brancas_apos_primeira_retirada = 5
    bolas_pretas_apos_primeira_retirada = 3
    bolas_azuis_apos_primeira_retirada = 3

    # Número de bolas a serem retiradas simultaneamente após a primeira retirada
    bolas_retiradas_apos_primeira_retirada = 2

    # Calcular o número total de combinações possíveis após a primeira retirada
    total_combinacoes_apos_primeira_retirada = comb(total_bolas_apos_primeira_retirada, bolas_retiradas_apos_primeira_retirada)

    # Calcular o número de combinações com duas bolas brancas após a primeira retirada
    combinacoes_brancas_apos_primeira_retirada = comb(bolas_brancas_apos_primeira_retirada, bolas_retiradas_apos_primeira_retirada)

    # Calcular o número de combinações com duas bolas pretas após a primeira retirada
    combinacoes_pretas_apos_primeira_retirada = comb(bolas_pretas_apos_primeira_retirada, bolas_retiradas_apos_primeira_retirada)

    # Calcular o número de combinações com duas bolas azuis após a primeira retirada
    combinacoes_azuis_apos_primeira_retirada = comb(bolas_azuis_apos_primeira_retirada, bolas_retiradas_apos_primeira_retirada)

    # Probabilidade de que as duas primeiras bolas sejam da mesma cor (branca ou preta)
    probabilidade_mesma_cor_apos_primeira_retirada = (combinacoes_brancas_apos_primeira_retirada + combinacoes_pretas_apos_primeira_retirada) / total_combinacoes_apos_primeira_retirada

    # Número total de bolas na caixa após a segunda retirada
    total_bolas_apos_segunda_retirada = total_bolas_apos_primeira_retirada + 2  # 2 novas bolas são retiradas da caixa

    # Número de bolas brancas, pretas e azuis após a segunda retirada
    bolas_brancas_apos_segunda_retirada = bolas_brancas_apos_primeira_retirada
    bolas_pretas_apos_segunda_retirada = bolas_pretas_apos_primeira_retirada
    bolas_azuis_apos_segunda_retirada = bolas_azuis_apos_primeira_retirada

    # Número de bolas a serem retiradas simultaneamente após a segunda retirada
    bolas_retiradas_apos_segunda_retirada = 2

    # Calcular o número total de combinações possíveis após a segunda retirada
    total_combinacoes_apos_segunda_retirada = comb(total_bolas_apos_segunda_retirada, bolas_retiradas_apos_segunda_retirada)

    # Calcular o número de combinações com duas bolas brancas após a segunda retirada
    combinacoes_brancas_apos_segunda_retirada = comb(bolas_brancas_apos_segunda_retirada, bolas_retiradas_apos_segunda_retirada)

    # Calcular o número de combinações com duas bolas pretas após a segunda retirada
    combinacoes_pretas_apos_segunda_retirada = comb(bolas_pretas_apos_segunda_retirada, bolas_retiradas_apos_segunda_retirada)

    # Calcular o número de combinações com duas bolas azuis após a segunda retirada
    combinacoes_azuis_apos_segunda_retirada = comb(bolas_azuis_apos_segunda_retirada, bolas_retiradas_apos_segunda_retirada)

    # Probabilidade de que as duas últimas bolas sejam da mesma cor (branca, preta ou azul)
    probabilidade_mesma_cor_apos_segunda_retirada = (combinacoes_brancas_apos_segunda_retirada + combinacoes_pretas_apos_segunda_retirada + combinacoes_azuis_apos_segunda_retirada) / total_combinacoes_apos_segunda_retirada

    return probabilidade_mesma_cor_apos_segunda_retirada

def probabilidade_de_ganhar_contratos():
    # Probabilidade de ganhar o contrato elétrico
    p_ganhar_eletrico = 1/2

    # Probabilidade de ganhar o contrato de encanamento, dado que ganhou o contrato elétrico
    p_ganhar_encanamento_dado_eletrico = 3/4

    # Probabilidade de ganhar o contrato de encanamento, dado que não ganhou o contrato elétrico
    p_ganhar_encanamento_dado_nao_eletrico = 1/3

    # a) Probabilidade de ganhar os dois contratos (elétrico e encanamento)
    p_ganhar_os_dois_contratos = p_ganhar_eletrico * p_ganhar_encanamento_dado_eletrico

    # b) Probabilidade de ganhar apenas um contrato (ou elétrico ou encanamento, mas não ambos)
    p_ganhar_apenas_um_contrato = p_ganhar_eletrico * (1 - p_ganhar_encanamento_dado_eletrico) + (1 - p_ganhar_eletrico) * p_ganhar_encanamento_dado_nao_eletrico

    # c) Probabilidade de não ganhar nenhum contrato (nem elétrico nem encanamento)
    p_nao_ganhar_nenhum_contrato = (1 - p_ganhar_eletrico) * (1 - p_ganhar_encanamento_dado_nao_eletrico)

    return p_ganhar_os_dois_contratos, p_ganhar_apenas_um_contrato, p_nao_ganhar_nenhum_contrato


st.title("Lista 2")
st.subheader(":blue[1) Três companhias A, B e C disputam a obtenção do contrato de fabricação. A chefia do departamento de vendas de A estima que sua companhia tem probabilidade igual à da companhia B de obter o contrato, mas que por sua vez é igual a duas vezes a probabilidade de C obter o mesmo contrato. Determine a probabilidade de A ou C obter o contrato.]")
st.subheader("Resposta: ")

st.write("A compania A e B possuem a mesma chance, porém é duas vezes maior que a compania C")
st.write("Então, assumindo que A e B tenham 2 de chance de ganhar, e deve ser o dobro de c, logo:")
st.write("A e B = 4, C = 2")
st.write("Então, para A ou C ganhar, soma-se as probabilidades, que resulta: 6, ou 60%")

st.subheader(":blue[2) Um lote A contém 10 peças, sendo 4 defeituosas e 6 perfeitas; outro lote B possui 15 peças, sendo 5 defeituosas e 10 perfeitas. Uma peça é escolhida, aleatoriamente, de cada lote. Calcule a probabilidade de:]")
st.subheader("Resposta: ")
st.subheader("a) pelo menos uma das peças escolhidas ser perfeita")
st.write("lote A possui 6/10 peças perfeitas, e o lote B 10/15 o que resulta: 60/150 = 6/15 = 3/5")
st.subheader("b) ambas as peças escolhidas serem defeituosas")
st.write("Lote A possui 4/10, lote B possui 5/15, portanto: 20/150 = 2/15")
st.subheader("c) uma peça escolhida ser perfeita e a outra defeituosa.")
st.write("Basta multiplicar 6/10 * 5/15 = 30/150 = 3/15 = 1/5")

st.subheader(":blue[3) Suponha que temos dois lotes nas seguintes condições: O primeiro com 200 peças, onde 10 tem defeito de fabricação, e o segundo com 300 peças, onde 12 tem defeito de fabricação. Se uma peça for retirada de cada lote, qual é a probabilidade de que:]")
st.subheader("Resposta: ")
st.write("lote 1 possui: 190/200 peças perfeitas | lote 2 possui: 288/300 peças perfeitas")
st.subheader("a) nenhuma delas tenha defeito de fabricação?")
st.write("Então: 190/200 * 288/300 = 0.912 ou 91,2% de chance de que nenhuma peça tenha defeito")
st.subheader("b) apenas a peça do primeiro lote tenha defeito de fabricação?")
st.write("Então: 10/200 * 288/300 = 0.048 ou 4,8%")


st.subheader(":blue[4) Numa cidade 20% dos carros são da marca K, 30% dos carros são táxis e 40% dos táxis são da marca K. Se um carro é escolhido, ao acaso, determinar a probabilidade de:]")
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

st.subheader(":blue[5)Em uma empresa a probabilidade de que uma nova política de mercado tenha sucesso (A) foi estimada em 0,6. A probabilidade de que a despesa para o desenvolvimento da estratégia seja mantida dentro dos limites do orçamento previsto (B) é de 0,5. Admitindo que ambos os eventos A e B sejam independentes, determine a probabilidade de que:]")
st.subheader("a) pelo menos um dos objetivos seja atingido")
st.write("P(A) = 0,6")
st.write("P(B) = 0,5")
st.write("Como os eventos são independentes temos que: P(A e B) = P(A)⋅P(B)")
st.write("P(A e B) = 0.6 * 0.5 = 0.3, essa é a probabilidade de que ambos ocorram, logo: P(A ou B) = P(A) + P(B) - P(A e B)")
st.write("concluindo: 0.6 + 0.5 - 0.3 = 0.8 ou 80% de chance que pelo menos um dos objetivos seja atingido.")
st.subheader("b) somente A seja atingido:")
st.write("P(A e não B) = P(A) - P(A e B) logo: 0.6 - 0.3 = 0.3, ou 30% chance de ser atingido")
st.subheader(":blue[6) Uma rede local de computadores é composta por um servidor e cinco clientes. Dos pedidos de um tipo de processamento cerca de 10% vem do cliente A, 15% do B, 15% do C, 40% do D e 20% do E. Caso o pedido não seja feito de forma adequada, o processamento apresentará erro. Usualmente ocorrem os seguintes percentuais de pedidos inadequados: 1% do cliente A, 2% do cliente B, 0,5% do cliente C, 2% do cliente D e 8% do cliente E.]")
st.subheader("a) Qual a probabilidade de o sistema apresentar erro?")
st.write("P(Erro) = 0,01 * 0,10 + 0,02 * 0,15 + 0,005 * 0,15 + 0,02 * 0,40 + 0,08 * 0,20")
st.write("P(Erro) = 0,001 + 0,003 + 0,00075 + 0,008 + 0,016")
st.write("P(Erro) = 0.02875 ou 2,875%")
st.subheader("b) Sabendo-se que o processo apresentou erro calcule a probabilidade de que o processo tenha sido pedido pelo cliente E.")
st.write("P(E|Erro) = (P(Erro|E) * P(E)) / P(Erro)")
st.write("P(E|Erro) = (0,08 * 0,20) / 0,02875")
st.write("P(E|Erro) = 0,016 / 0,02875")
st.write("P(E|Erro) ≈ 0,5565")
st.subheader(":blue[7) Uma caixa contém 5 bolas brancas e três bolas pretas. Duas bolas são retiradas simultaneamente ao acaso e substituídas por três bolas azuis. Em seguida duas novas bolas são retiradas da caixa. Calcule a probabilidade de que essas duas últimas bolas sejam da mesma cor.]")

probabilidade = probabilidade_mesma_cor()
st.write(f"A probabilidade de que as duas últimas bolas sejam da mesma cor é: {probabilidade:.4f}")

st.subheader(":blue[8) Um empreiteiro apresentou orçamentos separados para a execução da parte elétrica e da parte de encanamento de um edifício. Ele acha que a probabilidade de ganhar a concorrência da parte elétrica é de 1/2. Caso ele ganhe a parte elétrica, a chance de ganhar a parte de encanamento é de 3/4; caso contrário, essa probabilidade é de 1/3. Qual a probabilidade de ele:]")

p_ganhar_os_dois, p_ganhar_apenas_um, p_nao_ganhar_nenhum = probabilidade_de_ganhar_contratos()
st.write(f"a) ganhar os dois contratos? {p_ganhar_os_dois:.4f}")
st.write(f"b) ganhar apenas um? {p_ganhar_apenas_um:.4f}")
st.write(f"c) não ganhar nada? {p_nao_ganhar_nenhum:.4f}")


