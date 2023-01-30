#!/usr/bin/env python
# coding: utf-8

# In[12]:


# DataFrames pt3 Multi level index


# In[13]:


import numpy as np
import pandas as pd


# In[14]:


from numpy.random import randn


# In[15]:


np.random.seed(101)


# In[16]:


# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)


# In[17]:


outside


# In[18]:


inside


# In[19]:


hier_index


# In[20]:


df = pd.DataFrame(randn(6,2), hier_index, ['A', 'B'])


# In[21]:


df


# In[22]:


df.loc['G1']


# In[24]:


df.loc['G1'].loc[1]


# In[25]:


df.index.names


# In[26]:


df.index.names = ['Groups', 'Num']


# In[27]:


df


# In[29]:


df.loc['G2'].loc[2]['B']


# In[30]:


df.loc['G1']


# In[31]:


df.xs('G1')


# In[33]:


df.xs(1,level='Num') # ability to skip levels


# In[ ]:




