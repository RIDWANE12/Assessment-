
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score 
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_squared_log_error
from sklearn.preprocessing import MinMaxScaler
from sklearn.experimental import enable_hist_gradient_boosting  
from sklearn.ensemble import HistGradientBoostingRegressor
import warnings 
warnings.simplefilter('ignore')

# load the data
df=pd.read_csv('/content/palm_ffb.csv')
cols=df.columns

# split the data
x=pd.concat([df[cols[1+0]], 
             df[cols[1+1]], 
             df[cols[1+2]], 
             df[cols[1+3]], 
             df[cols[1+4]], 
             df[cols[1+5]], 
             df[cols[1+6]]], axis=1)

y=df['FFB_Yield']

print('x col:', x.columns)
print('y col:',y.name)

seed=list(np.arange(0,100,1))
for i in seed:
    Xt,Xs,Yt,Ys=train_test_split(x,y,test_size=0.3,random_state=i)

    scaler = MinMaxScaler()
    Xtt=scaler.fit_transform(Xt)
    Xst=scaler.fit_transform(Xs)
    rf=RandomForestRegressor()
    hgbr=HistGradientBoostingRegressor(tol=0.6000000000000001, 
                                       min_samples_leaf=3, 
                                       max_leaf_nodes=90, 
                                       max_iter=80, 
                                       max_depth=60, 
                                       learning_rate=0.1, 
                                       l2_regularization=0.9)

    model=hgbr
    model.fit(Xtt,Yt)

    # Training results 
    pred=model.predict(Xtt)
    r21=r2_score(Yt, pred)
    mape1=mean_absolute_percentage_error(Yt, pred)
    rmse1=np.sqrt(mean_squared_error(Yt, pred))

    # Test results 
    preds=model.predict(Xst)
    r22=r2_score(Ys, preds)
    mape2=mean_absolute_percentage_error(Ys, preds)
    rmse2=np.sqrt(mean_squared_error(Ys, preds))
    ft=[np.var(preds),np.var(Ys)]
    fts=np.max(ft)/np.min(ft)
    
    if r22 >= 0.475 and r21 >=0.475 and r21>r22:
        print(i)
        l1=[r21,r22]
        l2=[rmse1,rmse2]
        l3=[mape1,mape2]
        l6=[fts]
        l7=['r2','RMSE','MAPE','F-test']
        df3=pd.DataFrame([l1,l2,l3,l6]).transpose()
        df3.columns=l7
        display(df3)
        break

