#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
print('****Taş, Kağıt, Makas Oyunu****')
kullanıcı = int(input("Hangisini seçiyosun? Taş için 0, Kağıt için 1, Makas için 2 \n"))


bilgisayar = random.randint(0,2)
print("Bilgisayarın Seçimi:")
print(bilgisayar)

if kullanıcı >= 3 or kullanıcı < 0: 
  print("Hatalı giriş yaptın, kaybettin") 
elif kullanıcı == 0 and bilgisayar == 2:
  print("Kazandın!")
elif bilgisayar == 0 and kullanıcı == 2:
  print("Kaybettin!")
elif bilgisayar > kullanıcı:
  print("Kaybettin!")
elif kullanıcı > bilgisayar:
  print("Kazandın!")
elif bilgisayar == kullanıcı:
  print("Berabere")


# In[ ]:




