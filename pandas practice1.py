#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df =pd.read_csv('US_Baby_Names_right.csv')


# In[3]:


df


# In[4]:


df.head()


# In[5]:


df.shape


# In[6]:


df.info(1)


# In[7]:


df.tail()


# In[8]:


df.columns


# In[9]:


df[['Name','Gender']]


# In[10]:


df[0:5]


# In[11]:


df.iloc[2:5]


# In[12]:


df.loc[df['Name'] == "Emma"]


# In[13]:


df.describe()


# In[14]:


df.sort_values('Name',ascending=False)


# In[15]:


df.sort_values('Name',ascending=True)


# In[16]:


df.sort_values(['Name','State'],ascending=[0,0])


# In[17]:


df['Age']=2021-df['Year']


# In[18]:


df.head(5)


# In[19]:


df=df.drop(columns=['Year'])


# In[20]:


df['Score']=df.iloc[:,6:7].sum(axis=1)
df


# In[21]:


li=list(df.columns)


# In[22]:


li


# In[23]:


#df=df.drop(columns='Score')
df.head(5)


# In[24]:


#df=df[li[0:5]+[li[7]]+[li[6]]


# In[25]:


df.loc[(df['Name']=='Emma') | ( df['State']=='AK')]


# In[26]:


EmmaAK=df.loc[(df['Name']=='Emma') & ( df['State']=='AK')]


# In[27]:


new_df=df.head(5)


# In[28]:


new_df


# In[29]:


new_df.to_csv('new_df.csv')


# In[30]:


EmmaAK


# In[31]:


EmmaAK=EmmaAK.reset_index()


# In[32]:


EmmaAK


# In[35]:


emma=df.loc[~df['Name'].str.contains('mm')]
emma


# In[36]:


emma=df.loc[df['Name'].str.contains('mm')]
emma


# In[41]:


emma.loc[emma['Name']=='Emma','Name']='new name'
emma


# In[42]:


emma.loc[emma['Name']=='new name','Name']='Emma'
emma 


# In[43]:


df.head(5)


# In[45]:


df.groupby(['Name']).mean()


# In[53]:


df.groupby(['Name']).mean().sort_values('Age',ascending=False)


# In[54]:


df['Age'].sum()


# In[55]:


df.count()


# In[61]:


df['Count']=1
all=df.groupby(['Name']).count()['Count']


# In[62]:


all


# In[67]:


#for chunk in pd.read_csv('US_Baby_Names_right.csv',chunksize=1000):
 #      print("DF for big data" )
  #     print(chunk)


# In[ ]:




