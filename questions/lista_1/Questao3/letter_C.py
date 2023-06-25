import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import csv_local
import numpy as np

# import utils
import seaborn as sns

taxaDeOctanagem = [
    88.5,
    87.7,
    83.4,
    86.7,
    87.5,
    91.5,
    88.6,
    100.3,
    96.5,
    93.3,
    94.7,
    91.1,
    91.0,
    94.2,
    87.8,
    89.9,
    88.3,
    87.6,
    84.3,
    86.7,
    84.3,
    86.7,
    88.2,
    90.8,
    88.3,
    98.8,
    94.2,
    92.7,
    93.2,
    91.0,
    90.1,
    93.4,
    88.5,
    90.1,
    89.2,
    88.3,
    85.3,
    87.9,
    88.6,
    90.9,
    89.0,
    96.1,
    93.3,
    91.8,
    92.3,
    90.4,
    90.1,
    93.0,
    88.7,
    89.9,
    89.8,
    89.6,
    87.4,
    88.4,
    88.9,
    91.2,
    89.3,
    94.4,
    92.7,
    91.8,
    91.6,
    90.4,
    91.1,
    92.6,
    89.8,
    90.6,
    91.1,
    90.4,
    89.3,
    89.7,
    90.3,
    91.6,
    90.5,
    93.7,
    92.7,
    92.2,
    92.2,
    91.2,
    91.0,
    92.2,
    90.0,
    90.7,
]

df = pd.DataFrame(taxaDeOctanagem, columns=["Octanagem"])


def letter_C():
    # frequency = utils.Frequency(df["Octanagem"])
    frequencyBeans = pd.cut(x=df["Octanagem"], bins=16).sort_index()
    st.write(frequencyBeans.value_counts().sort_index())
    sns.countplot(x=frequencyBeans.index, data=frequencyBeans)
    plt.xticks(rotation=45, ha="right")
    st.pyplot()
