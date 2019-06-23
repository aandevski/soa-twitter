from flask import Flask
import consul
app = Flask(__name__)


consul.register()


@app.route("/")
def hello():
    return "Hello from tweets!"
