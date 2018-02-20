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
    return scoreAnalysis(file)
    
def scoreAnalysis(file):
    x_values=[], y_values=[]
    clean_text=[]
    score=0.0
    for x in file:
        if not x.isalpha() or len(x)==1 or x==x.upper():
            continue
        clean_text.append(x)
    for x in clean_text:
        for y in lexicon_file:
            lexicon_data=y.split(",")
            if x.lower()==lexicon_data[0]:
                score+=np.float32(lexicon_data[1])
    return score


print takeInScript("a101script.txt")
print takeInScript("bg101script.txt")

#print clean_text
            