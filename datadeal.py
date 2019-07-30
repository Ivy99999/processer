import numpy as np
import pandas as pd
import jieba
from gensim.models import word2vec
from sklearn.model_selection import train_test_split


#读入数据

pos = pd.read_table('data/pos.csv',header=None,index_col=None)
neg = pd.read_table('data/neg.csv',header=None,index_col=None)
print(pos.head())