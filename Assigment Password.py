#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print('Forgot your password ?')
name = 'Joseph'

while True :
    veri = (input('Enter your name :')).title()
    
    if veri ==  name :
        print('Hello, Joseph! The password is : W@12')
    
    
    else :
        print(f'Hello {veri}, see you later')
    break

