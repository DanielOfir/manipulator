from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/manipulator', methods=['POST'])
def manipulator():
    # Get the number from the POST request
    num = request.json['num']
    square = num ** 2

    return jsonify({'square': square})

@app.route('/', methods=['GET'])
def readiness_check():
    return '', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')