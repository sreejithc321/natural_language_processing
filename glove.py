#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import gensim
from tqdm import tqdm
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors
import os


# In[4]:


#embedding_url = 'http://nlp.stanford.edu/data/glove.6B.zip'
glove_input_file = 'glove.6B.300d.txt'
word2vec_output_file = 'glove.6B.300d.txt.word2vec'

if not os.path.exists(word2vec_output_file):
    glove2word2vec(glove_input_file, word2vec_output_file)
embed = KeyedVectors.load_word2vec_format(word2vec_output_file, binary=False)


# In[5]:


stop_words = ['for', 'a', 'or', 'in']
cuisine_refs = ["mexican", "thai", "british", "american", "italian"]


# In[7]:


def sim_found(sample_sentence):
    try:
        tokens = sample_sentence.split()
        tokens = [x.lower().strip() for x in tokens] 
        threshold = 10
        found = []
        for term in tokens:
            if term not in stop_words:
                if term in embed.vocab:
                    scores = []
                    for C in cuisine_refs:
                        scores.append(np.dot(embed[C], embed[term].T)) 
                        mean_score = np.mean(scores)
                    if mean_score > threshold:
                        found.append(term)
        return(found)
    except Exception as error:
        print(error)
        return found


# In[8]:


# Finding possible cuisine names from a given sentence using Glove
sample_sentence = "I’m looking for a cheap Indian or Chinese place in Indiranagar"
print(sim_found(sample_sentence))


# In[ ]:





# In[ ]:





# In[ ]:




