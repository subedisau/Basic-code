#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
df= pd.read_excel('C:/Users/subed/OneDrive/Desktop/testdata/weather.xlsx')
df


# In[10]:


rows, columns = df.shape
rows


# In[11]:


df.head()


# In[13]:


df[2:5]


# In[14]:


df.columns


# In[15]:


df.day


# In[16]:


df[['event','day']]


# In[19]:


df['temperature'].std()


# In[25]:


df['day'][df.temperature== df.temperature.max()]


# In[27]:


df.set_index('day', inplace=True)


# In[28]:


df


# In[29]:


df.loc['2017/1/5']


# In[31]:


df.loc['Snow']


# In[ ]:




