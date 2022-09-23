import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
from scipy import stats 

df=pd.read_excel('/content/ingredient_KF-denoised.xlsx')
fig, axs = plt.subplots(len(df.columns), figsize=(5,15))
fig.suptitle('(a)                The data frame anomaly')
cols=df.columns
for ax,col in zip(axs,cols):
        d1=df[col]
        x=np.linspace(d1.min(), d1.max(),d1.shape[0])
        y=stats.norm.pdf(x, np.mean(d1), np.std(d1))
        ax.plot(x,y, label='Normal Dist.', lw=3)
        ax.set_title(f'{d1.name}')
        ax.hist(d1,density=True,  bins=30, label='Actual Data')
        ax.legend()
        ax.set_xlabel('Values', size=12)
        ax.set_ylabel('Count')
