#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
import pandas as pd


# In[24]:


# Importing the data itself
data_set  = pd.read_csv('D:/ExcelR/Support Vector Machines/SalaryData_Train(1).csv')


# In[25]:


data_set.info()


# In[26]:


data_set.head()


# In[27]:


occupation_set = set(data_set['occupation'])
print(occupation_set)


# In[28]:


data_set['occupation'] = data_set['occupation'].map({'?': 0, ' Farming-fishing': 1, ' Tech-support': 2, 
                                                       ' Adm-clerical': 3, ' Handlers-cleaners': 4, ' Prof-specialty': 5,
                                                       ' Machine-op-inspct': 6, ' Exec-managerial': 7, 
                                                       ' Priv-house-serv': 8, ' Craft-repair': 9, ' Sales': 10, 
                                                       ' Transport-moving': 11, ' Armed-Forces': 12, ' Other-service': 13, 
                                                       ' Protective-serv': 14}).astype(int)
data_set.head()


# In[29]:


# Again, let's see how many unique categories we have in this property
income_set = set(data_set['Salary'])
print(income_set)


# In[30]:


# As expected. Just transforming now.

data_set['Salary'] = data_set['Salary'].map({' <=50K': 0, ' >50K': 1, np.NaN: 20}).astype(int)
data_set.head()


# In[31]:


# Just print it to see if nothing gone wrong
data_set.head()


# In[32]:


import matplotlib as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[33]:


data_set.groupby('education').Salary.mean().plot(kind='bar')


# In[34]:


data_set.groupby('occupation').Salary.mean().plot(kind='bar')


# In[35]:


from sklearn.model_selection import train_test_split

# Taking only the features that is important for now
X = data_set[['educationno','occupation']]

# Taking the labels (Income)
Y = data_set['Salary']

# Spliting into 80% for training set and 20% for testing set so we can see our accuracy
X_train, x_test, Y_train, y_test = train_test_split(X, Y, test_size=0.02, random_state=1)


# In[37]:


# Importing C-Support Vector Classification from scikit-learn
from sklearn.svm import SVC

# Declaring the SVC with no tunning
classifier = SVC()

# Fitting the data. This is where the SVM will learn
classifier.fit(X_train, Y_train)

# Predicting the result and giving the accuracy
score = classifier.score(x_test, y_test)

print(score)


# In[38]:


# Transforming the Sex into 0 and 1
data_set['sex'] = data_set['sex'].map({' Male': 0, ' Female': 1}).astype(int)
data_set.head()


# In[39]:


# How many unique races we got here?
data_set['race'] = data_set['race'].map({' Black': 0, ' Asian-Pac-Islander': 1, ' Other': 2, ' White': 3, 
                                             ' Amer-Indian-Eskimo': 4}).astype(int)
data_set.head()


# In[40]:


# What about maritial status?
mstatus_set = set(data_set['maritalstatus'])
print(mstatus_set)


# In[41]:


data_set['maritalstatus'] = data_set['maritalstatus'].map({' Married-spouse-absent': 0, ' Widowed': 1, 
                                                             ' Married-civ-spouse': 2, ' Separated': 3, ' Divorced': 4, 
                                                             ' Never-married': 5, ' Married-AF-spouse': 6}).astype(int)
data_set.head()


# In[42]:


import seaborn as sns
import matplotlib.pyplot as pplt
#correlation matrix
corrmat = data_set.corr()
f, ax = pplt.subplots(figsize=(12, 9))
sns.heatmap(corrmat, vmax=.8, square=True);


# In[43]:


k = 8 #number of variables for heatmap
cols = corrmat.nlargest(k, 'Salary')['Salary'].index
cm = np.corrcoef(data_set[cols].values.T)
sns.set(font_scale=1.25)
hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)
pplt.show()


# In[44]:


# Taking only the features that is important for now
X = data_set[['educationno', 'occupation','age']]

# Taking the labels (Income)
Y = data_set['Salary']

# Spliting into 80% for training set and 20% for testing set so we can see our accuracy
X_train, x_test, Y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)


# In[45]:


# Declaring the SVC with no tunning
classifier = SVC()

# Fitting the data. This is where the SVM will learn
classifier.fit(X_train, Y_train)

# Predicting the result and giving the accuracy
score = classifier.score(x_test, y_test)

print(score)


# In[46]:


# Taking only the features that is important for now
X = data_set[['educationno', 'age', 'hoursperweek', 'capitalgain']]

# Taking the labels (Income)
Y = data_set['Salary']

# Spliting into 80% for training set and 20% for testing set so we can see our accuracy
X_train, x_test, Y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)


# In[47]:


# Declaring the SVC with no tunning
classifier = SVC()

# Fitting the data. This is where the SVM will learn
classifier.fit(X_train, Y_train)

# Predicting the result and giving the accuracy
score = classifier.score(x_test, y_test)

print(score)


# In[48]:


data_set.groupby('race').Salary.mean().plot(kind='bar')


# In[49]:


data_set.groupby('sex').Salary.mean().plot(kind='bar')


# In[50]:


# Mean below 20 years old
data_set.groupby('age').Salary.mean().plot(kind='bar')

