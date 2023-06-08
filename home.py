import streamlit as st

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

st.markdown(f"#### Feito por: Eugênio Araújo")

st.markdown(f"###### libraries: plotly, seaborn, pandas, numpy")

# code = """def hello():
#         print("Hello, Streamlit!")"""
#         st.code(code, language="python")
