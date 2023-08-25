import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from matplotlib.colors import ListedColormap

bc_df = load_breast_cancer()
df = pd.DataFrame(bc_df.data, columns=bc_df.feature_names)
features = StandardScaler().fit_transform(df)
pca = PCA(n_components=2)
x_pca = pca.fit_transform(features)
cmap = ListedColormap(["black", "#9F9F9F"])
plt.scatter(x_pca[:, 0], x_pca[:, 1], c=bc_df.target, cmap=cmap)
plt.xlabel("First principle component")
plt.ylabel("Second principle component")
plt.show()
