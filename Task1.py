import nltk
nltk.download("stopwords")
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop=stopwords.words('english')
user_term=input('Enter a word ,please:')

doc1=open(r'C:\Users\East-Sound\Desktop\Second_Term\IR\Practical\Documents\doc1.txt','r',encoding='utf-8').read()
doc2=open(r'C:\Users\East-Sound\Desktop\Second_Term\IR\Practical\Documents\doc2.txt','r',encoding='utf-8').read()
doc3=open(r'C:\Users\East-Sound\Desktop\Second_Term\IR\Practical\Documents\doc3.txt','r',encoding='utf-8').read()
doc4=open(r'C:\Users\East-Sound\Desktop\Second_Term\IR\Practical\Documents\doc4.txt','r',encoding='utf-8').read()

documents=[doc1,doc2,doc3,doc4]
#Inverted index
l=[]
#stop words in the documents
filtered=[]
for document in documents:
    text=word_tokenize(document)
    for word in text:
        if word in stop:
            filtered.append(word)
        else:
            if word==user_term:
                l.append(documents.index(document)+1)
print("Inverted Index:",list(set(l)))
print("Filtered words:",filtered)     

    

   
        


