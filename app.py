from flask import Flask, request, jsonify
from utils import convert_message_to_token, predict

app = Flask(__name__)

@app.route('/convert_message', methods=['POST'])
def convert_message():
    # Get the message from the request JSON data
    data = request.get_json()
    if 'message' not in data:
        return jsonify({'error': 'Message not provided in JSON data'}), 400

    # Retrieve the message from the JSON data
    message = data['message']

    # Use the convert_message_to_token function
    tokenized_message = convert_message_to_token(message)

    # Return the converted message as JSON response
    return jsonify({'converted_message': tokenized_message})

@app.route('/predict', methods=['POST'])
def predict_message():
    # Get the message from the request JSON data
    data = request.get_json()
    if 'message' not in data:
        return jsonify({'error': 'Message not provided in JSON data'}), 400

    # Retrieve the message from the JSON data
    message = data['message']

    # Use the convert_message_to_token function
    prediction = predict(message)

    # Return the converted message as JSON response
    response = 'Message is not a spam' if int(prediction) == 0 else 'Message is a spam'
    return jsonify({'prediction': response})

if __name__ == '__main__':
    app.run(debug=True)
