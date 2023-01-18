#!/usr/bin/env python
# coding: utf-8

# In[1]:

import warnings
warnings.filterwarnings('ignore') # setting ignore as a parameter


#importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')
#get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


#reading the rating csv file and displaying the first 5 rows
ratings = pd.read_csv('ratings.csv')
ratings.head(5)


# In[4]:


#reading the movie csv file and displaying the first 5 rows
movie = pd.read_csv('movies.csv')
print(movie.head())


# In[5]:


#merging both the rating and movie csv file and displaying the first 5 rows
data = pd.merge(ratings, movie, on='movieId')
data.head()


# In[9]:


#displaying the avaerage movie rating in the dataset
data.groupby('title')['rating'].mean().sort_values(ascending=False).head(10)



data.groupby('title')['rating'].mean().sort_values(ascending=False).head(10)

#total number of rating for a movie
data.groupby('title')['rating'].count().sort_values(ascending=False).head(10)



#add the mean rating to the dataframe
mean_rating= pd.DataFrame(data.groupby('title')['rating'].mean())
mean_rating.head()


#add the total number of rating to the dataframe
mean_rating['total_no_rating'] = pd.DataFrame(data.groupby('title')['rating'].count())
mean_rating.head()




#histogram of total number of rating
plt.figure(figsize=(10,8))
mean_rating['total_no_rating'].hist(bins=10)
plt.show()


# In[18]:


#histogram of average rating
plt.figure(figsize=(10,8))
mean_rating['rating'].hist(bins=50)


# In[19]:


#scatter plot of rating and total number of rating
plt.figure(figsize=(10,8))
sns.jointplot(x='rating', y='total_no_rating', data=mean_rating, alpha=0.4)


# In[41]:


#pivot table of movies titles and rating
user_rating = data.pivot_table(index='userId', columns='title', values='rating')
user_rating.head()


# In[42]:


#user ratings for Shawshank Redemption
Shawshank_Redemption_ratings = user_rating['Shawshank Redemption, The (1994)']
Shawshank_Redemption_ratings.head()


# In[43]:


#correlation between the user ratings for The Shawshank Redemption and all the other movies
Shawshank_Redemption = user_rating.corrwith(Shawshank_Redemption_ratings)
corr_Shawshank_Redemption = pd.DataFrame(Shawshank_Redemption, columns=['Correlation'])
corr_Shawshank_Redemption.dropna(inplace=True)
corr_Shawshank_Redemption.head()


# In[44]:


#show the top 5 correlated movies
corr_Shawshank_Redemption.sort_values('Correlation', ascending=False).head()


# In[49]:


#adding the total no of rating column to the Shawshank redemption column
corr_Shawshank_Redemption = corr_Shawshank_Redemption.join(mean_rating['total_no_rating'])
corr_Shawshank_Redemption.head()


# In[50]:


#displaying highly correlated movies with at least 50 total number of rating
corr_Shawshank_Redemption[corr_Shawshank_Redemption ['total_no_rating']>50].sort_values('Correlation', ascending=False).head()


# In[46]:


#correlation of all the other movies
user_rating = user_rating.dropna(thresh=10, axis=1).fillna(0,axis=1)
corrMatrix = user_rating.corr(method='pearson')
corrMatrix.head(100)


# In[ ]:




