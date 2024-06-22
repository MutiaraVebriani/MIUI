# app.py

from flask import Flask, jsonify, request, render_template
import requests

app = Flask(_name_)

@app.route('/')
def home():
    return render_template('index.html')

if _name_ == '_main_':
    app.run(debug=True)
