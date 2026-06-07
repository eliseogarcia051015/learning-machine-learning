import kagglehub
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

#KAGGLE API KEY
folder_path = kagglehub.dataset_download("camnugent/california-housing-prices")
data = pd.read_csv(f"{folder_path}/housing.csv")
#print(data)

x = data.drop('median_house_value', axis=1)
y = data['median_house_value']

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)
train_data = x_train.join(y_train)

plt.figure(figsize=(6,6))
#train_data.hist()
#plt.show()
sns.heatmap(train_data.corr(numeric_only=True), annot=True, cmap="YlGnBu")
plt.show()
