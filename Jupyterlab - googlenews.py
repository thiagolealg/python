#!/usr/bin/env python
# coding: utf-8

# In[16]:


get_ipython().system('pip install GoogleNews')


# In[17]:


from GoogleNews import GoogleNews


# In[18]:


import pandas as pd


# In[19]:


googlenews = GoogleNews()
googlenews.set_lang('pt')
googlenews.set_period('5d')


# In[21]:


googlenews.clear()


# In[23]:


googlenews.search('bolsonaro')


# In[25]:


googlenews.total_count()


# In[28]:


pesquisa_bolsonaro = googlenews.results()


# In[29]:


df_bolsonaro = pd.DataFrame(pesquisa_bolsonaro)    


# In[30]:


display(df_bolsonaro)


# In[31]:


googlenews.clear()


# In[35]:


pesquisa_lula = googlenews.search('Lula')


# In[36]:


googlenews.total_count()


# In[37]:


pesquisa_lula = googlenews.results()


# In[38]:


df_lula = pd.DataFrame(pesquisa_lula)


# In[39]:


display(df_lula)


# In[ ]:




