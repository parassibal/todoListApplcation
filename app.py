from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')


#{"todo": 'pushup', "done":True}
todos = [{"task": "Same Todo", "done": False}]

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

#adding todos
@app.route('/add', methods = ['POST'])
def add():
    todo = request.form['todo']
    todos.append({'task':todo, "done": False})
    return redirect(url_for("index"))

#editing todos
@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    todo = todos[index]
    if request.method == "POST":
        todo['task'] = request.form['todo']
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo, index=index)

#checking off todos
@app.route('/check/<int:index>')
def check(index):
    todos[index]['done'] = not todos[index]['done']
    return redirect(url_for("index"))


#deleting todos
@app.route('/delete/<int:index>')
def delete(index):
    del todos[index]
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)
