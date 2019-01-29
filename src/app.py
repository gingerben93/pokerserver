from flask import Flask, jsonify, request
import json
import logging
#import pokerRuleLogic
from pokerRuleLogic import make_deck
from pokerRuleLogic import make_player_hand
from pokerRuleLogic import make_player_hands
from pokerRuleLogic import find_player_hand_types
from pokerRuleLogic import find_winning_player
from pokerRuleLogic import make_community_cards

log = logging.getLogger(__name__)

app = Flask(__name__)

deck = []

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

        json_value = json.dumps(cards_value)
        json_suit = json.dumps(cards_suit)
        return jsonify({'values': json_value}, {'suits': json_suit})


@app.route("/lock_in_cards", methods=['POST'])
def lock_in_cards():
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
        global deck
        test_community_cards = make_community_cards(deck)
        player_hand1 = make_player_hands(list_values, list_suits)

        list_players.append(find_player_hand_types(test_community_cards, player_hand1, "player1"))

        win_lose = []
        top_cards = []
        middle_cards = []
        bottom_cards = []
        temp_wrapper = find_winning_player(list_players)

        win_lose.append(temp_wrapper[0])
        top_cards.append(temp_wrapper[1])
        middle_cards.append(temp_wrapper[2])
        bottom_cards.append(temp_wrapper[3])

        for p in win_lose:
            for x in p:
                print(x)

        top_value = []
        top_suit = []
        for player in top_cards:
            for hand in player:
                for c in hand.hand:
                    top_value.append(c.value.value)
                    top_suit.append(c.suit.value)

        middle_value = []
        middle_suit = []
        for player in middle_cards:
            for hand in player:
                for c in hand.hand:
                    middle_value.append(c.value.value)
                    middle_suit.append(c.suit.value)

        bottom_value = []
        bottom_suit = []
        for player in bottom_cards:
            for hand in player:
                for c in hand.hand:
                    bottom_value.append(c.value.value)
                    bottom_suit.append(c.suit.value)

        cards_value = []
        cards_suit = []

        for c in test_community_cards:
            cards_value.append(c.value.value)
            cards_suit.append(c.suit.value)

        json_value = json.dumps(cards_value)
        json_suit = json.dumps(cards_suit)
        json_win_lose = json.dumps(win_lose)
        json_top_cards_value = json.dumps(top_value)
        json_top_cards_suit = json.dumps(top_suit)
        json_middle_cards_value = json.dumps(middle_value)
        json_middle_cards_suit = json.dumps(middle_suit)
        json_bottom_cards_value = json.dumps(bottom_value)
        json_bottom_cards_suit = json.dumps(bottom_suit)

        return jsonify({'values': json_value},
                        {'suits': json_suit},
                        {'win_lose': json_win_lose},
                        {'top_value': json_top_cards_value},
                        {'top_suit': json_top_cards_suit},
                        {'middle_value': json_middle_cards_value},
                        {'middle_suit': json_middle_cards_suit},
                        {'bottom_value': json_bottom_cards_value},
                        {'bottom_suit': json_bottom_cards_suit})

@app.route("/", methods=['POST'])
def index_post():
    if(request.method == 'POST'):
        #list_values = []
        #list_suits = []
        client_message = request.get_json()

        #for row in client_message:
        #    row_json = client_message[row]
        #    print(row_json)
        #    for card in row_json:
        #        list_values.append((int)(client_message[row][card]['value']))
        #        list_suits.append((int)(client_message[row][card]['suit']))

        #list_players = []
        #test_community_cards = make_community_cards()
        #player_hand1 = make_player_hands(list_values, list_suits)

        #list_players.append(find_player_hand_types(test_community_cards, player_hand1, "player1"))

        #find_winning_player(list_players)

        return jsonify({'post message': client_message})

@app.route("/", methods=['PUT'])
def index_put():
    if(request.method == 'PUT'):
        client_message = request.get_json()
        return jsonify({'put message': client_message})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
