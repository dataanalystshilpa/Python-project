#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np   #mathematical operations in arrays
a1=np.array([1,2,3,4,5])
a2=np.array([[1,2,3],[4,5,6]])
sum1=np.sum(a1)
sum2=np.sum(a2)

print(sum1,sum2)


# In[9]:


import pandas as pd

data={'Name': ['a','b','c'],
        'Age': [25,30,35],
      
         'city': ['abc','xyz','pqr']}

df=pd.DataFrame(data)
print(df)


# # GLOBAL DATASET ANALYSIS

# In[5]:


import numpy as np
import pandas as pd


file_path=r'C:\Users\Digisnare\Downloads\Global_Superstore2.csv'
data=pd.read_csv(file_path,encoding='latin-1')
#file_path=r'C:/Users/Digisnare/Downloads/archive (1)/Global-Superstore.csv'
#data=pd.read_csv(file_path,encoding='latin-1')


# In[6]:


data


# # ANALYSING DATAFRAME

# # head

# In[20]:


data.head()   #shows first 5 rows in data


# # shape

# In[21]:


data.shape   #shows total number of rows and total number of columns


# # INDEX

# In[22]:


data.index    #shows the details about indexing


# # column   

# In[24]:


data.columns    #SHOWS ALL THE COLUMN NAMES


# # DTYPES

# In[25]:


data.dtypes    #SHOWS THE DATA TYPE OF EACH COLUMN


# # UNIQUE

# In[31]:


data['Category'].unique()  #PRINTS THE UNIQUE VALUES FROM THE COLUMN


# # nunique

# In[32]:


data.nunique()    #shows the count of the unique values in each column


# # count

# In[34]:


data.count()    #it shows the not null count in each column


# # value count

# In[35]:


data['Category'].value_counts()


# In[2]:


import matplotlib.pyplot as plt     #graphical representation of the data


# In[6]:


data.plot()


# In[10]:


data.plot(subplots=True)   #seperates each column visuals


# In[11]:


data.plot(title='GLOBAL DATASET ANALYSIS') #can give heading to your plots


# # ANALYSING

# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




