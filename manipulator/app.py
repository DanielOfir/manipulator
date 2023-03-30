from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/square', methods=['POST'])
def square():
    # Get the number from the POST request
    num = request.json['num']

    # Square the number
    square = num ** 2

    # Return the square as a JSON response
    return jsonify({'square': square})

@app.route('/double', methods=['POST'])
def double():
    # Get the number from the POST request
    num = request.json['num']

    # Square the number
    double = num * 2

    # Return the square as a JSON response
    return jsonify({'double': double})

@app.route('/', methods=['GET'])
def readiness_check():
    return '', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')