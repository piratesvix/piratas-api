from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

# Rota Inicial
@app.route("/")
def hello_world():
    return render_template('index.html')