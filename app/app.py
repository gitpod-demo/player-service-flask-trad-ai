from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

# Sample data
players = [
    {'id': 1, 'nameFirst': 'Intuit', 'nameLast': 'Is Life'},
    {'id': 2, 'nameFirst': 'Eric', 'nameLast': 'Fa'},
    {'id': 3, 'nameFirst': 'Alice', 'nameLast': 'Smith'},
]

# Get all players
@app.route('/v1/players', methods=['GET'])
def get_players():
    return jsonify(players)

# Get a specific player by ID
@app.route('/v1/players/<int:player_id>', methods=['GET'])
def get_player(player_id):
    player = [player for player in players if player['id'] == player_id]
    if player:
        return jsonify(player[0])
    else:
        return jsonify({'message': 'player not found'}), 404

# Define a route for the POST method to match the curl call
@app.route('/team/generate', methods=['POST'])
def generate_team():
    # Parse the JSON request data
    data = request.get_json()

    # Define the URL for the POST request
    url = "http://127.0.0.1:5000/team/generate"

    # Extract the "seed_id" and "team_size" from the request
    seed_id = data.get('seed_id')
    team_size = data.get('team_size')

    # Define the data to be sent in the POST request
    data = {
        "seed_id": "abbotji01",
        "team_size": 10
    }

    # Make the POST request and pass the data as JSON
    response = requests.post(url, json=data)

    # Print the response from the server
    if response.status_code == 200:
        return jsonify(response)
    else:
        jsonify({'message': 'model not found'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)