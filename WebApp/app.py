from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

todo_list = []

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) #My txt file is not in the same directory thus i needed to add an extra "dirname"
todo_file = os.path.join(basedir, 'todo_list.txt')

#Load the to-do list from file before moving on. 
try:
    with open(todo_file, "r") as file:
        for line in file:
            todo_list.append(line.strip())
except FileNotFoundError:
    pass

#Http endpoints
@app.route("/")
def index():
    with open(todo_file, "r") as file:
        todo_list = file.read().splitlines()
    return render_template("index.html", todo_list=todo_list)

@app.route("/add", methods=["POST"])
def add_todo():
    todo = request.form["todo"]
    todo_list.append(todo)
    save_todo_list()
    return redirect(url_for("index"))

@app.route("/remove", methods=["POST"])
def remove_todo():
    item_number = int(request.form["item_number"])
    if 0 < item_number <= len(todo_list):
        todo_list.pop(item_number - 1)
        save_todo_list()
    return redirect(url_for("index"))


#Save to file method
def save_todo_list():
    with open("todo_list.txt", "w") as file:
        for todo in todo_list:
            file.write(todo + "\n")


if __name__ == "__main__":
    app.run(debug=True)

