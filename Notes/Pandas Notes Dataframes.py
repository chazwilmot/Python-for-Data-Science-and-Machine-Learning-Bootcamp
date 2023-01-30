#!/usr/bin/env python
# coding: utf-8

# In[1]:


# DataFrames Pandas


# In[2]:


import numpy as np
import pandas as pd


# In[3]:


from numpy.random import randn


# In[4]:


np.random.seed(101)


# In[7]:


df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])


# In[8]:


df # Series' that share index


# In[9]:


df['W'] # given series


# In[10]:


type(df)


# In[11]:


df.W # df['W'] grab column name


# In[12]:


df[['W', 'Z']] # given dataframe


# In[14]:


df['new'] = df['W'] + df['Y']


# In[15]:


df


# In[19]:


df.drop('new', axis=1, inplace=True) # doesnt affect  df unless inplace = true


# In[20]:


df


# In[21]:


df.drop('E') #axis = 0 to drop row #axis = 1 to drop column


# In[22]:


df.shape


# In[23]:


# zero index equals rows
# one index equals columns


# In[24]:


df[['Z', 'X']]


# In[25]:


df.loc['A']


# In[26]:


df.loc[['A', 'E']]


# In[28]:


df.iloc[0]


# In[29]:


df.iloc[[0,4]]


# In[30]:


df.loc['B', 'Y']


# In[31]:


df.iloc[1, 2]


# In[33]:


df.loc[['A', 'B'], ['W', 'Y']]


# In[ ]:




