from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class Todo(db.Model):
    task_id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    done=db.Column(db.Boolean, default=False)
    deadline = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f'<Task {self.name}>'

@app.route('/')
def home():
    todo_list=Todo.query.all()
    return render_template('index.html', todo_list=todo_list)

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    deadline = request.form.get('deadline')

    if deadline:
        deadline = datetime.strptime(deadline, '%Y-%m-%d').date()
    else:
        deadline = None

    new_todo = Todo(name=name, deadline=deadline)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/update/<int:todo_id>')
def update(todo_id):
    todo = Todo.query.get(todo_id)
    todo.done = not todo.done
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

if __name__=='__main__':
    app.run(debug=True)