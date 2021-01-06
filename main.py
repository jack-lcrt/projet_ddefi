# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 15:26:19 2021

@author: jacqu
"""

import pickle
import PyPDF2 as pdf
from nltk.tokenize import RegexpTokenizer
from nltk import Text
#input pdf
pdf_name='../Bilan d_entreprises/Airbus Annual Report 2019.pdf'


file = open(pdf_name,'rb')
pdf_reader = pdf.PdfFileReader(file)
tokenizer = RegexpTokenizer(r'\w+')


keyword='co'
page=[]
sol=[]
for i in range(pdf_reader.getNumPages()):
  raw=pdf_reader.getPage(i).extractText()
  token=tokenizer.tokenize(raw)
  text=Text(token)
  word=[w.lower() for w in text]
  while keyword in word:
    index=word.index(keyword)
    if word[index+1]=='2':
      page.append(i)
      sol.append(word[index-15:index+15])
    word.remove('co')
sentence=[]
for i in sol:
  sentence.append(' '.join(i))
  

LR=pickle.load(open('LR_CO2.sav', 'rb'))
Vectorizer=pickle.load(open('vector.pickel', 'rb'))
vec_sentence=Vectorizer.transform(sentence)

label=LR.predict(vec_sentence)
info=[sentence[i] for i in range(len(sentence)) if vec_sentence[i]>0]
print(info)
        

