# Imports
import pandas as pandas_lib
import numpy as numpy_lib
import matplotlib.pyplot as mat_lib
import seaborn as seaborn_lib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel


data = pandas_lib.read_csv(r'D:\Coding\Life\Data Files/clean_data.csv')
data['overview'] = data['overview'].fillna('')

tfv_object = TfidfVectorizer(min_df=3,max_features=None,ngram_range=(1,3),stop_words='english')
tfv_matrix = tfv_object.fit_transform(data['overview'])
x = tfv_matrix.toarray()

pandas_lib.DataFrame(x)

s_value = sigmoid_kernel(tfv_matrix , tfv_matrix)
index = data.index
title = data['original_title']

indices = pandas_lib.Series(data.index,index=data['original_title'])
sigma_scores = sorted(list(enumerate(list(s_value[indices['Avatar']]))),key=lambda x:x[1],reverse = True)

ind = [index[0] for index in sigma_scores[1:11]]

def recommend(title):
    iddc = indices[title]
    model_scores = list(enumerate(list(s_value[indices[iddc]])))
    model_scores = sorted(model_scores,key=lambda x:x[1],reverse=True)
    movie_indices = [index[0] for index in model_scores[1:11]]
    return data['original_title'].iloc[movie_indices]

# arr = recommend('WarGames',s_value)

# print(arr)
