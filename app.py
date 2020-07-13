from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html"), 200


@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/cadastrar/')
def cadastrar():
    return render_template('cadastro.html')

        
    

if __name__ == "__main__":
    app.run(debug=True)
