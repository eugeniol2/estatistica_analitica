import pandas as pd

Question9dataset = pd.read_csv("csv_local/Question9dataset.csv")
ruralDs = pd.read_csv("csv_local/AlugueisRural.csv")
urbanDs = pd.read_csv("csv_local/AlugueisUrban.csv")
cereaisDs = pd.read_csv("csv_local/cereais.csv")




def getQuestionOneDataset():
    return Question9dataset


def getQuestionTwoDataset():
    return urbanDs, ruralDs

def getCereaisDataset():
    return cereaisDs