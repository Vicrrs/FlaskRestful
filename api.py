from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY']='THISISSECRET'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/sqlite/todo.db'

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
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)
    
    
@app.route('/user', methods=['GET'])
def get_all_users():
    return ''


@app.route('/user/<user_id>', methods=['GET'])
def get_one_user():
    return ''


@app.route('/user', methods=['POST'])
def create_user():
    return ''


@app.route('/user/<user_id>', methods=['PUT'])
def promote_user()
    return ''


@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user():
    return ''

    
if __name__ == "__main__":
    app.run(debug=True)
