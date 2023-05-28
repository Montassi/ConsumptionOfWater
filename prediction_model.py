import joblib

def load_model():
    # Load your trained model
    model = joblib.load('Consumption_Model.pkl')
    return model

def predict(data):
    # Load the model
    model = load_model()

    # Make predictions
    predictions = model.predict(data)

    return predictions