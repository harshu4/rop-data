from flask import Flask, request, jsonify
app = Flask(__name__)


def background():
    pass




@app.route('/task', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    background()
    return ("herlllo")    



# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)