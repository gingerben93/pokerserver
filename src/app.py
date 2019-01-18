from flask import Flask, jsonify, request
import json
import logging
import pokerRuleLogic
from pokerRuleLogic import make_player_hands
from pokerRuleLogic import find_player_hand_types
from pokerRuleLogic import find_winning_player
from pokerRuleLogic import make_community_cards

log = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index_get():
    if(request.method == 'GET'):
        return jsonify({'Start': 'Hello World'})

@app.route("/", methods=['POST'])
def index_post():
    if(request.method == 'POST'):
        list_values = []
        list_suits = []
        client_message = request.get_json()

        for row in client_message:
            row_json = client_message[row]
            print(row_json)
            for card in row_json:
                list_values.append((int)(client_message[row][card]['value']))
                list_suits.append((int)(client_message[row][card]['suit']))

        list_players = []
        test_community_cards = make_community_cards()
        player_hand1 = make_player_hands(list_values, list_suits)

        list_players.append(find_player_hand_types(test_community_cards, player_hand1, "player1"))

        find_winning_player(list_players)

        return jsonify({'post message': client_message})

@app.route("/", methods=['PUT'])
def index_put():
    if(request.method == 'PUT'):
        client_message = request.get_json()
        return jsonify({'put message': client_message})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
