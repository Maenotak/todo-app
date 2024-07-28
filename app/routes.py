from flask import Blueprint, render_template, request, red>

    main = Blueprint('main', __name__)

    tasks = []

    @main.route('/')
    def index():
        return render_template('index.html', tasks=tasks)

    @main.route('/add', methods=['POST'])
    def add():
        task = request.form.get('task')
        tasks.append(task)
        return redirect(url_for('main.index'))

    @main.route('/delete/<int:task_id>')
    def delete(task_id):
        if 0 <= task_id < len(tasks):
            tasks.pop(task_id)
        return redirect(url_for('main.index'))
