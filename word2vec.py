import logging
import os
from gensim.models import word2vec
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',level=logging.INFO)
sentences = word2vec.LineSentence('corpusSegDone.txt')
model = word2vec.Word2Vec(sentences,hs=1,min_count=1,window=4,size=300)
