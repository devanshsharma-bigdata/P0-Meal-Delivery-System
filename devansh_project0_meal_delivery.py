#!/usr/bin/env python
# coding: utf-8

# In[103]:


#Importing the packages
import pymongo
import json
import warnings
warnings.filterwarnings('ignore')


# In[104]:


#Connecting to client


# In[105]:


client = pymongo.MongoClient('mongodb://localhost:27017')


# In[106]:


#Creating database


# In[107]:


db = client['project0_db']


# In[108]:


#Creating a collection


# In[109]:


collection=db['Meal_Delivery']


# In[110]:


#Loading JSON Data to collection


# In[111]:


with open('C:\\Users\Devansh Sharma\\Downloads\\meal_info.json') as file:
    data = json.load(file)


# In[112]:


collection.insert_many(data)


# In[113]:


document={'meal_id':'1111','category':'Beverages','cuisine':'French'}


# In[114]:


#Inserting one document


# In[115]:


collection.insert_one(document)


# In[116]:


documents=[{'meal_id':'7777','category':'Other Snacks','cuisine':'Indian'},{'meal_id':'8888','category':'Other Snacks','cuisine':'Arab'},{'meal_id':'9999','category':'Main Course','cuisine':'Korean'}]


# In[117]:


#Inserting many documents


# In[118]:


ids=collection.insert_many(documents)


# In[119]:


#Getting the inserted IDs of documents


# In[120]:


print(ids.inserted_ids)


# In[121]:


#Finding one document


# In[122]:


collection.find_one({'meal_id':'1111'})


# In[123]:


#Updating one document


# In[124]:


collection.update_one({ 'meal_id': '1111' },{'$set':{ 'cuisine': 'Italian' }})


# In[125]:


collection.find_one({'meal_id':'1111'})


# In[126]:


#Deleting one document


# In[127]:


collection.delete_one({'meal_id':'1111'})


# In[128]:


#Updating many documents


# In[129]:


collection.update_many({},{'$set':{'cuisine':'Turkish'}})


# In[130]:


query={'category':'Other Snacks'}


# In[131]:


#Deleting many documents


# In[132]:


collection.delete_many(query)


# In[133]:


#Finding many documents


# In[134]:


for i in collection.find():
    print(i)


# In[135]:


#Using sort to get the documents in ascending order


# In[136]:


for i in collection.find().sort("meal_id", 1):
    print(i)


# In[137]:


#Dropping the collection


# In[138]:


collection.drop()




