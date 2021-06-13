from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('banglore_home_prices_model.pickle', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        sqft=float(request.form['Total SQFT'])
        bath=int(request.form['Bath'])
        bhk=int(request.form['BHK'])
        price_sqft=request.form['Price Per SQFT']
        size=request.form['Size']
        prediction=model.predict([[sqft,bath,bhk,price_sqft,size]])
        output=int(prediction[0])
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot buy this property")
        else:
            return render_template('index.html',prediction_text="You Can buy The property at Rs {} Lakhs".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
