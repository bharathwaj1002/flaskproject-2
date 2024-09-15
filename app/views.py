from flask import Blueprint, request, render_template, redirect
from .models import *

views = Blueprint('views',__name__)

@views.route('/',methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        to_be_added = Todo(content=task_content)
        
        db.session.add(to_be_added)
        db.session.commit()
        return redirect('/')
    else:
        todo = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=todo)