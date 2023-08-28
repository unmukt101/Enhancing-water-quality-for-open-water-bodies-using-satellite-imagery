#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install streamlit')


# In[2]:


import numpy as np


# In[3]:


import pickle


# In[4]:


loaded_model = pickle.load(open('C:/Users/spars/OneDrive/Desktop/minor-2/trained_model.sav', 'rb'))


# In[6]:


input_data = (8.1,1.01,8.4,18.2,0.01,350.8,300.45,-0.1,998.56)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The water is not safe')
else:
  print('The wate is safe')


# In[ ]:




