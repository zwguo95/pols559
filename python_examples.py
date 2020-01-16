#!/usr/bin/env python
# coding: utf-8

# # Python examples
# ## Workflow 
# * Read files from the web or a desktop folder into a list or dictionary
# * Import, parse and pre-process those files for different objectives
# * Basic word frequencies
# * Save or pickle your results and retrieve them
# * Computer interrater reliability for the PAP labels example
# * Construct a confusion matrix using the PAP labels example

# In[ ]:


# Start by downloading basic packages and setting your working directory. Make sure that you are in the desired working directory (where you will retrieve and store files)
import sys
import os

print os.getcwd() # print the current working directory 
os.chdir('your new path') # set up a new path 


# # PART I: Basics of lists, dictionaries, methods, loops, functions
# * Python is case sensitive
# * Indenting is critical for loops and functions

# ## Quick look at Python

# In[3]:


3/2
3/2.0


# In[4]:


a='head'
print(a)


# In[5]:


print(a+'light')


# In[6]:


b = a[:-1]
print(b)
len(b)


# In[7]:


b=a+'light'+'s are on'
print(b)


# ## Tuples
# * Note the parentheses

# In[8]:


tupleExample=(12, "hungry", "men")
len(tupleExample)
print(tupleExample(1))  #Tuples are immutable! won't work


# ## Lists
# * Note the hard brackets, strings in quotes. A list is just what it sounds like - a vector of something that can be read, manipulated, whatever. They are mutable.

# In[10]:


listExample=[12, 'hungry', 'men']
len(listExample)
print(listExample[1:]) #Lists are mutable, will work


# In[ ]:


#deleting first element in list (to grab just one element, listExample.pop[0])

del listExample[0]
print listExample


# In[ ]:


#applying a method to a list (here insert 'yes' in location 0)

listExample.insert(0,'yes')
print listExample


# In[ ]:


#adding a list to a list

listExample2=[47, listExample]
print(listExample2)


# In[ ]:


#to inspect the 2nd element of the second list within a list  

print listExample2[1][1]


# In[ ]:


#how about a list of lists (could be a list of tuples, whatever)

listOflists = [[1,2], [3,4]]

print listOflists[1][1]


# In[ ]:


#how about using a loop flattening a list of list into a single list

flatList=[]
for sublist in listOflists:
    for item in sublist:
        flatList.append(item)

print flatList


# In[ ]:


#use a loop to apply a method to a list 5 times (element is an #arbitrary variable name, could be i, j, whatever) 
 
myList=[]
for element in range(5):
    myList.append(element)    
print(myList)


# In[ ]:


#above append is a method or attribute of the 'list' object (or module)
#to view the directory of methods or attributes for an object or module, use:

dir(list)

#This error (below) indicates that you are trying to use a method that's not available for that object
#AttributeError: 'list' object has no attribute 'split'

#Available modules  https://docs.python.org/2/py-modindex.html
#Data structures (like list) https://docs.python.org/2/tutorial/datastructures.html


# ## Functions 
# * Commands that you create in advance and call (use the name of the function for efficiency)

# In[11]:


def happyBirthdayEmily(): #program does nothing as written
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear Emily.")
    print("Happy Birthday to you!")
    
happyBirthdayEmily() #running the function 


# In[ ]:


#some other examples where the function asks for inputs (you #could apply the function to a list of values for example)

def perfect( score ):
    print ("I got a perfect " + score)
    
perfect(score='100') 


# In[ ]:


def myfunction():
    for i in myList:
        if i > 3:
            print i

myfunction()


# In[ ]:


def pinfo( name, age ):
   print "Name: ", name
   print "Age ", age
   
pinfo( age=50, name="miki" )


# ## Dictionaries
# * Note the curly brackets. Each dictionary entry (case) has keys (variable name) and values. They are a way to organize data for easy extraction of selected information 

# In[ ]:


dictExample={'name':'john', 'age': 29, 'sex': 'M'}

#dictionaries are automatically sorted, so be sure to check that you are getting what you think you are getting

dictExample.keys()  #the first key in not 'name'
len(dictExample)
type(dictExample)
print(dictExample['age'])

