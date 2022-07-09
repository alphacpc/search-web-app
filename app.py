from flask import Flask, jsonify, render_template, request
from elasticsearch6 import Elasticsearch
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

elastic = Elasticsearch()

@app.route('/', methods=["GET"])
def home():
    return render_template('home.html')


@app.route('/search', methods=["GET"])
def search_data():
    words = request.args.get('value')
    # resp = elastic.search(index="flights", query = {
    #     "multi_match": { 
    #         "type" : "best_fields", 
    #         "fields" :  ["NUM_FLIGHT", "DEPART", "ARRIVE", "DATE_FORMATED", "AIRLINE", "ORIGIN_AIRPORT", "DESTINATION_AIRPORT"], 
    #         "query" : words
    #     }
    # })


    return jsonify({"message": words})



if __name__=='__main__':
    app.run(debug = True, port = 5000)