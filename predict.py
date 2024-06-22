# api/predict.py

from flask import Flask, jsonify, request
import pickle

app = Flask(_name_)

# Load models
model1 = pickle.load(open("best_modelSVM.pkl", "rb"))
model2 = pickle.load(open("best_modelRF.pkl", "rb"))

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json()
    link_input = data['link']
    link_data = [link_input]
    
    prediction1 = model1.predict(link_data)
    result1 = prediction1[0]
    
    prediction2 = model2.predict(link_data)
    result2 = prediction2[0]
    
    return jsonify({
        'link': link_input,
        'result1': int(result1),
        'result2': int(result2)
    })

if _name_ == '_main_':
    app.run(debug=True)
