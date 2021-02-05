import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import math
app = Flask(__name__)
model = pickle.load(open('model_new.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [x for x in request.form.values()]
    print("x_test",x_test)
    for i in range(5):
        if(x_test[i]=='Y'):
            x_test[i]=1
        else:
            x_test[i]=0
            
    if(x_test[9]=='Y'):
        x_test[9]=1
    else:
        x_test[9]=0  
        
    if(x_test[10]=='U'):
        x_test[10]=0
    elif(x_test[10]=='R'):
        x_test[10]=1
    else:
        x_test[10]=2
    
    x_test = [float(x) for x in x_test]    
    x_test = [int(x) for x in x_test]  
    final_features = [np.array(x_test)]
    print(final_features)
    prediction = model.predict(final_features)
    print(prediction)
    output=round(prediction[0],2)
    if(output==1):
        msg = 'Approved'
    elif(output==0):
        msg = 'Disapproved'
    
    return render_template('index.html', prediction_text='Loan status  {}'.format(msg))
'''
@app.route('/predict_api',methods=['POST'])
def predict_api():
  #  For direct API calls trought request
    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)'''

if __name__ == "__main__":
    app.run(debug=True)
