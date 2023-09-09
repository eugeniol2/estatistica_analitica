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
import csv_local.datasets as csv_local

st.set_option('deprecation.showPyplotGlobalUse', False)
ds = csv_local.getCereaisDataset()


st.title("Correlação e Regressão")

st.title("Letra A")
st.subheader("Dados cereais")
st.write(ds)

# Calcule a correlação entre Y e X1
correlacao_Y_X1 = ds['Y'].corr(ds['X1'])

# Calcule a correlação entre Y e X2
correlacao_Y_X2 = ds['Y'].corr(ds['X2'])

# Exiba os resultados
st.write(f"Correlação entre Y e X1: {correlacao_Y_X1}")

sns.regplot(x='Y', y='X1', data=ds, ci=None)
plt.title('Gráfico de Dispersão com Linha de Tendência')
plt.xlabel('Y')
plt.ylabel('X1')
st.pyplot()

st.write(f"Correlação entre Y e X2: {correlacao_Y_X2}")

sns.regplot(x='X2', y='Y', data=ds, ci=None)
plt.title('Gráfico de Dispersão com Linha de Tendência')
plt.xlabel('X2')
plt.ylabel('Y')
st.pyplot()

st.title('Letra B')

st.subheader("Represente a linha de tendência no gráfico para (Y e X1)")
sns.regplot(x='X1', y='Y', data=ds, ci=None)
plt.xlabel('X1')
plt.ylabel('Y')
st.pyplot()

# Determine the simple linear regression equation for X1 and Y
coeficiente_X1, intercepto_X1, _, _, _ = stats.linregress(ds['X1'], ds['Y'])
st.header('Determine a Equação de Regressão Linear Simples para X1 e Y')
st.write(f"Inclinação (Coeficiente) para X1: {coeficiente_X1}")
st.write(f"Intercepto para X1: {intercepto_X1}")

# Calculate the mean of Y and the predicted Y (Y hat) for X1
media_Y_X1 = np.mean(ds['Y'])
Y_previsto_X1 = intercepto_X1 + coeficiente_X1 * ds['X1']

# Calculate the residuals (Y - Y hat) for X1
residuos_X1 = ds['Y'] - Y_previsto_X1

# Calculate the standard error of the estimate (EPE) for X1
epe_X1 = np.sqrt(np.sum(residuos_X1 ** 2) / (len(ds) - 2))

# Display results for X1 and Y
st.header('Resultados para X1 e Y')
st.write(f"Média de Y: {media_Y_X1}")
st.write(f"Y Previsto para X1:")
st.write(Y_previsto_X1)
st.header('Resíduos para X1 e Y')
st.write(residuos_X1)
st.header('Erro Padrão de Estimativa para X1 e Y')
st.write(f"Erro Padrão de Estimativa para X1: {epe_X1}")

# Calculate total, explained, and unexplained variations for X1 and Y
st.header('Variações Total, Explicada e Não Explicada para X1 e Y')
variacao_total_X1 = np.sum((ds['Y'] - media_Y_X1) ** 2)
variacao_explicada_X1 = np.sum((Y_previsto_X1 - media_Y_X1) ** 2)
variacao_nao_explicada_X1 = np.sum(residuos_X1 ** 2)

# Display results for X1 and Y
st.write(f"Variação Total para X1: {variacao_total_X1}")
st.write(f"Variação Explicada para X1: {variacao_explicada_X1}")
st.write(f"Variação Não Explicada para X1: {variacao_nao_explicada_X1}")

# Calculate the coefficient of determination (R-squared) for X1 and Y
st.header('Coeficiente de Determinação para X1 e Y')
r_quadrado_X1 = variacao_explicada_X1 / variacao_total_X1
st.write(f"Coeficiente de Determinação para X1: {r_quadrado_X1}")

# Uncomment the code for "Letra C"
st.title("Letra C")

st.subheader("Represente a linha de tendência no gráfico para (Y e X2)")
sns.regplot(x='X2', y='Y', data=ds, ci=None)
plt.xlabel('X2')
plt.ylabel('Y')
st.pyplot()

# Determine the simple linear regression equation for X2 and Y
coeficiente_X2, intercepto_X2, _, _, _ = stats.linregress(ds['X2'], ds['Y'])
st.header('Determine a Equação de Regressão Linear Simples para X2 e Y')
st.write(f"Inclinação (Coeficiente) para X2: {coeficiente_X2}")
st.write(f"Intercepto para X2: {intercepto_X2}")

# Calculate the mean of Y and the predicted Y (Y hat) for X2
media_Y_X2 = np.mean(ds['Y'])
Y_previsto_X2 = intercepto_X2 + coeficiente_X2 * ds['X2']

