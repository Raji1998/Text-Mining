# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 12:50:34 2019

@author: RAJARAJESHWARI
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 22:59:44 2019

@author: RAJARAJESHWARI
"""

import nltk
import xlsxwriter
import xlrd
import sys
import math
import numpy
import scipy
from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))
workbook = xlsxwriter.Workbook(r'F:\\PAPERS\\excel.xlsx') 
worksheet = workbook.add_worksheet()
 

file=open(r'F:\\PAPERS\\data.txt','rt',encoding="utf8")
file2=open(r'F:\\PAPERS\\excel_processed.txt','wt',encoding="utf8")
f=file.readlines()

end='EOF'

for i in f:
    if i == '\n':
     print(end,file=file2)

    else:
     print(i,file=file2)
     
file.close()
file2.close()

print("111")

f2=open(r'F:\\PAPERS\\excel_processed.txt','rt',encoding="utf8")
f1=f2.read()
s=[]
tokens=nltk.word_tokenize(f1)
for i in tokens:
    if i.isalnum()==True and i not in stop_words:
     s.append(i)
     
data=list(s)

print("222")

from textblob import TextBlob as tb

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)
    """ sum1=0
    for blob in bloblist:
        if word in blob.words:
            sum1=sum1+1
    return sum1"""
    
def idf(word, bloblist):
    return math.log((len(bloblist) / (1 + n_containing(word, bloblist))+0.01))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

print("333")     

bloblist=[]

for d in data:
    bloblist.append(tb(d))
    
r=1
c=1

h=0

for i, blob in enumerate(bloblist):
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sumsq=0
    sc1={}
    for j in scores.values():
        v=j**2
        sumsq=sumsq+v
    squareroot=math.sqrt(sumsq)    
    for (x,y) in scores.items():
        y=y/squareroot
        sc1[x]=y 
    h=h+1 
    print(h)
    for word, score in sc1.items():
            if score> 0.2 and word not in ['EOF']:
                print("yes")
                worksheet.write(r,c,word)
                cc+1
            else
                r=r+1
                c=1

print("end")
workbook.close()



