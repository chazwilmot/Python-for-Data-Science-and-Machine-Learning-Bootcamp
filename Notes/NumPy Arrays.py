#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_list = [1,2,3]


# In[2]:


import numpy as np


# In[5]:


arr = np.array(my_list)


# In[6]:


arr


# In[7]:


my_mat = [[1,2,3],[4,5,6],[7,8,9]]


# In[8]:


np.array(my_mat)


# In[11]:


np.arange(0, 11, 2)


# In[12]:


np.zeros(3)


# In[13]:


np.zeros((5,5))


# In[14]:


np.ones(4)


# In[15]:


np.ones((4,4))


# In[18]:


np.linspace(0,5,100)


# In[19]:


np.eye(4) # identity matrix


# In[21]:


np.random.rand(5)


# In[22]:


np.random.rand(5,5)


# In[25]:


np.random.randn(5,5)


# In[27]:


np.random.randint(1,100,10)


# In[28]:


arr = np.arange(25)


# In[29]:


arr


# In[30]:


ranarr = np.random.randint(0,50,10)


# In[31]:


ranarr


# In[34]:


arr.reshape(5,5)


# In[35]:


ranarr


# In[36]:


ranarr.max()


# In[37]:


ranarr.min()


# In[38]:


ranarr


# In[39]:


ranarr.argmax() # index of max val


# In[40]:


ranarr.argmin()


# In[42]:


arr = arr.reshape(5,5)


# In[43]:


arr.shape


# In[44]:


arr.dtype


# In[ ]:




