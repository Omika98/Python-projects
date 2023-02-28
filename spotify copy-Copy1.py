#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style 
import seaborn as sns


# In[2]:


spotify_tracks = pd.read_csv('C:/Users/Dell/Desktop/python study material/tracks.csv')
spotify_tracks.head()


# In[3]:


pd.isnull(spotify_tracks).sum()


# In[4]:


spotify_tracks.info()


# In[5]:


##top 10 least popular songs
sptf_sort = spotify_tracks.sort_values('popularity', ascending = True).head(10) 


# In[6]:


sptf_sort


# In[10]:


spotify_tracks.describe().transpose()


# In[17]:


##popularity in Descensing order greater than 90, iplace = false(do no not want to change in original dataframe)
sptf_popularity = spotify_tracks.query('popularity>90', inplace = False).sort_values('popularity', ascending=False)
sptf_popularity[:10]


# In[47]:


spotify_tracks.set_index('release_date', inplace = True)
spotify_tracks =pd.to_datetime(spotify_tracks.index)
spotify_tracks.head()


# In[29]:


spotify_tracks[["artists"]].iloc[18]


# In[44]:


spotify_tracks['Duration'] = spotify_tracks['duration_ms'].apply(lambda x: round(x/1000))
spotify_tracks.drop('duration_ms', inplace = True, axis =1)
spotify_tracks.Duration.head()


# In[20]:


correlation = spotify_tracks.drop(["key","mode","explicit"],axis=1).corr(method = "pearson")
spotify_tracks.corr()


# In[21]:



corr_heatmap = sns.heatmap(correlation,annot=True,vmin=-1,vmax=+1,center=0,cmap="inferno",linewidths=2,linecolor="Black")
corr_heatmap.set_title("correlation heatmap between variables")


# In[24]:


sample_df= spotify_tracks.sample(int(0.004*len(spotify_tracks)))
print(len(sample_df))


# In[28]:


plt.figure(figsize= (10,6))
sns.regplot(data=sample_df,y="loudness",x="energy",color ="c").set(title="loudness vs energy correlation")


# In[29]:


plt.figure(figsize= (10,6))
sns.regplot(data=sample_df,y="popularity",x="acousticness",color ="b").set(title="popularity vs acousticness correlation")


# In[5]:


##Renaming release_date to date
spotify_tracks.rename(columns = {'release_date': 'Date'},inplace = True)
spotify_tracks.Date= pd.to_datetime(spotify_tracks.Date)
spotify_tracks.head()


# In[12]:


##songs released in particular year
Chart = spotify_tracks['Date']


# In[28]:


plt.figure(figsize = (7,7))
Histogram = plt.hist(Chart,bins = 5,histtype='stepfilled')
plt.xlabel('Date')
plt.ylabel('Tracks released')
plt.title('Number of songs per year')
plt.show()


# In[17]:


##convert millisecond to seconds and plot line chart duration vs date
spotify_tracks["duration"]= spotify_tracks["duration_ms"].apply(lambda x:round(x/1000))
spotify_tracks.drop("duration_ms",inplace = True, axis =1) 
spotify_tracks.head()


# In[ ]:


Sec = spotify_tracks['duration_ms']
plt.plot(Chart,Sec)
plt.figure(figsize=(10,10)) 
plt.plot(Chart,Sec)
plt.title('Wind')


# In[ ]:




