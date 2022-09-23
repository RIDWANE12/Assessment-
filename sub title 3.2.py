import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import nltk
import nltk.corpus
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import nltk
nltk.download('punkt')

f = open('/content/Text.txt','r')
X=f.read()
token = word_tokenize(X)    
fdist = FreqDist(token)

keys=fdist.keys()

vals=fdist.values()
p= [i/len(keys) for i in list(vals)]
df1=pd.DataFrame([keys,list(vals), p ])
df1.set_axis(keys, axis=1, inplace=True)
df1.set_axis(['word', 'count','prob'], axis=0, inplace=True)
display(df1.transpose().round(2))
df1.to_excel('disnr.xlsx')

