from flask import Flask, request, render_template, redirect, jsonify
from models import db, connect_db, Todo

app = Flask(__name__)

# Configure and Initialize Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///todos_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

# GET All Todos
@app.route("/api/todos")
def list_todos():
  all_todos = [todo.serialize() for todo in Todo.query.all()]
  return jsonify(todos=all_todos)

# GET Single Todo
@app.route("/api/todos/<int:id>")
def get_todo(id):
  todo = Todo.query.get_or_404(id)
  return jsonify(todo=todo.serialize())

# POST New Todo
@app.route("/api/todos", methods=["POST"])
def create_todo():
  new_todo = Todo(title=request.json["title"])
  db.session.add(new_todo)
  db.session.commit()
  response_json = jsonify(todo=new_todo.serialize())
  return (response_json, 201)