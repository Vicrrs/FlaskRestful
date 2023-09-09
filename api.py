from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY']='THISISSECRET'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////mnt/c/User/vicrrs/api_example/todo.db'

db = SQLAlchemy(app)

# Tabela do usuario
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.Boolean)
    admin = db.Column(db.Boolean)
    
# Tabela de tarefas
class Todo(db.Model):
    id = id.Column(db.Integer, primary_key=True)
    text = id.Column(db.String(50))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)
    
    
if __name__ == "__main__":
    app.run(debug=True)
