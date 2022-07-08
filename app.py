from flask import Flask, render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://groupe3:passer123@localhost/chickens'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/', methods=["GET"])
def home():
    return render_template('home.html')


if __name__=='__main__':
    app.run(debug = True, port = 5000)