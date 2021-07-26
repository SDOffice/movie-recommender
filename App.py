#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
import pickle
from sklearn.impute import SimpleImputer


# In[2]:


# Reading dataframe
df = pd.read_csv('netflix_titles.csv')

# Deserializing Training Model
with open('cosine_sim.pkl', 'rb') as handle:
    cosine_sim = pickle.load(handle)
    
with open('indices.pkl', 'rb') as handle:
    indices = pickle.load(handle)

# Generating Recommendation
class Recommender:    
    def get_recommendation(self, title):
        try:
            title = title.lower()
            row_index = indices[title]
            sim_scores = list(enumerate(cosine_sim[row_index]))
            sim_scores = sorted(sim_scores, key = lambda x: x[1], reverse = True)

            sim_scores = sim_scores[1:11]

            movie_indices = [i[0] for i in sim_scores]

            return df.iloc[movie_indices]
        except:
            return 'Movie/ Tv Show not found. Please try again.'


# In[3]:


movie = Recommender()


# In[9]:


# # Serializing
# with open('movie.pkl', 'wb') as handle:
#     pickle.dump(movie, handle, pickle.HIGHEST_PROTOCOL)


# In[ ]:





# In[ ]:




