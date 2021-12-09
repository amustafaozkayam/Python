#!/usr/bin/env python
# coding: utf-8

# In[2]:


satır1 = ["⬜","⬜","⬜","⬜","⬜"]
satır2 = ["⬜","⬜","⬜","⬜","⬜"]
satır3 = ["⬜","⬜","⬜","⬜","⬜"]
satır4 = ["⬜","⬜","⬜","⬜","⬜"]
satır5 = ["⬜","⬜","⬜","⬜","⬜"]

map = [satır1, satır2, satır3, satır4, satır5]
#print(f"{satır1}\n{satır2}\n{satır3}\n{satır4}\n{satır5}")
pozisyon = input("Gülen Suratı Nereye Koymak İstersin :")
yatay = int(pozisyon[0])
dikey = int(pozisyon[1])
map[dikey - 1][yatay - 1] = '😍'
print(f"{satır1}\n{satır2}\n{satır3}\n{satır4}\n{satır5}")


# In[ ]:




