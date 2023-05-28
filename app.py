from flask import Flask, render_template, request
from prediction_model import predict
app = Flask("WaterConsumption")
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve form data
    data1 = request.form['textbox1']
    data2 = request.form['textbox2']
    data3 = request.form['textbox3']
    data4 = request.form['textbox4']
    
  # Create a list of input data
    input_data = [data1, data2, data3, data4]

    # Call the predict function from your model file
    prediction = predict(input_data)

    # Return the prediction result
    return render_template('result.html', prediction=prediction)