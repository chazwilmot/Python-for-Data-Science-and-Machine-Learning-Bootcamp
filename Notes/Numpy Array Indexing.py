#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


arr = np.arange(0,11)


# In[3]:


arr


# In[4]:


arr[8]


# In[5]:


arr[1:5]


# In[7]:


arr[:6]


# In[8]:


arr[::-1]


# In[9]:


arr[0:5] = 100


# In[10]:


arr


# In[11]:


arr = np.arange(0,11)


# In[12]:


arr


# In[13]:


slice_of_arr = arr[0:6]


# In[14]:


slice_of_arr


# In[16]:


slice_of_arr[:] = 99


# In[17]:


slice_of_arr


# In[18]:


arr


# In[19]:


arr_copy = arr.copy()


# In[20]:


arr


# In[21]:


arr_copy


# In[22]:


arr_copy[:] = 100


# In[24]:


arr_copy


# In[25]:


arr


# In[ ]:




