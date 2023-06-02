#!/usr/bin/env python3
from flask import Flask
from flask import Response
from flask import render_template
from flask_cors import CORS
from flask import request
from time import time
import json
app = Flask(__name__)
cors = CORS(app)
def generateResponse(result):
    response = {
        "sucess":result
    }
    return json.dumps(response)

@app.route('/',methods = ['POST','GET'])
def default():
    response = {'success': 'false'} 
    if(request.method == 'POST'):
        data = request.get_data()
        if(data):
            try:
                data = json.loads(data.decode('utf-8'))
            except:
                print(data)
                generateResponse(False)
            with open('logs/' + str(time()) + '.json','w') as h:
                h.write(json.dumps(data,indent=4))
            print(data)
            return generateResponse(True)
        # j = request.json()
        else:
            with open('result.data','wb') as h:
                h.write(data)
            # print(j)
            print(data)
    else:
        pass
    return generateResponse(False)
if(__name__ == '__main__'):
    app.run(host="0.0.0.0",debug=True)