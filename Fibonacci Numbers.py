#!/usr/bin/env python
# coding: utf-8

# In[1]:


liste = [1,1]


while liste[-1] !=55:
    liste.append(liste[-1] + liste[-2])
print(liste)


# In[2]:


l=[1,1]

for i in range(3,11) :
     eleman = l[-1] + l[-2]
     l.append(eleman)
print(l)


# In[ ]:




