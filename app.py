import numpy as np
from flask import Flask, jsonify, request, render_template  
import pickle

app = Flask(__name__)

# Menyambungkan model pickle ke Flask
model1 = pickle.load(open("best_modelSVM.pkl", "rb"))
model2 = pickle.load(open("best_modelRF.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        link_input = request.form['link']
        link_data = [link_input]
        
        prediction1 = model1.predict(link_data)
        result1 = prediction1[0]
        print("Hasil prediksi SVM:", result1)
        
        prediction2 = model2.predict(link_data)
        result2 = prediction2[0]
        print("Hasil prediksi Random Forest:", result2)
        
        return render_template('index.html', link=link_input, result1=result1, result2=result2)

if __name__ == '__main__':
    app.run(debug=True)
