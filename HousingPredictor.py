import kagglehub
from importlib.metadata import version

#KAGGLE API
path = kagglehub.dataset_download("camnugent/california-housing-prices")

print(version('kagglehub'))
print("Path to dataset files:", path)