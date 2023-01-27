#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# # Python Crash Course Exercises 
# 
# This is an optional exercise to test your understanding of Python Basics. If you find this extremely challenging, then you probably are not ready for the rest of this course yet and don't have enough programming experience to continue. I would suggest you take another course more geared towards complete beginners, such as [Complete Python Bootcamp](https://www.udemy.com/complete-python-bootcamp/?couponCode=PY20)

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 7 to the power of 4?**

# In[2]:


7**4


# ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **

# In[5]:


s = "Hi there Sam!"
s.split()


# In[3]:





# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[7]:


planet = "Earth"
diameter = 12742
print(f"The diameter of {planet} is {diameter} kilometers.")


# In[6]:





# ** Given this nested list, use indexing to grab the word "hello" **

# In[10]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[13]:


print(lst[3][1][2][0])


# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[14]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[15]:


print(d['k1'][3]['tricky'][3]['target'][3])


# ** What is the main difference between a tuple and a list? **

# In[23]:


# Tuple is immutable


# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

# In[25]:


def domainGet(a):
    for i in range(0, len(a)):
        if(a[i] == '@'):
            print(a[i+1::])


# In[26]:


domainGet('user@domain.com')


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[27]:


def findDog(a):
    if(a.find("dog", 0, len(a)) != -1):
        return True
    else:
        return False


# In[30]:


findDog('Is there a dog here?')


# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[43]:


def countDog(a):
    count = 0
    words = a.split()
    for i in range(0, len(words)):
        if(words[i] == 'dog'):
            count += 1
    
    return count


# In[44]:


countDog('This dog runs faster than the other dog dude!')


# ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']

# In[47]:


seq = ['soup','dog','salad','cat','great']


# In[51]:


words = filter(lambda word : word[0] == 's', seq)
print(list(words))


# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

# In[56]:


def caught_speeding(speed, is_birthday):
    if(speed <= 60):
        return 'No Ticket'
    if(is_birthday == True):
        if(speed > 65 and speed < 86):
            return 'Small Ticket'
        else:
            return 'Big Ticket'
    if(speed > 60 and speed < 81):
        return 'Small Ticket'
    else:
        return 'Big Ticket'


# In[57]:


caught_speeding(81,True)


# In[58]:


caught_speeding(81,False)


# # Great job!
