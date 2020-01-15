# -*- coding: utf-8 -*-
"""
Created on Sun Jan  16 08:44:06 2017

@author: John
"""

#read files from the web or a desktop folder into a list or dictionary
#import, parse and pre-process those files for different objectives
#basic word frequencies
#save or pickle your results and retrieve them
#computer interrater reliability for the PAP labels example)
#Construct a confusion matrix using the PAP labels example

#Many of these scripts came from searching google for examples! 

#-----------------------------------------------------

#Start by downloading basic packages and setting your working directory. Make sure that you 
#are in the desired working directory (where you will retrieve and store files)

import sys
import os

print os.getcwd()
%cd C:\Users\John.DESKTOP-ES1A8AS\Desktop\pols559\2018  
print os.getcwd() #be sure that it worked

------------------------------------------------------
#PART I
#Basics of lists, dictionaries, methods, loops, functions
#Python is case sensitive!!
#Indenting is critical for loops and functions!!


3/2
3/2.0  

a='head'
print(a)

print(a+'light')

b = a[:-1]
print(b)
len(b)

b=a+'light'+'s are on'
print(b)


#Tuples: Note the parentheses. 

tupleExample=(12, "hungry", "men")
len(tupleExample)
print(tupleExample(1))  #Tuples are immutable! won't work

#-------------------------------------------------------

#Lists: Note the hard brackets, strings in quotes. A list is #just what it sounds like - a vector of something that can be #read, manipulated, whatever. They are mutable.

listExample=[12, 'hungry', 'men']
len(listExample)
print(listExample[1:]) #Lists are mutable, will work

#deleting first element in list (to grab just one element, listExample.pop[0])

del listExample[0]
print listExample

#applying a method to a list (here insert 'yes' in location 0)

listExample.insert(0,'yes')
print listExample

#adding a list to a list

listExample2=[47, listExample]
print(listExample2)

#to inspect the 2nd element of the second list within a list  

print listExample2[1][1]

#how about a list of lists (could be a list of tuples, whatever)

listOflists = [[1,2], [3,4]]

print listOflists[1][1]

#how about using a loop flattening a list of list into a single list

flatList=[]
for sublist in listOflists:
    for item in sublist:
        flatList.append(item)

print flatList

#use a loop to apply a method to a list 5 times (element is an #arbitrary variable name, could be i, j, whatever) 
 
myList=[]
for element in range(5):
    myList.append(element)    
print(myList)

#above append is a method or attribute of the 'list' object (or module)
#to view the directory of methods or attributes for an object or module, use:

dir(list)

#This error (below) indicates that you are trying to use a method that's not available for that object
#AttributeError: 'list' object has no attribute 'split'

#Available modules  https://docs.python.org/2/py-modindex.html
#Data structures (like list) https://docs.python.org/2/tutorial/datastructures.html




#-----------------------------------------------------------

#functions are commands that you create in advance and call #using the name of the function for efficiency

def happyBirthdayEmily(): #program does nothing as written
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear Emily.")
    print("Happy Birthday to you!")
    
happyBirthdayEmily() #running the function 

#some other examples where the function asks for inputs (you #could apply the function to a list of values for example)

def perfect( score ):
    print ("I got a perfect " + score)
    
perfect(score='100') 

def myfunction():
    for i in myList:
        if i > 3:
            print i

myfunction()


def pinfo( name, age ):
   print "Name: ", name
   print "Age ", age
   
pinfo( age=50, name="miki" )

#-------------------------------------------------------

#Dictionaries: note the curly brackets! Each dictionary entry (case) has keys (variable name) and values. They are a way
#to organize data for easy extraction of selected information 

 
dictExample={'name':'john', 'age': 29, 'sex': 'M'}

#dictionaries are automatically sorted, so be sure to check that you are getting what you think you are getting

dictExample.keys()  #the first key in not 'name'
len(dictExample)
type(dictExample)
print(dictExample['age'])

listExample3=[dictExample] #can add to a list

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

#create a function to extract just the values from a dictionary and add them to a list
myValuelist=[]
for values in myDict3['name']:
    myValuelist.append(values)
    
print myValuelist[:]
print(myValuelist)
print(myValuelist[0])

#OK! Can you create your own function that loops through some data applying a method?

#---------------------------------------------------------

