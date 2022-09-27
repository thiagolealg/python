#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install python-twitter-v2')


# In[2]:


get_ipython().system('pip install snscrape')


# In[20]:


import snscrape.modules.twitter as dados
import pandas as pd
import datetime


# In[21]:


lista_twittes_bolsonaro = []


# In[30]:


data_final = datetime.date.today()
data_inicial = '2022-1-1'


# In[34]:


for i, tweet in enumerate(dados.TwitterSearchScraper(f'{"Bolsonaro"} + since:{data_inicial} until:{data_final}').get_items()):
    if i>500:
        break
    lista_twittes_bolsonaro.append([tweet.date, tweet.id, tweet.content, tweet.username])


# In[35]:


df_bolsonaro = pd.DataFrame(lista_twittes_bolsonaro, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])


# In[36]:


display(df_bolsonaro)


# In[26]:


lista_twittes_lula = []


# In[37]:


for i, tweet in enumerate(dados.TwitterSearchScraper(f'{"Lula"} + since:{data_inicial} until:{data_final}').get_items()):
    if i>500:
        break
    lista_twittes_lula.append([tweet.date, tweet.id, tweet.content, tweet.username])


# In[38]:


df_lula= pd.DataFrame(lista_twittes_lula, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])


# In[39]:


display(df_lula)


# In[ ]:




