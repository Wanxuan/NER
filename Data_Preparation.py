# -*- coding: UTF-8 -*-
import jieba
import gensim
from gensim.models import word2vec

fileTrainRead = []
with open('/home/wanxuanl/corpus.txt') as fileTrainRaw:
    for line in fileTrainRaw:
        line = unicode(line, "utf8", errors="ignore")
        fileTrainRead.append(line)

# Word Tokenize
fileTrainSeg=[]
for i in range(len(fileTrainRead)):
    fileTrainSeg.append([' '.join(list(jieba.cut(fileTrainRead[i][9:-11],cut_all=False)))])
    if i % 50000 == 0 :
        print i

# 将jieba的断词产出存档
fileSegWordDonePath ='corpusSegDone.txt'
with open(fileSegWordDonePath,'wb') as fW:
    for i in range(len(fileTrainSeg)):
        fW.write(fileTrainSeg[i][0].encode('utf-8'))
        fW.write('\n')

# 检查jieba断词的结果
def PrintListChinese(list):
    for i in range(len(list)):
        print list[i],

PrintListChinese(fileTrainSeg[10])

# jieba分詞轉word2vec向量
# word2vec.word2vec('corpusSegDone.txt', 'corpusWord2Vec.bin', size=300,verbose=True)
