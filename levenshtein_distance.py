# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 00:00:47 2024

@author: rikutotomita
"""

import jellyfish as jf
from docx import Document

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

doc1 = docRead('./w10-quiz-43.docx')
doc2 = docRead('./w10-quiz-79.docx')

D = jf.levenshtein_distance(doc1,doc2)

# print(f"D:{D/(len(doc1)+len(doc2)):.3f}")
print(f"ファイル1の文字数は{len(doc1)}です")
print(f"ファイル2の文字数は{len(doc2)}です")
print(f"レーベンシュタイン距離による類似度は{D/(0.5*(len(doc1)+len(doc2)))*100:.1f}%です")
print(D)
print(abs(len(doc2)-len(doc1)))