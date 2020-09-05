#!/usr/bin/env python
# coding: utf-8

# ### for loops

# In[8]:


list1 = [2,5,8,9,6,6]
sum = 0
for i in list1:
        sum = sum + i
print("The sum is", sum)


# In[5]:


return_list = []
list6 = ["acb1", "abc2",["1cba", "2cba"]]
for i in list6:
    if type(i) == list:
        for j in i:
            return_list.append(j[::-1])
return_list


# In[9]:


return_list1 = []
list7 = ["acb1", "abc2",["2cba", "1cba"]]
for i in list7:
    if type(i) == list:
        for j in i[::-1]:
            return_list1.append(j[::-1])
return_list1


# In[1]:


sum1 = 0
for i in range(0,100):
    sum1 = sum1 + i
print(sum1)


# In[71]:


return_list = []
for i in range(30):
    if i%3==0:
        return_list.append(i)


# In[72]:


print(return_list)


# In[3]:


for i in "string":  # it will skip the i alphabet
    if i == "i":
        continue
    print(i)


# ### List Comprehension
# #### List comprehension provides as concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more if clauses. The expressions can be anything, meaning you we can put all kinds of objects in lists,

# In[73]:


[i for i in range(30) if i%3 == 0]


# In[74]:


# writing so many codes
squares = []
def shishir(list):
    for number in list:
        squares.append(number*number)
    return squares


# In[75]:


shishir([1,2,3,4,5])


# In[2]:


shishir = [2,4,6,8,3,7]


# In[77]:


[i*i for i in shishir] # list comprehension for squaring


# In[78]:


[i*i for i in shishir if i%2 == 0] # with if condition for even numbers


# In[79]:


[i for i in shishir if i%2 != 0]


# In[80]:


# Numbers which are divisible by 7 but not multiple of 5, between 2000 and 3200 (both included) in 
# single line with comma seperated

numbers = [str(i) for i in range(2000,3200) if i%7 == 0 and  i%5 != 0]
print(",".join(numbers))


# In[81]:


nl=[]
for x in range(2000, 3200):
	    if (x%7==0) and (x%5!=0):
	        nl.append(str(x))
print (','.join(nl))


# ### Lamda function
# #### Can be used to create a function with single expression

# In[82]:


addition = lambda a,b : a+b


# In[83]:


addition (3,4)


# In[84]:


mean = lambda list : sum(list)/len(list)


# In[85]:


mean(shishir)


# 
# ### Map function 

# In[86]:


def even_odd_check(num):
    if num%2 == 0:
        return "The number {} is even".format(num)
    else:
        return "The number {} is odd".format(num)


# In[87]:


even_odd_check(10)


# In[88]:


even_odd_check(3)


# In[89]:


#map function to check this over list


# In[90]:


map(even_odd_check, shishir)


# In[91]:


list(map(even_odd_check, shishir))


# In[92]:


# list comprehension practise


# In[93]:


lis1 = [20, 130, 450, 50, 98, 69, 43, 44, 1]


# In[94]:


[i+1 if i >= 45 else i+5 for i in lis1]


# In[95]:


fruits = ["orange", "orange", "orange","mango", "graps"]


# In[96]:


[i if i == "orange" else i +" to be replaced" for i in fruits]


# In[103]:


shishir


# In[101]:


list(map(lambda num:num%2==0,shishir))


# In[102]:


list(filter(lambda num:num%2==0,shishir))


# #### While loops

# In[108]:


i = 0
while i <= 10:
    i = i + 1
    print (i)
    


# In[9]:


i = 1
n = 9
while i <= 10:
    print(n , "*" , i , "=" , i*n)
    i = i + 1


# In[2]:


n = int(input("Enter value "))
sum = 1 
i = 1

while i <= n:
    sum = sum + i
    i = i+1
sum


# In[ ]:




