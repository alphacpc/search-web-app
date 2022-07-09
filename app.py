from flask import Flask, jsonify, render_template, request
from elasticsearch6 import Elasticsearch
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://groupe3:passer123@localhost/chickens'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)



@app.route('/', methods=["GET"])
def home():    
    return render_template('home.html')


@app.route('/search', methods=["GET"])
def search_data():
    words = request.args.get('value')
    return jsonify({"message": words})


if __name__=='__main__':
    app.run(debug = True, port = 5000)