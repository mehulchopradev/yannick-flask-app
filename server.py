from flask import Flask, jsonify, abort, request
# from db.dbconnect import connect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

fapp = Flask(__name__)
fapp.config.from_object(Config)
db = SQLAlchemy(fapp)
migrate = Migrate(fapp, db)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50))
    done = db.Column(db.Boolean)

# sample database
'''todos = [
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
]'''

# by default GET
@fapp.route('/index')
def hello():
    return 'Hello world to all'

@fapp.route('/contact-us')
def contactus():
    return "Email: mehul@gmail.com"

@fapp.route('/api/v1.0/todos')
def get_todos():
    todos_db = []
    '''try:
        con = connect()
    except Exception as e:
        print(e)
        abort(500)
    else:
        query = 'select * from todos'
        cursor = con.cursor()

        try:
            cursor.execute(query)
        except Exception as e:
            print(e)
            abort(500)
        else:
            for row in cursor:
                row_dict = {
                    'id': row[0],
                    'title': row[1],
                    'done': False if row[2] == '0' else True
                }
                todos_db.append(row_dict)

            con.close()
            return jsonify(todos_db)'''

    todos = Todo.query.all()
    todoslist = [{
        'id': todo.id,
        'title': todo.description,
        'done': todo.done
    } for todo in todos]
    return jsonify(todoslist)

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
    '''if len(todos):
        idnewtodo = todos[-1]['id'] + 1
    else:
        idnewtodo = 1
    todo['id'] = idnewtodo'''
    '''try:
        con = connect()
    except Exception as e:
        print(e)
        abort(500)
    else:
        cursor = con.cursor()
        query = 'insert into todos(title, done) values(%s, %s)'
        try:
            cursor.execute(query, (todo['title'], todo['done']))
        except Exception as e:
            print(e)
            abort(500)
        else:
            con.commit()
            con.close()

            todo['id'] = cursor.lastrowid
            return jsonify(todo)'''

    todo_obj = Todo(description=todo['title'], done=todo['done'])
    db.session.add(todo_obj)
    db.session.commit()
    return jsonify({
        'id': todo_obj.id,
        'title': todo_obj.description,
        'done': todo_obj.done
    })

    # todos.append(todo)

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
