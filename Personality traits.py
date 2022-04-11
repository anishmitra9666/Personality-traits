#!/usr/bin/env python
# coding: utf-8

# The data is the score of 104 humans across the big 5 psychology traits(extroversion, agreeableness, conscientiousness, 
# emotional stability and intellect/imagination). The goal is to create a plot which shows information on both where people 
# scored on the big have personality traits as well as how many people shared that score(duplicates). For this problem, I feel
# a bar chart is the most readable and gives off the most information.

# In[1]:


#Importing pandas, numpy and pyplot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure as fig


# In[2]:


#Reading in the data
df = pd.read_csv("characteristics - Sheet1.csv")


# In[3]:


#Perusing data
df.head(104)


# In[4]:


#Creating tuples of each series
dfextroversion = tuple(df["Extroversion"].head(110).values)
dfagreeableness = tuple(df["Agreeableness"].head(110).values)
dfconscientousness = tuple(df["Conscientiousness"].head(110).values)
dfemotionalstability = tuple(df["Emotional Stability"].head(110).values)
dfintellectimagination = tuple(df["Intellect/Imagination"].head(110).values)


# In[5]:


#Creating a list of values to distinguish personality traits equal to size of tuple(1-extroversion,2-agreeableness etc).
extroversionlist = []
for x in range(104):
    extroversionlist.append(1)
agreeablenesslist = []
for x in range(104):
    agreeablenesslist.append(2)
conscientousnesslist = []
for x in range(104):
    conscientousnesslist.append(3)
emotionalstabilitylist = []
for x in range(104):
    emotionalstabilitylist.append(4)
intellectimaginationlist = []
for x in range(104):
    intellectimaginationlist.append(5)


# In[6]:


#Converting series dataframes to dictionaries
extroversionduplicates = df["Extroversion"].value_counts().to_dict()
agreeablenessduplicates = df["Agreeableness"].value_counts().to_dict()
conscientousnessduplicates = df["Conscientiousness"].value_counts().to_dict()
emotionalstabilityduplicates = df["Emotional Stability"].value_counts().to_dict()
intellectimaginationduplicates = df["Intellect/Imagination"].value_counts().to_dict()


# In[7]:


#Creating lists for plots
xvalues = (extroversionlist, intellectimaginationlist, emotionalstabilitylist, conscientousnesslist, agreeablenesslist)
yvalues = (dfextroversion, dfagreeableness, dfemotionalstability, dfconscientousness, dfintellectimagination)


# Making sure the length of each and every series is the same. They all have 104 values as there are 104 total people so the check is verified.

# In[8]:


len(extroversionlist)


# In[9]:


len(intellectimaginationlist)


# In[10]:


len(emotionalstabilitylist)


# In[11]:


len(conscientousnesslist)


# In[12]:


len(agreeablenesslist)


# In[13]:


len(dfextroversion)


# In[14]:


len(dfagreeableness)


# In[15]:


len(dfconscientousness)


# In[16]:


len(dfemotionalstability)


# In[17]:


len(dfintellectimagination)


# Printing out the number of values at each level for each data point. Ex:- 67:11 means there are 11 people with an extroversion score of 67.

# In[18]:


extroversionduplicates


# In[19]:


agreeablenessduplicates


# In[20]:


conscientousnessduplicates


# In[21]:


emotionalstabilityduplicates


# In[22]:


intellectimaginationduplicates


# In[23]:


#Creating lists of duplicate values so that the final bar chart can accurately show the number of duplicates at each 
#level. There will be one less duplicate value than the total number of values at each level. Displaying the number of 
#duplicates is the best way to visualize this data as displaying all the values would make the final plot messy whereas 
#not displaying the number of duplicate values would hide a lot of useful information.
#Extroversion
extroversionduplicatevalues = []
for x in extroversionduplicates.values():
    numberofduplicates = x - 1
    extroversionduplicatevalues.append(numberofduplicates)
extroversionduplicatekeys = []
for x in extroversionduplicates.keys():
    extroversionduplicatekeys.append(x)
extroversiondictionary = {extroversionduplicatekeys[i]: extroversionduplicatevalues[i] for i in range(len(extroversionduplicatevalues))}
#Agreeableness
agreeablenessduplicatevalues = []
for x in agreeablenessduplicates.values():
    numberofduplicates = x - 1
    agreeablenessduplicatevalues.append(numberofduplicates)
agreeablenessduplicatekeys = []
for x in agreeablenessduplicates.keys():
    agreeablenessduplicatekeys.append(x)
agreeablenessdictionary = {agreeablenessduplicatekeys[i]: agreeablenessduplicatevalues[i] for i in range(len(agreeablenessduplicatevalues))}
#Conscientousness
conscientousnessduplicatevalues = []
for x in conscientousnessduplicates.values():
    numberofduplicates = x - 1
    conscientousnessduplicatevalues.append(numberofduplicates)
