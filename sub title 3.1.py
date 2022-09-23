import nltk
import nltk.corpus
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import nltk
nltk.download('punkt')

with open('/content/Text.txt') as f:
    lines = f.readlines()
    for line in lines: 
        # print the line index
        idx=lines.index(line)
        print(idx)
        # print the current line 
        print(lines[idx])
        token = word_tokenize(line)    
        fdist = FreqDist(token)
        # print the current line words count 
        key=fdist.keys()
        keyl=list(key)
        print(key)

        # print the current line words probability  
        val=fdist.values()
        print(list(val))
        tot=sum(val)
        p= [i/tot for i in list(val)]

        df1=pd.DataFrame([keyl,list(val), p ])
        df1.set_axis(['word', 'count','prob'], axis=0, inplace=True)
        display(df1.transpose().round(2))

