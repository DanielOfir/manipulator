from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/manipulator', methods=['POST'])
def manipulator():
    # Get the number from the POST request
    nums = request.json['nums']
    square = nums[0] ** 2
    double = nums[1] * 2
    triple = nums[2] * 3

    return jsonify({'square': square,'double': double,'triple': triple})

@app.route('/', methods=['GET'])
def readiness_check():
    return '', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')