listExample3=[dictExample] #can add to a list


# In[ ]:


#Creating a dictionary with keys and values for four different people. 

namelist=('jane', 'jon', 'joe', 'george')
agelist=(12,12,5,4)

myDict3={'name':[], 'age':[]}
for i in namelist: #i refers to an element of namelist
     myDict3['name'].append(i)
for j in agelist:  #j refers to an element of agelist     
        myDict3['age'].append(j)

print myDict3['name'][2]
print myDict3['age'][2]
print myDict3


# In[ ]:


#create a function to extract just the values from a dictionary and add them to a list
myValuelist=[]
for values in myDict3['name']:
    myValuelist.append(values)
    
print myValuelist[:]
print(myValuelist)
print(myValuelist[0])

#OK! Can you create your own function that loops through some data applying a method?


# ## Regular Expressions
# * A sequence of characters that define a search pattern. For example, '\,' says look for a comma. See https://docs.python.org/3.4/library/re.html

# In[ ]:


#split 'happy, go lucky wherever there is a comma, or whereever #there is a space

from bs4 import re
re.split('\,', 'happy, go lucky') 

re.split('\s', 'happy, go lucky') #split whereever there is a space  \s

#play with regular expressions here  http://www.regexr.com/


# In[ ]:


#Data are not always well behaved. The ignore and try/except commands can be used to say in effect:
#If it works do it, if not move on to the next case!
#Here's an example that is part of a function

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print "division by zero!"
    else:
        print "result is", result


divide(2.0,3.0)
divide(2.0, 0)


# In[ ]:


#If you just want to ignore bad cases (rather than printing an error message):

def divide(x, y):
    try:
        result = x / y
    except:
        pass
    else:
        print "result is", result

divide(2.0,3.0)
divide(2.0, 0)


# In[ ]:


#This script says convert the text to strings that are sentences in ascii format. 
#If a character can't be converted to ascii (e.g. some unicode characters), ignore it 

cleanwords=str(sentence.encode('ascii',errors='ignore'))


# In[ ]:


#Finally, here's a more deliberate way to remove unicode from a list of files.
#This worked when the above ignore command did not 

list2 = []
file_counter = 0
for file in list1:
	file_counter += 1
	missing_words = 0
	out_file = ''
	word_list = file.split()
	for word in word_list:
		try:
			new_word = str(word)
			out_file = '%s %s'%(out_file, new_word)
		except:
			missing_words += 1
	list2.append(out_file)
	print('%s%s%s%s'%('File: ', file_counter, '| Missing words: ', missing_words)) 


# # Part II: Scraping, parsing, and tokenizing data
# * Scraping data (using API, website or desktop)
# * Parsing documents
# * Tokenizing and cleaning a document
# * Tokenize and parse each of the files in fomclist by sentence

# In[16]:


# APIs for structured data

#Websites that have an API will also have instructions for how to use it. They are all unique

#WeatherUnderground API (https://www.wunderground.com/weather/api/d/docs)
#note that f below includes my registered key (5de2d6847556443d). 
#WU limits free calls, so it might not work if too many use it in one day! You could request your own key

import sys
import os
import urllib.request
import json
import pprint
#NYT API: Everything you need to scrape the NYT is here (also requires a key): 
#http://dlab.berkeley.edu/blog/scraping-new-york-times-articles-python-tutorial

#Twitter API https://dev.twitter.com/overview/api
#There are also specific python modules for working with Twitter


# ## Scraping a single website 

# In[37]:


import sys
import os
import urllib.request

opener = urllib.request.FancyURLopener({})
tempfile = opener.open("https://www.polisci.washington.edu/people")
polisci=tempfile.read()
open(polisci, 'w')
 
print(polisci)
type(polisci)  #it's a long string

plist=[polisci] #convert it to a list
print(plist)  #take a look at it now
type(plist)

#create a new list that split by words (at every \n or newline)
wlist=[polisci.split()] 
print(wlist)

#There are off the shelf tools such as downthemall, scrapy that are very useful for 
#scraping lots of pages


# In[ ]:





# In[ ]:




