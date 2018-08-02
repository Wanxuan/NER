import logging
import os
from gensim.models import word2vec
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',level=logging.INFO)
sentences = word2vec.LineSentence('/home/wanxuanl/corpusSegDone.txt')
model = word2vec.Word2Vec(sentences,hs=1,min_count=1,window=4,size=300)
model.train(sentences,total_examples=model.corpus_count,epochs=model.iter)
model.save('/home/wanxuanl/mymodel')
model.save_word2vec_format('home/wanxuanl/mymodel.txt,binary=False)
