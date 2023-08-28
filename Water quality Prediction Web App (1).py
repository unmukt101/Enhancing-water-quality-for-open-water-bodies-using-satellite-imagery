#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import streamlit as st


# In[3]:


import pickle


# In[4]:


loaded_model = pickle.load(open('C:/Users/spars/OneDrive/Desktop/water_qualtyprediction/trained_model.sav', 'rb'))


# In[5]:


import numpy as np
import streamlit as st



def waterquality_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)

    if (prediction[0] == 0):
        return 'The water is not safe'
    else:
        return 'The water is safe'
    
    
def main():
     
    # giving a title
    st.title('Water quality Prediction Web App')
        
    # getting the input data from the user
 
    pH = st.text_input("pH")
    Salinity= st.text_input("Salinity")
    Dissolved_Oxygen = st.text_input("Dissolved_Oxygen")
    Temperature = st.text_input("Temperature")
    Turbidity = st.text_input("Turbidity")
    Dissolved_Organic_Matter = st.text_input("Dissolved_Organic_Matter")
    Suspended_Matter = st.text_input("Suspended_Matter")
    Chlorophyll = st.text_input("Chlorophyll")
    
    
    # code for Prediction
    Prediction = ''
    
    # creating a button for Prediction
    
    if st.button('Water quality Result'):
        Prediction = waterquality_prediction([pH,Salinity,Dissolved_Oxygen,Temperature,
                         Turbidity,Dissolved_Organic_Matter, Suspended_Matter,Chlorophyll])
        
        
    st.success(Prediction)
    
    
if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:




