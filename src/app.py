from flask import Flask, jsonify, request
import json
import logging

#import pokerRuleLogic
from pokerRuleLogic import Number
from pokerRuleLogic import Suit
from pokerRuleLogic import Player_data
from pokerRuleLogic import make_deck
from pokerRuleLogic import make_player_hand
from pokerRuleLogic import make_player_hands
from pokerRuleLogic import find_player_hand_types
from pokerRuleLogic import find_winning_player
from pokerRuleLogic import make_community_cards

from init import create_app
from models import Users, db

class community_cards:
    def __init__(self, json_dict):
        self.card_values = json_dict['card_values']
        self.card_suits = json_dict['card_suits']

log = logging.getLogger(__name__)

app = Flask(__name__)

deck = []

#testing db connection
###########################

app = create_app()

@app.route("/get_all", methods=['GET'])
def fetch():
    users = Users.query.all()
    all_users = []
    for user in users:
        new_user = {
            "user_id": user.user_id,
            "user_name":  user.user_name,
            "user_password": user.user_password
        }

        all_users.append(new_user)
    return json.dumps(all_users)

@app.route("/add", methods=['POST'])
def add():
    user_data = request.get_json()

    name = user_data['user_name']
    password = user_data['user_password']

    user = Users(user_name = name, user_password = password)
    db.session.add(user)
    db.session.commit()
    return json.dumps("Added User"), 200

###########################

@app.route("/", methods=['GET'])
def index_get():
    if(request.method == 'GET'):
        return jsonify({'Start': 'get'})

@app.route("/get_free_cards", methods=['GET'])
def get_free_cards():
    if(request.method == 'GET'):
        global deck
        deck = make_deck()
        player_hand = make_player_hand(deck)
        cards_value = []
        cards_suit = []

        for c in player_hand.hand:
            cards_value.append(c.value.value)
            cards_suit.append(c.suit.value)

        cards_dict = {}
        cards_dict['card_values'] = cards_value
        cards_dict['card_suits'] = cards_suit

        player_free_cards = community_cards(cards_dict)

        json_string_free_cards = json.dumps(player_free_cards.__dict__)

        return json_string_free_cards

@app.route("/lock_in_cards", methods=['POST'])
def lock_in_cards():
    if(request.method == 'POST'):
        list_values = []
        list_suits = []
        client_message = request.get_json()

        player_cards = community_cards(client_message)

        list_players = []
        global deck
        test_community_cards = make_community_cards(deck)

        #add current player
        player_hand1 = make_player_hands(player_cards.card_values, player_cards.card_suits)

        #have to add players to list
        list_players.append(find_player_hand_types(test_community_cards, player_hand1, "player1", player_cards.card_values, player_cards.card_suits))

        #start at two because nuner is used to name player; change later when play name comes from player
        for i in range(2,4):
            temp_player = make_player_hand(deck)
            temp_values = []
            temp_suits = []
            for x in temp_player.hand:
                temp_values.append(x.value.value)
                temp_suits.append(x.suit.value)

            temp_player_hand = make_player_hands(temp_values, temp_suits)

            #have to add players to list
            list_players.append(find_player_hand_types(test_community_cards, temp_player_hand, "player" + str(i), temp_values, temp_suits))

        list_player_data = find_winning_player(list_players)

        cards_value = []
        cards_suit = []

        for c in test_community_cards:
            cards_value.append(c.value.value)
            cards_suit.append(c.suit.value)

        list_dict_player_data = {}
        list_data = []

        cards_dict = {}
        cards_dict['card_values'] = cards_value
        cards_dict['card_suits'] = cards_suit

        current_comminty_cards = community_cards(cards_dict)

        list_dict_player_data["communityCards"] = current_comminty_cards.__dict__

        for player_data in list_player_data:
            list_data.append(player_data.__dict__)

        list_dict_player_data["playerData"] = list_data

        json_string = json.dumps(list_dict_player_data)
        return json_string

@app.route("/", methods=['POST'])
def index_post():
    if(request.method == 'POST'):
        client_message = request.get_json()
        return jsonify({'post message': client_message})

@app.route("/", methods=['PUT'])
def index_put():
    if(request.method == 'PUT'):
        client_message = request.get_json()
        return jsonify({'put message': client_message})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
