#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # NumPy Exercises 
# 
# Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks, and then you'll be asked some more complicated questions.

# #### Import NumPy as np

# In[1]:


import numpy as np


# #### Create an array of 10 zeros 

# In[4]:


arr = np.zeros(10)
arr


# #### Create an array of 10 ones

# In[5]:


arr_ones = np.ones(10)
arr_ones


# #### Create an array of 10 fives

# In[6]:


arr_fives = np.ones(10)*5
arr_fives


# #### Create an array of the integers from 10 to 50

# In[7]:


arr = np.arange(10, 51)
arr


# #### Create an array of all the even integers from 10 to 50

# In[8]:


arr = np.arange(10, 51, 2)
arr


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[10]:


arr_3 = np.arange(0,9).reshape(3,3)
arr_3


# #### Create a 3x3 identity matrix

# In[11]:


arr_3Id = np.eye(3,3)
arr_3Id


# #### Use NumPy to generate a random number between 0 and 1

# In[14]:


np.random.rand(1)


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[16]:


np.random.randn(25) #randn for standard normal distribution


# #### Create the following matrix:

# In[18]:


np.arange(1,101).reshape(10,10) / 100


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[19]:


np.linspace(0,1,20)


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[23]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[39]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[25]:


mat[2:, 1:]


# In[29]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[26]:


mat[3,4]


# In[30]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[30]:


mat[0:3, 1].reshape(3,1)


# In[31]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[31]:


mat[4]


# In[32]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[32]:


mat[3:]


# ### Now do the following

# #### Get the sum of all the values in mat

# In[33]:


mat.sum()


# #### Get the standard deviation of the values in mat

# In[34]:


mat.std()


# #### Get the sum of all the columns in mat

# In[35]:


mat.sum(axis=0)


# # Great Job!
