#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


arr_2d = np.array([[5,10,15], [20,25,30], [35,40,45]])


# In[3]:


arr_2d


# In[4]:


arr_2d[0][0]


# In[5]:


arr_2d[0]


# In[6]:


arr_2d[2][2]


# In[8]:


arr_2d[2,2]


# In[11]:


arr_2d[:2,1:]


# In[15]:


arr_2d[:3, 1:]


# In[16]:


arr_2d[1, 0:]


# In[17]:


# Conditional Selection


# In[18]:


arr = np.arange(1,11)


# In[19]:


arr


# In[21]:


bool_arr = arr > 5


# In[22]:


bool_arr


# In[23]:


arr[bool_arr]


# In[24]:


arr[arr > 5]


# In[27]:


arr[arr<=3]


# In[28]:


arr_2d = np.arange(50).reshape(5,10)


# In[29]:


arr_2d


# In[30]:


arr_2d[1:3, 3:5]


# In[ ]:




