# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 21:38:40 2024

@author: ASUS
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading the saved model
diabetes_model=pickle.load(open('diabetes_model.sav','rb'))
Heart_disease_model=pickle.load(open('heart_disease_model.sav','rb'))
parkinsons_model=pickle.load(open('Parkinsson_model.sav','rb'))



#Sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           icons = ['activity','heart','person'],
                           default_index = 0)
    
    
#Diabetes Prediction Page
if(selected == 'Diabetes Prediction'):
    
    #Page title
    st.title('Diabetes Prediction using ML')
    
    #Getting the input data from the user
    # Columns for input fields
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    
    with col2:
        Glucose = st.text_input('Glucose Level')
        
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
        
    with col2:
        Insulin = st.text_input('Insulin Level')
        
    with col3:
        BMI = st.text_input('BMI value')
     
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        
    with col2:
        Age = st.text_input('Age of the Person')



        

    
    
    #Code for prediction
    diab_diagnosis = ''
    
    #Creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0]==1):
            diab_diagnosis = 'The person is Diabetic'
            
        elif (diab_prediction[0]==0):
            diab_diagnosis = 'The person is Not Diabetic'
            
            
    st.success(diab_diagnosis)
    
    
    
            
#Heart Disease Prediction Page
if(selected == 'Heart Disease Prediction'):
    
    #Page title
    st.title('Heart Disease Prediction using ML')
    col1,col2,col3=st.columns(3)
    
    with col1:
        age = st.number_input('Age of the Person')

    
    with col2:
        sex = st.number_input('Sex of the Person')

        
    with col3:
        cp = st.number_input('Chest pain types')

        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure')

        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')

        
    with col3:
        fbs = st.number_input('Fasting blood sugar > 120 mg/dl')

    with col1:
        restecg = st.number_input('Resting Electrocardiographic results')

        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.number_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.number_input('Mjor vessels colored by flourosopy')
        
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')



        

        
        


    
    
    
    #Code for prediction
    heart_diagnosis = ''
    
    #Creating a button for prediction
    
    if st.button('Heart Test Result'):
        heart_prediction = Heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if (heart_prediction[0]==1):
            heart_diagnosis = 'The person is suffering from Heart disease'
            
        else:
            heart_diagnosis = 'The person is Not suffering from Heart disease'
            
            
    st.success(heart_diagnosis)
    
    
    

    
#Parkinsons Prediction Page
if(selected == 'Parkinsons Prediction'):
    
    #Page title
    st.title('Parkinsons Prediction using ML')
    col1,col2,col3=st.columns(3)
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')


    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')


        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')


        
    with col1:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')


        
    with col2:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')


        
    with col3:
        RAP = st.text_input('MDVP:RAP')


    with col1:
        PPQ = st.text_input('MDVP:PPQ')


        
    with col2:
        DDP = st.text_input('Jitter:DDP')

        
    with col3:
        Shimmer = st.text_input('MDVP:Shimmer')

        
    with col1:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

        
    with col2:
        APQ3 = st.text_input('Shimmer:APQ3')

        
    with col3:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col1:
        APQ = st.text_input('MDVP:APQ')
        
    with col2:
        DDA = st.text_input('Shimmer:DDA')
        
    with col3:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col1:
        spread1 = st.text_input('spread1')
        
    with col2:
        spread2 = st.text_input('spread2')
        
    with col3:
        D2 = st.text_input('D2')
        
    with col1:
        PPE = st.text_input('PPE')


        

        
        
    #Code for prediction
    parkinsons_diagnosis = ''
        
    #Creating a button for prediction
        
    if st.button('Parkinsons Test Result'):
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
            
            if (parkinsons_prediction[0]==1):
                parkinsons_diagnosis = 'The person is suffering from Parkinsons disease'
                
            else:
                parkinsons_diagnosis = 'The person is Not suffering from Parkinsons disease'
                
                
    st.success(parkinsons_diagnosis)
        
        