# Calculate the residuals (Y - Y hat) for X2
residuos_X2 = ds['Y'] - Y_previsto_X2

# Calculate the standard error of the estimate (EPE) for X2
epe_X2 = np.sqrt(np.sum(residuos_X2 ** 2) / (len(ds) - 2))

# Display results for X2 and Y
st.header('Resultados para X2 e Y')
st.write(f"Média de Y: {media_Y_X2}")
st.write(f"Y Previsto para X2:")
st.write(Y_previsto_X2)
st.header('Resíduos para X2 e Y')
st.write(residuos_X2)
st.header('Erro Padrão de Estimativa para X2 e Y')
st.write(f"Erro Padrão de Estimativa para X2: {epe_X2}")

# Calculate total, explained, and unexplained variations for X2 and Y
st.header('Variações Total, Explicada e Não Explicada para X2 e Y')
variacao_total_X2 = np.sum((ds['Y'] - media_Y_X2) ** 2)
variacao_explicada_X2 = np.sum((Y_previsto_X2 - media_Y_X2) ** 2)
variacao_nao_explicada_X2 = np.sum(residuos_X2 ** 2)

# Display results for X2 and Y
st.write(f"Variação Total para X2: {variacao_total_X2}")
st.write(f"Variação Explicada para X2: {variacao_explicada_X2}")
st.write(f"Variação Não Explicada para X2: {variacao_nao_explicada_X2}")

# Calculate the coefficient of determination (R-squared) for X2 and Y
st.header('Coeficiente de Determinação para X2 e Y')
r_quadrado_X2 = variacao_explicada_X2 / variacao_total_X2
st.write(f"Coeficiente de Determinação para X2: {r_quadrado_X2}")

st.title("Letra D")

st.subheader("Das equações encontradas nas etapas B e C, qual é a melhor para predizer os valores de Y? Explique.")
# R² obtido na etapa B (X2 e Y)
st.write(f"R² para X2 e Y (LETRA C): {r_quadrado_X2}")

# R² obtido na etapa C (X1 e Y)
st.write(f"R² para X1 e Y (LETRA B): {r_quadrado_X1}")

st.write("De acordo com o que estudei, o modelo que estiver mais proximo de 1, no resultadodo coeficiente de determinação, melhor ele é, logo: a etapa C é mais interessante.")


# Ajuste um modelo de regressão linear múltipla com X1 e X2
from sklearn.linear_model import LinearRegression

X = ds[['X1', 'X2']]
y = ds['Y']

modelo_regressao_multipla = LinearRegression().fit(X, y)

# Coeficientes da regressão múltipla
coeficientes_multipla = modelo_regressao_multipla.coef_
intercepto_multipla = modelo_regressao_multipla.intercept_

st.title("Equação de Regressão Linear Múltipla:")
st.write(f"Y = {intercepto_multipla} + {coeficientes_multipla[0]} * X1 + {coeficientes_multipla[1]} * X2")

# Etapa 3: Calcule o coeficiente de determinação múltipla e o coeficiente de determinação ajustado
st.subheader("Letra D3: Coeficiente de Determinação Múltipla e Coeficiente de Determinação Ajustado")

# R² múltiplo para a regressão múltipla
r_quadrado_multipla = modelo_regressao_multipla.score(X, y)

# Número de observações (n)
n = len(ds)

# Número de variáveis independentes (p) no modelo
p = 2  # X1 e X2

# R² ajustado
r_quadrado_ajustado = 1 - ((1 - r_quadrado_multipla) * (n - 1) / (n - p - 1))

st.write(f"R² Múltipla: {r_quadrado_multipla}")
st.write(f"R² Ajustado: {r_quadrado_ajustado}")

st.write("Os valores de R² são baixos, indicando que as variáveis independentes X1 e X2 não explicam muito da variabilidade em Y")

# Etapa 4: Conclusão da comparação
st.subheader("Letra D4: Conclusão")

st.title("Observações")
st.write("Efeituei o treinamento de um modelo de regressão linear utilizando o SKLEARN")
st.code("""X = ds[['X1', 'X2']], y = ds['Y'], modelo_regressao_multipla = LinearRegression().fit(X, y)""", language='python')

st.write("Nisso foi possível extrair o coeficiente de determinação multipla")
st.code("""r_quadrado_multipla = modelo_regressao_multipla.score(X, y)""", language='python')
st.write("Pois de acordo com a documentação do sklearn o .score retorna o coeficiente, seja ele simples ou multiplo")

st.write("Por fim, apliquei a formula seguinte para obter o coeficiente ajustado")
st.code("""r_quadrado_ajustado = 1 - ((1 - r_quadrado_multipla) * (n - 1) / (n - p - 1))""", language='python')

