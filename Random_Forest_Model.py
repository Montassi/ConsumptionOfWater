# -*- coding: utf-8 -*-
"""
Created on Mon May 29 00:03:47 2023

@author: montasser
"""


# Import necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib


# Load the dataset
data = pd.read_excel("D:/LP_S5_S6/EST Salé/S6/Stage LP/Ain Aouda/Water/water_Final/Nouveau dossier/Join_Dataset_Consommation_eau_2010-2021.xlsx")
# Encode String columns
le = LabelEncoder()
data['Type_Participant'] = le.fit_transform(data['Type_Participant'])
xe = LabelEncoder()
data['Id_Participant'] = xe.fit_transform(data['Id_Participant'])

# Split dataset into training and testing sets
X = data.drop('Consomation', axis=1)
Y = data['Consomation']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Define the model
model = RandomForestRegressor(n_estimators=165, random_state=100)

# Train the model
model.fit(X_train, Y_train)

# Save the model
joblib.dump(model, 'D:/LP_S5_S6/EST Salé/S6/Stage LP/Ain Aouda/Water/water_Final/Nouveau dossier/random_forest.joblib')
