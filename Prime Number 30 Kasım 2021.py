#!/usr/bin/env python
# coding: utf-8

# In[10]:


prime = [2]
number = int(input(''))
for i in range(3,number+1) :
  for x in range(2,i) :
    if i % x == 0 :
      break
  else :
    prime.append(i)

print(prime)


# In[ ]:




