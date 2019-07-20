with open(r'F:\PAPERS\pri\clusters _1\onlyclusters2.txt',"r") as f:
    lines = f.read().splitlines()
se=set(lines)
#print(lines)
"""from collections import Counter

for doc in lines:
    tf = Counter()
    for word in doc.split():
        tf[word] +=1
    print (tf.items())
"""
data=list(se)
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
    
bloblist=[]
from nltk.corpus import stopwords
for d in data:
    bloblist.append(tb(d))
big=[]
f1=open(r"F:\PAPERS\pri\tfifd\cluster1_2.txt","w",encoding="UTF8")
for i, blob in enumerate(bloblist):
    f1.write("Top words in document {}".format(i + 1))
    f1.write("\n")
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words if word not in stopwords.words('english')}
    sumsq=0
    sc1={}
    for j in scores.values():
        v=j**2
        sumsq=sumsq+v
    squareroot=math.sqrt(sumsq)
    for (x,y) in scores.items():
        y=y/squareroot
        sc1[x]=y
    big.append([])    
        
    sorted_words = sorted(sc1.items(), key=lambda x: x[1], reverse=True)
   
    for word, score in sorted_words[:20]:
            if score> 0.2:
                f1.write("\tWord: {}, TF-IDF: {}\n".format(word, round(score, 5)))
                big[i].append(word)