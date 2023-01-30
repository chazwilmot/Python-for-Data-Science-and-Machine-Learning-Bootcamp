#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Pandas built on top of NumPy


# In[2]:


# Series
# DataFrames
# Missing Data
# GroupBy
# Merging, Joining, Concatenating
# Operations
# Data Input and Output


# In[3]:


## Series ##


# In[4]:


import numpy as np 


# In[5]:


import pandas as pd


# In[7]:


labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a':10, 'b':20, 'c':30}


# In[9]:


pd.Series(data = my_data)


# In[10]:


pd.Series(data = my_data, index = labels)


# In[11]:


pd.Series(my_data, labels)


# In[13]:


pd.Series(arr, labels)


# In[16]:


pd.Series(d)


# In[18]:


pd.Series(labels)


# In[19]:


pd.Series(data=[sum, print, len])


# In[20]:


ser1 = pd.Series([1,2,3,4], ['USA', 'Germany', 'USSR', 'Japan'])


# In[21]:


ser1


# In[22]:


ser2 = pd.Series([1,2,5,4], ['USA', 'Germany', 'Italy', 'Japan'])


# In[23]:


ser2


# In[24]:


ser1['USA']


# In[25]:


ser3 = pd.Series(data=labels)


# In[26]:


ser3


# In[27]:


ser3[0]


# In[28]:


ser1


# In[29]:


ser2


# In[30]:


ser1 + ser2

