#!/usr/bin/python3
import pandas as pd


df = pd.read_excel('100_Multichoice.xlsx')
def fdrec(df):
    drec = dict()
    ncols = df.values.shape[1]
    for line in df.values:
        d = drec
        for j, col in enumerate(line[:-1]):
            if not col in d.keys():
                if j != ncols-2:
                    d[col] = {}
                    d = d[col]
                else:
                    d[col] = line[-1]
            else:
                if j!= ncols-2:
                    d = d[col]
    return drec

obj = fdrec(df)
print(obj)
