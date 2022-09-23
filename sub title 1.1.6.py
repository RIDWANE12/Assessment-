import pandas as pd
import seaborn as sns 
df=pd.read_csv('/content/ingredient.csv')
cor=df.corr(method='spearman').round(2)
p1 = sns.heatmap(cor, annot=True)
p1
