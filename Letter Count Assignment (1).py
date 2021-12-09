#!/usr/bin/env python
# coding: utf-8

# In[4]:


sentence = input('Enter a Sentence :')
result = {}

for i in sentence :
    if i not in result :
        result[i] = 1
    else :
        result[i] += 1
print(result)


# In[ ]:




