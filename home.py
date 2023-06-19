import streamlit as st
import pandas as pd

# ds2021 = pd.read_csv(
#     "dadosCeça\contratos-2021.csv",
#     encoding="latin-1",
# )
# ds2022 = pd.read_csv(
#     "dadosCeça\contratos-2022.csv",
#     encoding="latin-1",
# )


st.set_page_config(
    page_title="Multipage App",
)

st.title("Estatística Aplicada à Análise de Dados")
st.write(
    "Este site contém soluções baseadas em código, mais específicamente utilizando a biblioteca Pandas e afins, resolvendo e demonstrando gráficos relevantes para cada questão."
)
st.write(
    "Ao lado esquerdo é possível navegar através de cada lista de exercicios e cada uma contém suas respectivas questões"
)

st.sidebar.success("Selecione uma das listas de exercicio acima")

st.markdown(f"#### Feito por: Eugênio Araújo e Claudiano Lima")

st.markdown(f"###### libraries: plotly, seaborn, pandas, numpy, matplotlib")

# st.write(ds2021.describe())
# st.write(ds2022.describe())

# ds_columns = [
#     "data_inicio_vigencia",
#     "data_final_vigencia",
#     "valor_contrato",
#     "ano_contrato",
#     "numero_contrato",
#     "documento_identificacao",
#     "ano_licitacao",
#     "numero_licitacao",
#     "objeto_contrato",
#     "razao_social",
# ]


# df_csv_concat = pd.concat([ds2021, ds2022], ignore_index=True)
# # df_csv_concat['codigo_unidade_gestora'] = df_csv_concat['codigo_unidade_gestora'].replace(',','')
# df_csv_concat[ds_columns].to_csv("contratos_2021_2022.csv")

# st.write(df_csv_concat[ds_columns])
