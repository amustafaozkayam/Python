#!/usr/bin/env python
# coding: utf-8

# In[ ]:


sayaç=0
 
sayi= int(input('Bir Sayı Giriniz: '))
for i in range(2,sayi):
      if sayi %i==0:
            sayaç+=1
            break
        
if (sayi <=1) or (sayaç!=0):
      print(f'({sayi}), sayısı asal sayı değildir.')
 
elif sayaç == 0 :
      print(f'({sayi}), sayısı asal sayıdır.')

