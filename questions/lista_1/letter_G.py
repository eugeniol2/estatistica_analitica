import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import csv_local

ds = csv_local.getQuestionOneDataset()


def letter_G():
    st.subheader("Letra G")
    st.write(
        """Como é o aproveitamento dos funcionários na disciplina Estatística, segundo a seção
            a que eles pertencem?"""
    )
    mean_values = ds.groupby("Seção")["Redação"].mean().reset_index()
    mean_df = pd.DataFrame(
        {"Seção": mean_values["Seção"], "Média de notas": mean_values["Redação"]}
    )
    mean_df = mean_df.sort_values(by="Média de notas", ascending=False)
    boxPlot = px.box(ds, y="Redação", x="Seção", color="Seção")

    meanDataset = """
            boxPlot = px.box(ds, y="Redação", x="Seção", color="Seção")
            st.write(boxPlot)
            """
    st.title("Gráfico de caixas")
    st.code(meanDataset, language="python")
    st.write(boxPlot)
    meanDataset = """
            mean_values = ds.groupby("Seção")["Redação"].mean().reset_index()
            mean_df = pd.DataFrame({"Seção": mean_values["Seção"], "Média de notas": mean_values["Redação"]})
            mean_df = mean_df.sort_values(by="Média de notas", ascending=False)
            st.write(mean_df)
            """
    col1, col2 = st.columns(2)
    with col1:
        st.header("Tabela de médias")
        st.write(mean_df)
    with col2:
        st.header("Conclusão")
        st.write(
            "A partir dos graficos e tabelas mostradas, é possível perceber que a maior média de notas foi da Seção T"
        )
    st.code(meanDataset, language="python")
