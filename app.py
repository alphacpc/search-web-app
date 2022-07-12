from flask import Flask, jsonify, render_template, request
from elasticsearch6 import Elasticsearch
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

elastic = Elasticsearch()

@app.route('/', methods=["GET"])
def home():
    body = {
        "size" : 1000,
        "query" : {
            "match_all":{}
        }
    }
    resp = elastic.search(index="flights", body = body)

    return render_template('home.html', data = resp['hits']['hits'])





@app.route('/data', methods=["GET"])
def data():
    body = {
        "size" : 100,
        "query" : {
            "match_all":{}
        }
    }

    resp = elastic.search(index="flights", body = body)

    return jsonify({ "data": resp['hits']['hits'] })



@app.route('/search', methods=["GET"])
def search_data():
    words = request.args.get('value')

    if words == "":
        body = {
            "size" : 1000,
            "query" : {
                "match_all":{}
            }
        }
    else:

        body = {
            "size": 1000,
                "query" : {
                    "multi_match": {
                        "type":       "bool_prefix",
                        # "type" : "best_fields", 
                        "fields" :  ["NUM_FLIGHT", "DEPART", "ARRIVE", "DATE_FORMATED", "AIRLINE", "ORIGIN_AIRPORT", "DESTINATION_AIRPORT"], 
                    "query" : words        
                    }
                }
            }


    resp = elastic.search(index="flights", body = body)
  

    return jsonify({"data": resp['hits']['hits']})



if __name__=='__main__':
    app.run(debug = True, port = 5000)