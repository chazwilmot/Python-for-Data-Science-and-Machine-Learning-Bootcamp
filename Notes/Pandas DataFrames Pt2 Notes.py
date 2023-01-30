#!/usr/bin/env python
# coding: utf-8

# In[1]:


# DataFrames Pt2


# In[2]:


import numpy as np
import pandas as pd


# In[3]:


from numpy.random import randn


# In[4]:


np.random.seed(101)


# In[5]:


df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])


# In[6]:


df


# In[7]:


# Conditional Selection


# In[9]:


booldf = df > 0


# In[10]:


booldf


# In[11]:


df[booldf]


# In[13]:


df[df>0]


# In[14]:


df


# In[15]:


df['W']>0


# In[16]:


df[df['W']>0]


# In[18]:


df[df['Z']<0]


# In[19]:


resultdf = df[df['W']>0]


# In[20]:


resultdf


# In[21]:


resultdf['X']


# In[23]:


df[df['W']>0]['X']


# In[25]:


df[df['W']>0][['X', 'Y']] # one liners


# In[32]:


boolser = df['W']>0
result = df[boolser] # four liner
mycols = ['X', 'Y']
result[mycols]


# In[33]:


# Multiple Conditions


# In[34]:


df[df['W']>0]


# In[40]:


df[(df['W']>0) & (df['Y']>1)] # do not use keyword 'and', use & instead


# In[41]:


df[(df['W']>0) | (df['Y']>1)] # do not use keyword 'or', use | instead


# In[42]:


df


# In[43]:


df.reset_index() # wont occur inplace unless inplace = true


# In[44]:


newind = 'CA NY WY OR CO'.split()


# In[45]:


newind


# In[46]:


df['State'] = newind


# In[47]:


df


# In[49]:


df.set_index('State') # need inplace to change df


# In[50]:


df


# In[ ]:




