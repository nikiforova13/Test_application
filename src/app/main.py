from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def get_func():
    "hellloooo"
    return "<h1>HELLO, my name ku</h1>"
    # return render_template()


