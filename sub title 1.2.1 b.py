import pandas as pd
import numpy as np

df=pd.read_excel('/content/ingredient_KF-denoised.xlsx')
fig, axs = plt.subplots(len(df.columns), figsize=(5,15))
fig.suptitle('(b)                The data frame curves')
cols=df.columns
for ax,col in zip(axs,cols):
        d1=df[col]
        ax.set_title(f'{d1.name}')
        ax.plot(d1)
        ax.legend()
        ax.set_xlabel(f'{d1.name}', size=12)
        ax.set_ylabel('Values')
