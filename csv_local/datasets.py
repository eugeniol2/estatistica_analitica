import pandas as pd

Question9dataset = pd.read_csv("csv_local/Question9dataset.csv")
ruralDs = pd.read_csv("csv_local/AlugueisRural.csv")
urbanDs = pd.read_csv("csv_local/AlugueisUrban.csv")


def getQuestionOneDataset():
    return Question9dataset


def getQuestionTwoDataset():
    return urbanDs, ruralDs
