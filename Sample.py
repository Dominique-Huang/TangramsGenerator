from flask import Flask
from tangrams import tangramGenerator

app = Flask(__name__)

@app.route("/")
def hello():
    tangramGenerator()
    return "Hello Amon!"
    

if __name__ == "__main__":
    app.run(host = '127.0.0.1', port = 80)