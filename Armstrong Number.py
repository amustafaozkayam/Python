#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True :

    numbers = input('Enter a positive number :')
    value = len(numbers)
    total = 0
    
    if not numbers.isdigit():
        print('Wrong enterance, try again.')
    
    elif int(numbers) >=0 :
        for i in range(value):
            total = total + int(numbers[i]) ** value 
            
        if total == int(numbers) :
            print(numbers, 'is an Armstrong number')
            break
        
        else :
            print(numbers, 'is not an Armstrong number')
            break

