from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

todo_list = []

basedir = os.path.abspath(os.path.dirname(__file__))
todo_file = os.path.join(basedir, 'todo_list.txt')

#Load the to-do list from file before moving on. 
try:
    with open(todo_file, "r") as file:
        for line in file:
            todo_list.append(line.strip())
except FileNotFoundError:
    pass

@app.route("/")
def index():
    with open(todo_file, "r") as file:
        todo_list = file.read().splitlines()
    return render_template("index.html", todo_list=todo_list)

if __name__ == "__main__":
    app.run(debug=True)

