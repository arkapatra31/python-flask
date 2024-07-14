from flask import Flask

app = Flask(__name__)

@app.route('/')
def start():
    return "Server Started !!!"

if __name__ == '__main__':
    app.run(port=8000)