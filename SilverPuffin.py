# Spirit Animal User ID: SilverPuffin
# Date the file was last edited: Feb 22, 2018
# Challenge Number: 2.0
# Online Sources Used
# 1) https://stackoverflow.com/questions/22232906/list-all-file-name-of-a-directory-to-text-file
# 2) https://developers.google.com/edu/python/strings

#  Importing contents to be used in the project
from __future__ import division
import numpy as np
import matplotlib.pyplot as mplot
import re
import os

# Analysing Lexicon file to split the words and its emotional value and putting them into a
# dictionary named as Lexicon_dictionary
lexicon_file=open("sentiment_lex.csv","r")
lexicon_file=lexicon_file.read()
lexicon_file=lexicon_file.split("\n")
lexicon_file.pop()
lexicon_file.pop()
lexicon_dictionary={}
for data in lexicon_file:
    data=data.split(",")
    lexicon_dictionary[data[0]]=np.float32(data[1])
#<-------------------------------------------------------------------------------------->
# The function of mergeSeries is tokae in a String 'a' or 'b' from the user and then
# use the algorithm to search text files with specific starting charcater i.e. 'a' or 'b'
# anc concadinate its string as a whole in a variable main_string and call the function
# scoreAnalysis(main_string) for printing the graph.
def mergeSeries (series):
    main_string=""
    path="./"  
    dirList=os.listdir(path)
    for filename in dirList:
        if filename.startswith(series.lower()):
            file=open(filename,"r")
            data=file.read()
            main_string+=data
            file.close()
    scoreAnalysis(main_string,series)

#<-------------------------------------------------------------------------------------->    
# Analyses the string, checks its presence in lexicon_dictinary and gives the histogram
# chart based on the information provided...
def scoreAnalysis(huge_string,series_code):
    file=re.sub(r'\W+'," ",huge_string)
    file=file.split(" ")
    file=list(set(file))
    dictionary={"Neg": 0, "W.Neg": 0, "Neu": 0, "W.Pos": 0, "Pos": 0}
    clean_text=[]
    for x in file:
        if not x.isalpha() or len(x)==1 or x==x.upper():
            continue
        clean_text.append(x)
    for x in clean_text:
        if x in lexicon_dictionary:
            if -1.0<=lexicon_dictionary[x]<-0.6:
                    dictionary["Neg"]+=1
            elif -0.6<=lexicon_dictionary[x]<-0.2:
                    dictionary["W.Neg"]+=1
            elif -0.2<=lexicon_dictionary[x]<=0.2:
                    dictionary["Neu"]+=1
            elif 0.2<lexicon_dictionary[x]<=0.6:
                    dictionary["W.Pos"]+=1
            elif 0.6<=lexicon_dictionary[x]<=1.0:
                    dictionary["Pos"]+=1
    values=dictionary.values()
    keys=dictionary.keys()
    mplot.bar(range(0,len(values)),np.log10(values))
    mplot.xticks(range(0,len(keys)),keys)
    mplot.xlabel("Sentiment")
    mplot.ylabel("log Word Count")
    mplot.title("Sentiment Analysis for Series "+series_code)
    mplot.show()

#<--------------------------------------------------------------------------------------->
# Ask user to input a or b for series analysis    
mergeSeries(raw_input ("Enter the series name (a or b): "))

            