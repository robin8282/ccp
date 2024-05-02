
# Not needed

from flask import Flask

app = Flask(__name__)
@app.route('/', methods = ['GET'])
def welcome():
    return "Welcome to python web service"

if __name__ == '__main__':
    app.run(debug= True, port=4430)