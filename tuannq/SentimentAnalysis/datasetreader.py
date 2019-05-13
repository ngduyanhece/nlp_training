import pandas as pd


def readTrain():
    df = pd.read_csv('dataset/train.tsv', delimiter='\t')
    return df

def readTest():
    df = pd.read_csv('dataset/test.tsv', delimiter='\t')
    return df
