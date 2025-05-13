import pandas as pd
from sklearn.preprocessing import MinMaxScaler


data = pd.read_csv("sampledata.csv")

data.fillna(data.mean(), inplace=True)

columns_to_normalize = ['Age', 'Income', 'Score']

scaler = MinMaxScaler()
data_normalized = data.copy()
data_normalized[columns_to_normalize] = scaler.fit_transform(data[columns_to_normalize])

print("Normalized Data:")
print(data_normalized)