conscientousnessduplicatekeys = []
for x in conscientousnessduplicates.keys():
    conscientousnessduplicatekeys.append(x)
conscientousnessdictionary = {conscientousnessduplicatekeys[i]: conscientousnessduplicatevalues[i] for i in range(len(conscientousnessduplicatevalues))}
#Emotional Stability
emotionalstabilityduplicatevalues = []
for x in emotionalstabilityduplicates.values():
    numberofduplicates = x - 1
    emotionalstabilityduplicatevalues.append(numberofduplicates)
emotionalstabilityduplicatekeys = []
for x in emotionalstabilityduplicates.keys():
    emotionalstabilityduplicatekeys.append(x)
emotionalstabilitydictionary = {emotionalstabilityduplicatekeys[i]: emotionalstabilityduplicatevalues[i] for i in range(len(emotionalstabilityduplicatevalues))}
#Intellect/Imagination
intellectimaginationduplicatevalues = []
for x in intellectimaginationduplicates.values():
    numberofduplicates = x - 1
    intellectimaginationduplicatevalues.append(numberofduplicates)
intellectimaginationduplicatekeys = []
for x in intellectimaginationduplicates.keys():
    intellectimaginationduplicatekeys.append(x)
intellectimaginationdictionary = {intellectimaginationduplicatekeys[i]: intellectimaginationduplicatevalues[i] for i in range(len(intellectimaginationduplicatevalues))}

        

        


# Making dictionaries with the personality trait score as the key and the number of duplicates as the values.

# In[24]:


#Perusing the number of duplicate values for each personality trait score.
extroversiondictionary


# In[25]:


#Final dictionaries after dropping null values.
extroversiondc = {extroversionduplicatekeys : extroversionduplicatevalues for extroversionduplicatekeys, extroversionduplicatevalues in extroversiondictionary.items() if extroversionduplicatevalues != 0}
agreeablenessdc = {agreeablenessduplicatekeys : agreeablenessduplicatevalues for agreeablenessduplicatekeys, agreeablenessduplicatevalues in agreeablenessdictionary.items() if agreeablenessduplicatevalues != 0}
conscientousnessdc = {conscientousnessduplicatekeys : conscientousnessduplicatevalues for conscientousnessduplicatekeys, conscientousnessduplicatevalues in conscientousnessdictionary.items() if conscientousnessduplicatevalues != 0}
emotionalstabilitydc = {emotionalstabilityduplicatekeys : emotionalstabilityduplicatevalues for emotionalstabilityduplicatekeys, emotionalstabilityduplicatevalues in emotionalstabilitydictionary.items() if emotionalstabilityduplicatevalues != 0}
intellectimaginationdc = {intellectimaginationduplicatekeys : intellectimaginationduplicatevalues for intellectimaginationduplicatekeys, intellectimaginationduplicatevalues in intellectimaginationdictionary.items() if intellectimaginationduplicatevalues != 0}


# In[26]:


#Checking to see if the final dictionaries have null values and accurate number of duplicates. They did.


# In[27]:


extroversiondc


# In[28]:


agreeablenessdc


# In[29]:


conscientousnessdc


# In[30]:


emotionalstabilitydc


# In[31]:


intellectimaginationdc


# In[68]:


#Final plot
plt.figure(figsize=(16,16))
plt.scatter(xvalues,yvalues,c=xvalues)
plt.title("Big 5 personality traits", size =30)
plt.xlabel("Personality trait name", size =18)
plt.ylabel("Personality trait score", size =18)
labels = ["", "Extroversion", "", "Agreeableness", "", "Conscientiousness", "", "Emotional Stability", "", "Intellect/Imagination"]
ax = plt.gca()
ax.set_xticklabels(labels)
for i in extroversiondc:
    plt.text(x = 1.05, y = i, s = str(extroversiondc[i]),
    fontdict=dict(color='black', alpha=0.5, size=16))
for i in agreeablenessdc:
    plt.text(x = 2.05, y = i, s = str(agreeablenessdc[i]),
    fontdict=dict(color='black', alpha=0.5, size=16))
for i in conscientousnessdc:
    plt.text(x = 3.05, y = i, s = str(conscientousnessdc[i]),
    fontdict=dict(color='black', alpha=0.5, size=16))
for i in emotionalstabilitydc:
    plt.text(x = 4.05, y = i, s = str(emotionalstabilitydc[i]),
    fontdict=dict(color='black', alpha=0.5, size=16))
for i in intellectimaginationdc:
    plt.text(x = 5.05, y = i, s = str(intellectimaginationdc[i]),
    fontdict=dict(color='black', alpha=0.5, size=16))
plt.show()


# In[ ]:




