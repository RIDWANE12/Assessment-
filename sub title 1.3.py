import pandas as pd
from sklearn.cluster import KMeans

df=pd.read_excel('/content/ingredient_KF-denoised.xlsx')
print(df.shape)

kmeans = KMeans(n_clusters=4, init='k-means++', algorithm='auto',
                max_iter=300, n_init=10, random_state=00).fit(df)

print(kmeans.feature_names_in_)
kmeans.labels_

