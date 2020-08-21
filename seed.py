from models import db, connect_db, Todo
from app import app

db.drop_all()
db.create_all()

todos = [
  Todo(title="Wash Dishes"),
  Todo(title="Mow the lawm", done=True),
  Todo(title="Feed the dog"),
  Todo(title="Take a walk", done=True),
  Todo(title="Complete kata"),
  Todo(title="Complete journal entry", done=True),
  Todo(title="Repair laptop"),
  Todo(title="Sell laptop")
]

db.session.add_all(todos)
db.session.commit()