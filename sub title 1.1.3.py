import pandas as pd
df=pd.read_csv('/content/ingredient.csv')
print(df.isna().sum())