#Regular Expressions are a sequence of characters that define a #search pattern. 
#For example, '\,' says look for a comma. See https://docs.python.org/3.4/library/re.html

#split 'happy, go lucky wherever there is a comma, or whereever #there is a space

from bs4 import re
re.split('\,', 'happy, go lucky') 

re.split('\s', 'happy, go lucky') #split whereever there is a space  \s

#play with regular expressions here  http://www.regexr.com/

#-----------------------------------------------------------

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

#This script says convert the text to strings that are sentences in ascii format. 
#If a character can't be converted to ascii (e.g. some unicode characters), ignore it 

cleanwords=str(sentence.encode('ascii',errors='ignore'))

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

#-----------------------------------------------------------

#----------------------------------------------------------
#PART II
#Scraping data (using API, website or desktop)
#Parsing documents
#Tokenizing and cleaning a document
#Tokenize and parse each of the files in fomclist by sentence

#-----------------------------------------------------------------------------
# APIs for structured data

#Websites that have an API will also have instructions for how to use it. They are all unique

#WeatherUnderground API (https://www.wunderground.com/weather/api/d/docs)
#note that f below includes my registered key (5de2d6847556443d). 
#WU limits free calls, so it might not work if too many use it in one day! You could request your own key

import sys
import os
import urllib2
import json
import pprint
f = urllib2.urlopen('http://api.wunderground.com/api/5de2d6847556443d/conditions/q/98101.json') #Seattle zip code
json_string = f.read()
parsed_json = json.loads(json_string) 
pprint.pprint(parsed_json) #pretty print makes the json more readable - easier to figure out the hierarchy.

type(parsed_json)
parsed_json

#NYT API: Everything you need to scrape the NYT is here (also requires a key): 
#http://dlab.berkeley.edu/blog/scraping-new-york-times-articles-python-tutorial

#Twitter API https://dev.twitter.com/overview/api
#There are also specific python modules for working with Twitter

-----------------------------------------------------------------------------------------
#Scraping a single webpage

import sys
import os
import urllib

import urllib
opener = urllib.FancyURLopener({})
tempfile = opener.open("https://www.polisci.washington.edu/people")
polisci=tempfile.read()
open(polisci, 'w')
 
print polisci
type(polisci)  #it's a long string

plist=[polisci] #convert it to a list
print plist  #take a look at it now
type(plist)

#create a new list that split by words (at every \n or newline)
wlist=[polisci.split()] 
print wlist

#There are off the shelf tools such as downthemall, scrapy that are very useful for 
#scraping lots of pages

#--------------------------------------------------------
   
#This time, pre-process the text by stripping the html language and make the text more readable

import urllib
from bs4 import BeautifulSoup
from bs4 import re
import nltk  #this can take a while

url = "https://www.polisci.washington.edu/people"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)  #process as html
politext = soup.get_text() #extract the text
print politext
type(politext)

