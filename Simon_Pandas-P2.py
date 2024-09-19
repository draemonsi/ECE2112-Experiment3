#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd


# In[15]:


cars = pd.read_csv('cars.csv')


# In[17]:


# Part a: Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...)
# By using the iloc function and setting the index to :5 and ::2 it means that it will display 5 columns with a 2 step interval
first_five_odd_columns = cars.iloc[:5, ::2]
print(first_five_odd_columns)


# In[25]:


# Part b: Display the row that contains the ‘Model’ of ‘Mazda RX4’.
# Indexing with the given condition that if the value in the Model column is equal to Mazda RX4; it will display the row of that
mazda_rx4_row = cars[cars['Model'] == 'Mazda RX4']
print(mazda_rx4_row)


# In[33]:


# Part c: How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
# Indexing with the given condition that if the value in the Model is equal to Camaro Z28; it will display the 'cyl' column of that row
cyl_camaro_z28 = cars[cars['Model'] == 'Camaro Z28']['cyl']
print(cyl_camaro_z28)


# In[35]:


# Part d: Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models 
# ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
# Storing the model as string to models
# Indexing with the given condition that if the value in models is equal to Model, if so; print the Model, Cyl, and gear columns of the rows
models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
selected_cars = cars[cars['Model'].isin(models)][['Model', 'cyl', 'gear']]
print(selected_cars)


# In[ ]:




