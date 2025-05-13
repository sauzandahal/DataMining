import pandas as pd

data = pd.read_csv("sampledata.csv")
data.fillna(data.mean(), inplace=True)

stats = data.describe()
print("Descriptive Statistics:")
print(stats)
