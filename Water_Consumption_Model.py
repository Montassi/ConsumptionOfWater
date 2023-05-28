# Import necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score 
from sklearn.ensemble import RandomForestRegressor
import pickle


# Load the dataset
data = pd.read_excel("D:/LP_S5_S6/EST Salé/S6/Stage LP/Ain Aouda/Water/water_Final/Nouveau dossier/Join_Dataset_Consommation_eau_2010-2021.xlsx")
data['Id_Participant']=data['Id_Participant']

le = LabelEncoder()
data['Type_Participant'] = le.fit_transform(data['Type_Participant'])

xe = LabelEncoder()
data['Id_Participant'] = xe.fit_transform(data['Id_Participant'])

# Split dataset into training and testing sets
X = data.drop('Consomation', axis=1)
Y = data['Consomation']
#X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


# Define the model
model = RandomForestRegressor(n_estimators=165, random_state=100)
model.fit(X_train, Y_train)
# Make predictions on the testing data
y_pred = model.predict(X_test)

filename= "Consumption_Model"
pickle.dump(model,open(filename,'wb'))

