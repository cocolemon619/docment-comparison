# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:07:42 2024

@author: rikutotomita
"""

import jellyfish as jf
from docx import Document
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize
import numpy as np

# wordファイルの読み込みを関数化する
def docRead(path):
    document = Document(path)
    sample_text_list = []
    for i, p in enumerate(document.paragraphs):
        # デバッグプリント
        # print(i, p.text)
        sample_text_list.append(p.text)
    sample_text = "\n".join(sample_text_list)
    return sample_text

doc1 = docRead('./w10-quiz-1.docx')
doc2 = docRead('./w10-quiz-2.docx')

print("doc1:".format(doc1))
print("doc2:".format(doc2))
print(doc1)

# # 参考サイトから
# corpus = [
#     'This is the first document.',
#     'This document is the second document.',
#     'And this is the third one.',
#     'Is this the first document?'
# ]

corpus = [doc1,doc2]


# sklearnによる実装
tfidf = TfidfVectorizer()
x = tfidf.fit_transform(corpus)

df_tfidf = pd.DataFrame(x.toarray(), columns=tfidf.get_feature_names_out())
# print(df_tfidf)

# print(cosine_similarity(x))

cos_tf_idf = cosine_similarity(x)
# print(cos_tf_idf)


# 自作
wc = CountVectorizer()
x = wc.fit_transform(corpus)
wcX = np.array(x.toarray())
# print(wcX)

df_wcX = pd.DataFrame(wcX, columns=wc.get_feature_names_out())
# print(df_wcX)

smooth_idf = True
norm_idf = True

# term frequency:
N = wcX.shape[0]
tf = np.array([wcX[i, :] / np.sum(wcX, axis=1)[i] for i in range(N)])

# inverse documents frequency
df = np.count_nonzero(wcX, axis=0)
idf = np.log((1 + N) / (1 + df)) + 1  if smooth_idf else np.log( N / df )  

# normalize
tfidf = normalize(tf*idf) if norm_idf else tf*idf
tfidf = pd.DataFrame(tfidf, columns=wc.get_feature_names_out())

# print(tfidf)