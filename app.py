from flask import Flask, render_template, request, redirect, url_for, session
#from prediction_model import predict

app = Flask("WaterConsumption")
app=Flask(__name__,template_folder='./')
app.secret_key = 'my_secret_key_is_here_hah'
@app.route('/')
def index():
    message = session.pop('message', None)
    textbox_id = session.pop('textbox_id', None)
    return render_template('index.html', message=message, textbox_id=textbox_id)

@app.route('/predict', methods=['POST'])
def predict():
    
    textbox1_data = request.form.get('textbox1')
    textbox2_data = request.form.get('textbox2')
    textbox3_data = request.form.get('textbox3')
    textbox4_data = request.form.get('textbox4')
    
    # Create a list of input data
    data_list = [textbox1_data, textbox2_data, textbox3_data, textbox4_data]


    # Call the predict function from your model file
    #prediction = predict(input_data)
    message = 'predict you haha'
    textbox_id = 'predresult'
    session['message'] = message
    session['textbox_id'] = textbox_id
    #prediction="haha"

    # Return the prediction result
    #return render_template('index.html', prediction=prediction)
    #return redirect(url_for('index', _anchor="pred", prediction=prediction))
    return redirect(url_for('index', _anchor="pred"))
if __name__ == '__main__':
    app.run(debug=True)