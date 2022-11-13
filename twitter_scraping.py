#!/usr/bin/env python
# coding: utf-8

# In[7]:


get_ipython().system('pip install -q snscrape')


# In[152]:


get_ipython().system('pip install dnspython')
get_ipython().system('pip install pymongo[srv]')


# In[153]:


import snscrape.modules.twitter as sntwitter
import pandas as pd
import time


# In[154]:


import pymongo

client = pymongo.MongoClient("mongodb+srv://jayasurya:DbVF6hJM01Um69cu@cluster0.m5oaa.mongodb.net/?retryWrites=true&w=majority")
db = client.web_scraping
records = db.tweets


# In[155]:


tweets_list = []


# In[156]:


start_time = time.time()
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:NetflixIndia').get_items()): #declare a username 
    if i>10:                                                                             #number of tweets you want to scrape
        break
    tweets_list.append([tweet.date, tweet.id, tweet.user.username, tweet.outlinks, tweet.tcooutlinks,
                        tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.quoteCount, tweet.conversationId,
                        tweet.lang, tweet.retweetedTweet]) #declare the attributes to be returned
    
print("%s seconds" % (time.time() - start_time))
    


# In[157]:


# Creating a dataframe from the tweets list above 
tweets_df = pd.DataFrame(tweets_list, columns=['datetime', 'tweet_id', 'username', 'outlinks', 'tcooutlinks',
                                                'reply_count', 'retweet_count', 'likecount', 'quote_count', 'conversation_id',
                                                'language', 'retweeted_tweet'
                                               ])


# In[158]:


tweets_df.info()


# In[159]:


tweets_df.head()


# In[160]:


tweets_df.shape


# In[161]:


#tweets_df['url'].dtype


# In[162]:


#tweets_df['url'] = tweets_df['url'].astype('|S')


# In[163]:


tweets_dict = tweets_df.to_dict('records')


# In[164]:


tweets_dict


# In[165]:


records.insert_many(tweets_dict)

#issue 1 : documents must be non-empty list - included 'records' in the to_dict
#issue 2: bad auth : Authentication failed - removed < & > while connecting to client
#issue 3: cannot encode object: Photo - removed 'media'
#issue 4 : cannot encode object: user - removed 'mentioned_users'
#issue 4 : cannot encode object: Tweet - removed 'url', 'source', 'tweet', 'quoted_tweet'


# In[ ]:


#installation of streamlit
#Using anaconda navigator terminal, installation needs to be done
#login to share.streamlit.io
#


# In[169]:



import streamlit as st


# In[177]:


st.text('hello')


# In[172]:


st.write('Twitter Scrapping')
st.write(tweets_df)


# In[178]:


st.dataframe(tweets_df)


# In[ ]:


#NameError: name 'get_ipython' is not defined

