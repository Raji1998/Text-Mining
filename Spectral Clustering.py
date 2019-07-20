from textblob import TextBlob as tb
import pickle
import sys
import nltk
from nltk.corpus import stopwords
import ssl
import os
import math

import csv
with open(r'D:\clusters\cluster47.csv', 'r') as f:
    reader = csv.reader(f)
    big = list(reader)
for i in range(len(big)):
    big[i]= list(filter(None,big[i])) # fastest
"""with open("simat.txt","rb")as f1:
    board=pickle.load(f1)"""
def jaccard(A,B):
    if(len(A.union(B))!=0):
       return len(A.intersection(B))/len(A.union(B))
    else:
       return 0
board=[]
for i in range(len(big)):
    board.append([])
    for j in range(len(big)):
        board[i].append(jaccard(set(big[i]),set(big[j])))
import networkx as nx
import sklearn.cluster as sc
import matplotlib.pyplot as plt
#import matplotlib.colors as mc
#color_list=mc.get_named_colors_mapping()
#colors=[]
#for k,v in color_list.items():
#    colors.append(v)
    
#colors=colors[:50]

newsfinal=[]
for eachnews in big:
    stringval=' '.join(eachnews)
    newsfinal.append(stringval)
    stringval=''
data=newsfinal
G=nx.Graph()
G.add_nodes_from(data)


for i in range(len(data)):
    for j in range(i+1,len(data)):
        if board[i][j]>0.0 and i!=j:
            G.add_edge(data[i],data[j],weight=board[i][j])
            
n=3
MP=nx.adjacency_matrix(G)
spec=sc.spectral_clustering(affinity=MP,n_clusters=n,eigen_solver='arpack')
cluster=[]



mylist=G.nodes()
node_dict={i:spec[i] for i in range(len(mylist))}
color_map=[]
print(node_dict)

clus=[]
for key,val in node_dict.items():
	clus.append(val)

length=[]
for i in range(n):
    length.append([])

for k in range(n):
    length[k]=0

	
for k in range(len(clus)):
    val=clus[k]
    length[val]=length[val]+1

lengthdic={}
for k in range(len(length)):
    lengthdic[k]=length[k]
import csv
with open(r'D:\clusters\size of cluster47.csv','w') as f:
    w = csv.writer(f)
    w.writerows(lengthdic.items())

cluster=[]
for i in range(n):
    cluster.append([])
for n,c in node_dict.items():
    cluster[c].append(big[n])

#with open(r"F:\PAPERS\pri\finalclusencoded.txt","wb")as f5:
    #pickle.dump(cluster,f5)
   
f2=open(r"D:\clusters\onlyclusters47.txt","w",encoding="UTF8")
for i in range(3):
    f2.write("cluster ")
    f2.write(str(i))
    f2.write("\t")
    f2.write(str(len(cluster[i])))
    f2.write("\n")
    for val in cluster[i]:
        f2.write(str(val))
        f2.write("\n")
f2.close()