# Remove the many blank lines
lines = (line.strip() for line in politext.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
politext = '\n'.join(chunk for chunk in chunks if chunk)

print politext


#extract just the emails from the web page using a regular expression

import urllib
from bs4 import BeautifulSoup
from bs4 import re

poliemails=set() #create a set object
emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", politext, re.I)) 
poliemails.update(emails)  #add them to the set

print poliemails
type(poliemails)

emaillist=list(poliemails) #Now convert the set to a list of emails
emaillist[0]
 
#----------------------------------------------------------

#Download a web file and add it to a folder on the desktop

print os.getcwd()
%cd C:\Users\John.DESKTOP-ES1A8AS\Desktop\POLS559  
print os.getcwd()

import os
import urllib

filename = os.path.join('C:\Users\John.DESKTOP-ES1A8AS\Desktop\POLS559', 'syllabus.pdf')  #where it is going

urllib.urlretrieve("http://faculty.washington.edu/jwilker/559/http://faculty.washington.edu/jwilker/559/2018/Homework1.R", filename)  #where it is from

#Confirm that it is in your desktop folder?


-----------------------------------------------------------

#download three webfiles and import them into a list 
# it might be possible to use a regular expression for the doc number to get all of the minutes documents)

fedurllist=['https://www.federalreserve.gov/fomc/minutes/20060131.htm',
'https://www.federalreserve.gov/fomc/minutes/20060328.htm',
'https://www.federalreserve.gov/fomc/minutes/20060629.htm']

feddocs=[]

for element in fedurllist:
    t=urllib.urlopen(element).read()
    feddocs.append(t)
    
print feddocs[1][0:20] #first 21 characters of first element (transcript) in list

#------------------------------------------------------------

#Now we are going to manipulate some texts in more detail

# DO THIS FIRST: DOWNLOAD THE FOMC FOLDER AND FILES TO YOUR DESKTOP. TAKE A LOOK AT ONE OF THE FILES
# http://faculty.washington.edu/jwilker/559/FOMC/

import os
import nltk
import urllib
from bs4 import BeautifulSoup
from bs4 import re

#change to that folder on your desktop
%cd C:\Users\John.DESKTOP-ES1A8AS\Desktop\FOMC  #you'll need to create your own path

print os.getcwd()

#Create a list of the files in a folder

#below is a 'list comprehension' version of a loop that says add the name of any file that ends with .htm* 
#Below it is a loop that does the same thing

filelist = [filename for filename in os.listdir(os.getcwd()) if re.search(r'(.*\.htm*$)', filename) != None]

print len(filelist) #should equal number of html files in FOMC
print filelist[0]

#here's the other version
filelist2=[]
for filename in os.listdir(os.getcwd()):
    if re.search(r'(.*\.htm*$)', filename) !=None:
        filelist2.append(filename)

print len(filelist2) #should equal number of html files in FOMC
print filelist[0]

#loop through the files, pre-process and add to 'fomclist' 

fomclist = []
for element in filelist:
    input = open(element, 'r')
    y = BeautifulSoup(input.read()) 
    y = y.get_text() #get just the text (not html encoding)
    fomclist.append(y) #append the text to fomclist
  
len(fomclist) #should equal len(listing)    
print fomclist[0][1:100] #first 100 words of first meeting in list


nltk.download('punkt')  #module that parses sentences

sent_tokenize = nltk.data.load('nltk:tokenizers/punkt/english.pickle')

fomc_tok =[]
for element in fomclist:
      fomc_tok.append(sent_tokenize.tokenize(element))
      
print fomc_tok[0]

#what else are we doing in this block of code?!
      
meeting_sents=[]
for meeting in fomc_tok:
    for sentence in meeting:
        cleanwords=str(sentence.encode('ascii',errors='ignore'))
        meeting_sents.append(cleanwords.lower())
        
print meeting_sents[0]
#-------------------------------------------------------------

#Pop Quiz! What if you wanted to parse the meeting trascripts by 
#speaker statement instead of sentence?
#The answer is a little further below

#-------------------------------------------------------------
      
#remove stopwords and really short words. 
#this can take a while so we limited the number of meetings [0:10]

nltk.download('stopwords'),
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#Right now, each element in the list is a single long string. 
#Strings are immutable so we need to convert them to lists of words (and then back again later). 

meeting_sents2=[]
meeting_sents2 = [word_tokenize(i) for i in meeting_sents]  
                
print meeting_sents2[0]

#now that each word is separated we can manipulate them. 
#Lambda is like a list comprehension - a cleaner approach to embedding a conditional statement (in this case, filter if/or)

meeting_sents3=[]
for word in meeting_sents2[0:10]:
    keepwords = filter(lambda word: word not in stopwords.words('english') or len(word) >3, word)
    meeting_sents3.append(keepwords)
        
print meeting_sents2[0]
print meeting_sents3[0]

#if you wanted to include addtional stopwords

meeting_sents4=[]
mystop=['meeting','federal'] 

for word in meeting_sents3[0:10]:
    removewords = filter(lambda word: word not in mystop or len(word) >3, word)
    meeting_sents4.append(removewords)
    
print meeting_sents4[1]

#lambda above is an anonymous function. The line says filter (keep) only the words that fit the lambda function 'word' 

#------------------------------------------------------------- 

#stem words 
from nltk import PorterStemmer
Pstemmer = PorterStemmer()

print meeting_sents4[0] #take a look


meeting_sents5=[]

for sentence in meeting_sents4:
    newsent = []
    for word in sentence:
        mystem = ps.stem(word)
        newsent.append(mystem)
    meeting_sents5.append(newsent)
    
#now rejoin the words in each sentence in the list    
        
print meeting_sents5[1]

meeting_sents6=[]
for sentence in meeting_sents5:
    myjoin=" ".join(sentence)    
    meeting_sents6.append(myjoin)
               
print meeting_sents6[1]                 
                      
#-----------------------------------------------------------                  
                   
#What if we wanted to create one single list of words from all of the meetings? 

allMeetings= ' '.join(fomclist) #remember newlist?
allWords = nltk.word_tokenize(allMeetings)

#pre-process them again (be patient - this will take a while!) 

allWords = [word.lower() for word in allWords]
allWords2 = filter(lambda word: word not in stopwords.words('english') and len(word) >3, allWords)
allWords3 =  [Pstemmer.stem(word) for word in allWords2]
sorted(set(allWords3))

#We can use re's to remove additional junk in the file, such as \n (newline). 
#dirtyfile doesn't exist so this won't actually work
       
cleanfile=[]
for word in dirtyfile:
        fixed=re.sub(r'\\n', '', str(word))
        fixed=re.sub(r'\\\\u', '', fixed)        
        fixed=re.sub(r'[', '', fixed)
        fixed=re.sub(r'-+', '', fixed)
        fixed=re.sub(r'2014', "*\\", fixed)             
        cleanfile.append(fixed)

                      
-----------------------------------------------------

#if we decided that this was a list we wanted to keep, we would pickle (save) it. 
#Otherwise we'll have to run all of the code above

import pickle
pickle.dump(allWords3,open("allWords3.p", "wb"))

#To load the pickled file at some future time....

pkl_file = open('allWords3.p', 'rb')
allWords4 = pickle.load(pkl_file)
     
#-------------------------------------------------------------

#If we wanted to split the documents by speaker statement instead of sentence, 
#we would need to way to identify many different speakers' names. 
#In the FOMC transcripts, the speakers' names are uniquely in all capital letters (yea!)
#so we can use a regular expression

re.split(r'CHAIRMAN BERNANKE\\.|MR. [A-Z]+\\.|MRS. [A-Z]+\\.|MS. [A-Z]+\\.', nameofyourlist )

#This says split when it finds CHAIRMAN BERNANKE or MR. ALLCAPS or MRS. ALLCAPS etc.  Regular Expressions are the bomb.

#------------------------------------------------------
#PART III basic word frequencies

#These are just a few of the options

#Top 100 words (I think)

from collections import Counter
Counter(allWords4[1:100])

#How many instances of a specific word?"
     
allWords4.count("board")

#Frequency distribution of top 1000 words

allWords5=allWords4[1:1000]
fd = nltk.FreqDist(allWords5)
type(fd)

fd.plot(50, cumulative=True)

#------------------------------------------------------------------------

#Example of creating a document term matrix
#You'll need to install the textmining package
#download it and unzip to a folder
#use windows command prompt to navigate to the folder
#type 'python setup.py install' 
#tada!

import textmining

def termdocumentmatrix_example():
    # Create some very short sample documents
    doc1 = 'John and Bob are brothers.'
    doc2 = 'John went to the store. The store was closed.'
    doc3 = 'Bob went to the store too.'
    # Initialize class to create term-document matrix
    tdm = textmining.TermDocumentMatrix()
    # Add the documents
    tdm.add_doc(doc1)
    tdm.add_doc(doc2)
    tdm.add_doc(doc3)
    
    #note that instead of the above you could loop through a bunch of items in a list or whatever
        
    # Write out the matrix to a csv file. Note that setting cutoff=1 means
    # that words which appear in 1 or more documents will be included in
    # the output (i.e. every word will appear in the output). The default
    # for cutoff is 2, since we usually aren't interested in words which
    # appear in a single document. For this example we want to see all
    # words however, hence cutoff=1.
    tdm.write_csv('matrix.csv', cutoff=1)
    # Instead of writing out the matrix you can also access its rows directly.
    # Let's print them to the screen.
    for row in tdm.rows(cutoff=1):
            print row

termdocumentmatrix_example()


#ON A COMPLETELY DIFFERENT SUBJECT...
#-------------------------------------------------------------
# PART IV Interrater agreement

#This script works for a set of csv files (from different annotators) 
#that include several columns including coder, caseid, and label
#each csv file must be in the same format; and once they have been read in,
#the columns need to conform to the Python AnnotationTask requirements

import os
import nltk
import urllib
from bs4 import BeautifulSoup
from bs4 import re
import pandas as pi
import io

#Go to the directory where the csv files are located, for example: 

print os.getcwd()
%cd C:\Users\John.DESKTOP-ES1A8AS\POLS559\2018\ 

print os.getcwd()

#Create a list of the csv filenames in the directory
filelist = [filename for filename in os.listdir(os.getcwd()) if re.search(r'(.*\.csv*$)', filename) != None]

print len(filelist)
print filelist[0]

#read all of the csvs into a single list of dictionaries (called papcodes here). 
#I had to reformat the csv files so that they were identical

papcodes=[]  

import csv
for element in filelist:
    input_file = csv.DictReader(open(element))
    for r in input_file:
        papcodes.append(r)

print papcodes[0] #you'll see the keys and vaues for the first case/person

#retrieve only the values (not the keys) for each element

papcodes2=[]
for i in papcodes:
    j=dict.values(i)
    papcodes2.append(j)    

len(papcodes2)
print papcodes2[-1] #the keys should be gone

#the AnnotationTask module we will be using requires that the 
#order of each element in the list be coder, id, label so we may have to re-order the list entries

papcodes3=[]
myorder=[1,3,0,2]

for sublist in papcodes2:
    sublist_storer = []
    for element in myorder:
        sublist_storer.append(sublist[element])
    papcodes3.append(sublist_storer)        
        
len(papcodes3) 
print papcodes3[5]

#if we wanted to remove the last column completely

papcodes4=papcodes3
rmovIndxNo = 3
for i in papcodes4:
    del i[rmovIndxNo]

print papcodes4[3]

#Ready to examine interrater reliability. Consult the 
#AnnotationTask documentation for the different options

from nltk.metrics.agreement import AnnotationTask
import os.path
task = AnnotationTask(data=papcodes4)

task.avg_Ao()
task.alpha()

--------------------------------------------------------------
#Confusion matrix compares TRUE labels with PREDICTed labels. 
#True is the prexeisting label (of an expert annotator ("the gold standard")
#Predict includes just one response per bill

import os
import csv
import pandas as pd


#Quick tip! If you are using spyder and want to open plots etc in their own window, google it. 
#After you make the changes you have to restart spyder for it to work 


#confusion.csv has two columns, TRUE label and PREDICT label #for each bill.

confusiontrue=[]
confusionpredict=[]

filename = os.path.join('http://faculty.washington.edu/jwilker/559/confusion.csv') 
f = pd.read_csv(filename)
confusiontrue = f.TRUE
confusionpredict=f.PREDICT

#let's check

len(confusiontrue)
len(confusionpredict)

print(confusiontrue[0])
print(confusionpredict[0])

#OK, let's do it

from sklearn.metrics import confusion_matrix
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
import itertools

#IMPORTANT!! You need to create the def plot_confusion_matrix function BELOW before you do anything else

#need to provide labels
varnames=(1,2,3,4,5,6,7,8,10,12,13,14,15,16,17,18,19,20,21)

#this creates the basic matrix
cnf_matrix = confusion_matrix(confusiontrue, confusionpredict)
np.set_printoptions(precision=2)

#this creates the pretty plot

rcParams['figure.figsize'] = 20,30  #if the plot looks funny adjust the size

#Version 1: number of cases

plot_confusion_matrix(cnf_matrix, classes=varnames,
                      title='Confusion matrix, without normalization')

#Version 2: percent of cases

plot_confusion_matrix(cnf_matrix, classes=varnames, normalize=True, title='Normalized confusion matrix')

#You'll probably notice that there are some nan's (not a number) in the figure. 
#This is because at somepoint 0 is being used a diviser - the result of which is not a number
#To fix this, find the commented out line in the function below and make it functional. Should solve the problem! 


#Also, if you are using spyder and want to open plots etc in their own window, google it. 
#After you make the changes you have to restart spyder for it to work 



#Recall: % of the true cases that are correctly predicted
#Precision: % of predicted cases that are true cases.
#Not sure if there's an option for calculating these
--------------------------------------------------------
#Erratum: This long function is called above to create the plot and must be run before the above will work

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        #cm = np.nan_to_num(cm)
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], '.1f'),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

-------------------------------------------------------------

















