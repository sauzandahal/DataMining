import pandas as pd
from scipy.spatial.distance import euclidean

data = pd.read_csv("sampledata.csv")
data.fillna(data.mean(), inplace=True)

point1 = data.loc[0, ['Age', 'Income', 'Score']]
point2 = data.loc[1, ['Age', 'Income', 'Score']]

distance = euclidean(point1, point2)
print(f"Euclidean distance between point 1 and 2: {distance:.2f}")
