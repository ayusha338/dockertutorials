from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask App!"

@app.route("/hello/string/")
def hello(name):
    return render_template(
    'test.html',name=string)


if __name__ == "__main__":
    app.run()

