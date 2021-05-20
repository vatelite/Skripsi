#!/usr/bin/env python
# coding: utf-8

# In[1]:
import math
import pandas as pd


# In[2]:
df1=pd.read_csv('C:/Users/muham/new/train.csv')
df2=pd.read_csv('C:/Users/muham/new/test.csv')


# In[3]:
print(df1)


# In[4]:
#print(df2)


# In[5]:
df1=df1.sort_values(by=['Qmc'])
print(df1)


# In[6]:

# In[7]:
def getDoughertyBin(length):
    log_result = math.log(int(length), 10)
    nilai = 1 if log_result < 1 else math.floor(2*log_result)
    return float(nilai)


# In[8]:
getDoughertyBin(126)


# %%
