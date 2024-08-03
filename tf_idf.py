# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:07:42 2024

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

