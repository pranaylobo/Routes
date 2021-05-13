import requests
import polyline
from flask import jsonify
from flask import Flask
from flask import request
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
parser = reqparse.RequestParser()
parser.add_argument('place', type=str)

@app.route('/')
def hello():

    
    return jsonify("Success")




@app.route('/get_route',methods=['POST'])
def get_route():
    args = parser.parse_args()
    un = str(args['place'])
  
    print("hello",un)
    Tolls_Key = 'm34GG8f7Njnrr9TmFLnB3fb4MRHhRj8J'
    Tolls_URL = 'https://dev.tollguru.com/v1/calc/here'
    headers = {
            'Content-type': 'application/json',
            'x-api-key': Tolls_Key
          }
    params = {
            'from':
               {
                   'address': 'Borivali,Mumbai'
               },
           'to':
               {'address':
                    un
                },
            'vehicleType': '2AxlesAuto'
        }
    response = requests.post(Tolls_URL, json=params, headers=headers)


    a = response.json()


    arr12=[]
    for i in range(0,len(a["routes"])):
        dict1={}
        dict1.update({"route":i,"Duration":a["routes"][i]["summary"]['duration']['text'],"Distance":a["routes"][i]["summary"]['distance']['metric'],"polyline":polyline.decode(a["routes"][i]["polyline"]),"cost":a["routes"][i]["costs"]['cash']})
        arr12.append(dict1)

    return jsonify(value=arr12)

if __name__ == '__main__':
   app.run(threaded=True, port=5000)
