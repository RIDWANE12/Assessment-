import pandas as pd
import numpy as np 

df=pd.read_csv('/content/ingredient.csv')

def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return abs(20*np.log10(abs(np.where(sd == 0, 0, m**2/sd**2))))

snr=signaltonoise(np.array(df),0,0)

df4=pd.DataFrame(snr)
df4.set_axis(df.columns,axis=0,inplace=True)
df4.set_axis(['SNR'],axis=1,inplace=True)
df4


