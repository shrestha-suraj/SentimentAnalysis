from __future__ import division
import numpy as np
import matplotlib.pyplot as mplot
import re

lexicon_file=open("sentiment_lex.csv","r")
lexicon_file=lexicon_file.read()
lexicon_file=lexicon_file.split("\n")



def takeInScript(file_name):
    file=open (file_name,"r")
    file=file.read()
    file=re.sub(r'\W+'," ",file)
    file=file.split(" ")
    file=list(set(file))
    scoreAnalysis(file)
    
def scoreAnalysis(file):
    dictionary={"Neg": 0.0, "W.Neg": 0.0, "Neu": 0.0, "W.Pos": 0.0, "Pos": 0.0}
    clean_text=[]
    for x in file:
        if not x.isalpha() or len(x)==1 or x==x.upper():
            continue
        clean_text.append(x)
    for x in clean_text:
        for y in lexicon_file:
            lexicon_data=y.split(",")
            if x.lower()==lexicon_data[0]:
                if -1.0<=np.float32(lexicon_data[1])<-0.6:
                    dictionary["Neg"]+=np.float32(lexicon_data[1])
                elif -0.6<=np.float32(lexicon_data[1])<-0.2:
                    dictionary["W.Neg"]+=np.float32(lexicon_data[1])
                elif -0.2<=np.float32(lexicon_data[1])<=0.2:
                    dictionary["Neu"]+=np.float32(lexicon_data[1])
                elif 0.2<np.float32(lexicon_data[1])<=0.6:
                    dictionary["W.Pos"]+=np.float32(lexicon_data[1])
                elif 0.6<=np.float32(lexicon_data[1])<=1.0:
                    dictionary["Pos"]+=np.float32(lexicon_data[1])
    values=dictionary.values()
    keys=dictionary.keys()
    mplot.bar(range(0,len(values)),np.log10(values))
    mplot.xticks(range(0,len(keys)),keys)
    mplot.xlabel("Word Range")
    mplot.ylabel("Number of words")
    mplot.show()
                
takeInScript("a101script.txt")
takeInScript("bg101script.txt")

#print clean_text
            