from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pizzaria.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True, index=True)
    telefone = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.String(2), nullable=False)
    cidade = db.Column(db.String(20), nullable=False)
    bairro = db.Column(db.String(20), nullable=False)
    rua = db.Column(db.String(20), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    complemento = db.Column(db.String(20), nullable=False)
    bairro = db.Column(db.String(20), nullable=False)
    
    def __str__(self):
        return self.name
    
                       
    
@app.route("/")
def index():
    return render_template("index.html"), 200


@app.route('/cadastrar/')
def cadastrar():
    return render_template("cadastro.html"), 200



if __name__ == "__main__":
    app.run(debug=True)
