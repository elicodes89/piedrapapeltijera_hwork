from app import app
from models.game import lets_play


@app.route('/<player1choice>/<player2choice>')
def juego(player1choice, player2choice):
    return lets_play(player1choice, player2choice)
    # return player2choice

# @app.route('/tasks')
# def index():
#     return render_template('index.html', title='Home', tasks=tasks)

# @app.route('/tasks', methods=['POST'])
# def add_task():
#     task_title = request.form['title']
#     task_desc = request.form['description']
#     new_task = Task(task_title, task_desc, False)
#     add_new_task(new_task)

#     return render_template('index.html', title='Home', tasks=tasks)
