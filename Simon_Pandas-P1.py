#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# ####  Import cars.csv file

# In[10]:


cars = pd.read_csv('cars.csv')


# In[12]:


cars


# #### Displaying the first five and last row of the csv file.

# In[37]:


# By using the concat function, we can simultaneously show the results as the first five and last rows of the CSV file.
result = pd.concat([cars.head(), cars.tail()])


# In[39]:


result

