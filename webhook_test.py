# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 22:35:36 2022

@author: NISHIO KOJI
"""

import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # if request.method == 'POST':
    #     print("Data received from Webhook is: ", request.json)
    #     return "Webhook received!"
    
    data = json.loads(request.data)
    
    print(data["ticker"])
    print(data["bar"])
    
    return {
        "code": "success",
        "message": data
        }
