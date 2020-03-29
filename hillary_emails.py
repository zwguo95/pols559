import os
import pandas as pd
import re 
import gensim
from gensim import corpora
from gensim.models import ldamodel 
from nltk.corpus import stopwords  

# os.chdir('your directory') 
dir_path = os.getcwd()   
data_path = dir_path + '\hillary_emails.csv'
df = pd.read_csv(data_path)
df = df[['Id','ExtractedBodyText']].dropna() # there are a lot of NAs and we simply drop them this time

# define a method to clean the email text with the help of regular expressions 
def clean_email_text(text):
    text = text.replace('\n',' ') # discard new lines 
    text = re.sub(r'-', ' ', text) # separate the words containing "-"
    text = re.sub(r'\d+/\d+/\d+', '', text) # discard dates 
    text = re.sub(r'[0-2]?[0-9]:[0-6][0-9]', '', text) # discard time
    text = re.sub(r'[\w]+@[\.\w]+', '', text) # discard email addresses 
    text = re.sub(r'/[a-zA-Z]*[:\//\]*[A-Za-z0-9\-_]+\.+[A-Za-z0-9\.\/%&=\?\-_]+/i', '', text) # discard website addresses
    plain_text = ''
    # check if there are other special characters (we only need alphabets and spaces)
    for letter in text:
        if letter.isalpha() or letter==' ':
            plain_text += letter
    text = ' '.join(word for word in plain_text.split() if len(word)>1)
    return text

docs = df['ExtractedBodyText'] # get the email text 
docs = docs.apply(lambda s: clean_email_text(s)) # clean the email text 
doclist = docs.values # get the email content 
print(f"There are {len(doclist)} emails.") 

# remove the stop words, months, weekdays, and am/pm 
stop_words = list(stopwords.words('english'))
ampm = ['am','pm']
weeks = ['monday','mon','tuesday','tues','wednesday','wed','thursday','thur','friday','fri','saturday','sat','sunday','sun']
months = ['jan','january','feb','february','mar','march','apr','april','may','jun','june','jul',
          'july','aug','august','sept','september','oct','october','nov','november','dec','december']
stop_words = stop_words + ampm + weeks + months
       
texts = [[word for word in doc.lower().split() if word not in stop_words] for doc in doclist]   
 
# create corporas and attach index to each email text
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
# train the first LDA model 
lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=10) # train 10 topics this time
print(lda.print_topics(num_topics=10, num_words=5))  # take a look at all the topics 

# save the LDA model 
lda.save(dir_path + '\email_lda.model')

# load the LDA model and estimate the topic with new data 
lda = ldamodel.LdaModel.load(dir_path + '\email_lda.model') 
tweets = ['It\'s Election Day! Millions of Americans have cast their votes for Hillary—join them and confirm where you vote ',
       'Hoping everyone has a safe & Happy Thanksgiving today, & quality time with family & friends. -H']

tweets_text = [clean_email_text(t) for t in tweets]
texts = [[word for word in text.lower().split() if word not in stop_words] for text in tweets_text]
corpus_tweets = [dictionary.doc2bow(text) for text in texts]
topics_tweets = lda.get_document_topics(corpus_tweets) 
print('The topic distribution of the two tweets are: \n' + str(topics_tweets[0]) + '\n' + str(topics_tweets[1]))