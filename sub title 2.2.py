
import pandas as pd
from sklearn.linear_model import LinearRegression
sys.modules['sklearn.externals.joblib'] = joblib
from mlxtend.feature_selection import SequentialFeatureSelector as SFS

df=pd.read_csv('/content/palm_ffb.csv')

X=df.iloc[:,1:-1]
y=df['FFB_Yield']

linr=LinearRegression()
sfs1 = SFS(linr, 
           k_features=7, 
           forward=True, 
           floating=False, 
           verbose=0,
           scoring='r2',
           cv=0)

sfs1 = sfs1.fit(X, y)
sfs1.subsets_

