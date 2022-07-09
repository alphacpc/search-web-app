from flask import Flask, render_template
from elasticsearch6 import Elasticsearch

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://groupe3:passer123@localhost/chickens'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

elastic = Elasticsearch()

@app.route('/', methods=["GET"])
def home():
    
    resp = elastic.get(index='csv', id='7amA3oEBF_mbnRB09AuW', doc_type='_doc').get('_source')
    print(resp)
    

    return render_template('home.html')


if __name__=='__main__':
    app.run(debug = True, port = 5000)