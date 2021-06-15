import pandas as pd

data = pd.read_csv("DATA_CM.csv")
print(data.index)
print(data.loc[0])
print(data.loc[0,'Number'])
