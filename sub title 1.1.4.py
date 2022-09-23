import pandas as pd
import pandas as np 
df=pd.read_csv('/content/ingredient.csv')
print(df.isin([np.inf, -np.inf]).sum())

