#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# COVİD SORUSU ASSİNGMENT
age = input('Are you a cigarette addict older than 75 years old ? yes or on :') == 'yes'
chronic = input('Do you have a severe chronic disease? yes or no :') == 'yes'
immune = input('Is your immune system too weak? yes or no :') == 'yes'

if age or chronic or immune :
    print('You are in risky group ')
    
else :
    print ('You are not in risky group')

