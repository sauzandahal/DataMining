import pandas as pd


data = pd.read_csv('sampledata.csv') 


print("Missing values in each column:")
print(data.isnull().sum())


data.fillna(data.mean(), inplace=True)


print("\nData after handling missing values:")
print(data)
