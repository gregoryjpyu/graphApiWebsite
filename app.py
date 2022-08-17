from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! testing 2</p>"

if __name__ == '__main__':
    app.run()
