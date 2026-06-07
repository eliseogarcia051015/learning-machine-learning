import kagglehub
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from importlib.metadata import version

#KAGGLE API KEY
folder_path = kagglehub.dataset_download("camnugent/california-housing-prices")
#print("Path to dataset files:", path)

data = pd.read_csv(f"{folder_path}/housing.csv")
print(data)