from flask import Flask, jsonify

app = Flask(__name__)

# Route to get a greeting message
@app.route('/greeting', methods=['GET'])
def get_greeting():
    return jsonify({'message': 'Hello, welcome to the Flask API!'})

@app.route('/', methods=['GET'])
def get_greetings():
    return '<h1>hellooooo</h1>'


if __name__ == '__main__':
    app.run(debug=True)
