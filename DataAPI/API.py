from flask import Flask
from flask_restful import Api,Resource

app = Flask(__name__)

@app.route('/HELLOWORLD')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)