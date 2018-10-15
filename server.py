from flask import Flask, jsonify, abort, request

fapp = Flask(__name__)

# sample database
todos = [
    {
        'id': 1,
        'title': 'Learn ML',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Scala',
        'done': True
    }
]

# by default GET
@fapp.route('/index')
def hello():
    return 'Hello world to all'

@fapp.route('/contact-us')
def contactus():
    return "Email: mehul@gmail.com"

@fapp.route('/api/v1.0/todos')
def get_todos():
    return jsonify(todos)

@fapp.route('/api/v1.0/todos/<int:todo_id>')
def get_todo(todo_id):
    found_todos = [todo for todo in todos if todo['id'] == todo_id]
    if len(found_todos):
        return jsonify(found_todos[0])
    else:
        abort(404)

@fapp.route('/api/v1.0/todos', methods=['POST'])
def create_todo():
    todo = request.get_json()
    if len(todos):
        idnewtodo = todos[-1]['id'] + 1
    else:
        idnewtodo = 1
    todo['id'] = idnewtodo

    todos.append(todo)
    return jsonify(todo)

@fapp.route('/api/v1.0/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    found_todos = [todo for todo in todos if todo['id'] == todo_id]
    if len(found_todos):
        todos.remove(found_todos[0])
        return jsonify()
    else:
        abort(404)

@fapp.route('/api/v1.0/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    found_todos = [todo for todo in todos if todo['id'] == todo_id]
    if len(found_todos):
        todo = found_todos[0]
        todosent = request.get_json()
        todosent['id'] = todo['id']

        todos.remove(todo)
        todos.append(todosent)

        return jsonify(todosent)
    else:
        abort(404)
