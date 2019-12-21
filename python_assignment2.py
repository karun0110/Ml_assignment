#!/usr/bin/env python
# coding: utf-8

# In[2]:


def do_sum(x1, x2): 
    return x1 + x2

def my_reduce(func, seq):
    first = seq[0]
    for i in seq[1:]:
        first = func(first, i)
    return first

print(my_reduce(do_sum, [1, 2, 3, 4,5]))


# In[55]:


def myfilter(func, sequence):
    result = []
    for item in sequence:
        if func(item):
            result.append(item)
    return result
                          
def is_even(item):
    if item % 2 == 0:
        return True
    else:
        return False

f = myfilter(is_even, [1, 3, 10, 45, 6, 50])
print(f)


# In[7]:


word = "ACADGILD"
alphabet_list = [ alph for alph in word ]
print ("ACADGILD => " + str(alphabet_list))


# In[8]:


input_list = ['x','y','z']
result = [ item*num for item in input_list for num in range(1,5)  ]
print("['x','y','z'] => " +   str(result))


# In[9]:


input_list = [2,3,4]
result = [ [item+num] for item in input_list for num in range(0,3)]
print("[2,3,4] =>" +  str(result))


# In[10]:


input_list = [2,3,4,5]
result = [ [item+num for item in input_list] for num in range(0,4)  ]
print("[2,3,4,5] =>" +  str(result))


# In[11]:


input_list=[1,2,3]
result = [ (b,a) for a in input_list for b in input_list]
print("[1,2,3] =>" +  str(result))


# In[22]:


def LongestWord(sen): 
    
    wrd_array = list(sen.split(" "))
    
    letter_count = []
    
    for i in range(len(wrd_array)):
        letter_count.append(sum(c.isalpha() for c in wrd_array[i]))
        
    longest_loc = letter_count.index(max(letter_count))
    
    return wrd_array[longest_loc]

print (LongestWord("Python course for beginner") )


# In[56]:


class Triangle:
 def __init__(self, side1, side2, side3):
  self.side1 = side1
  self.side2 = side2
  self.side3 = side3

class AreaTriangle(Triangle):
     def __init__(self, side1, side2, side3):
        super(AreaTriangle, self).__init__(side1, side2, side3)
     def get_area(self):
                s = (self.side1 + self.side2 + self.side3)/2
                return (s*(s-self.side1)*(s-self.side2)*(s-self.side3))**0.5
instance = AreaTriangle(3,3,4)
print ("Area of triangle = " + str(instance.get_area()) )


# In[57]:


def filter_long_words(words, n):
    return [word for word in words if len(word) > n]

print (filter_long_words(['Python', 'Karun', 'Billava','Aravind','Ravi'], 5))


# In[46]:


def map_to_lengths_lists(words):
    return [len(word) for word in words]
print (map_to_lengths_lists(['Python', 'Karun', 'Billava','Aravind','Ravi']))


# In[ ]:





# In[ ]:




