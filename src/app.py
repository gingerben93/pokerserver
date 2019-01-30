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

def player_data():
    def __init__(self,
                 player_name,
                 community_card_values,
                 community_card_suits,
                 top_cards_values,
                 top_cards_suits,
                 middle_cards_values,
                 middle_cards_suit,
                 bottom_cards_values,
                 bottom_cards_suits,
                 list_win_lost):
        self.player_name = player_name
        self.community_card_values = community_card_values
        self.community_card_suit = community_card_suits
        self.top_cards_values = top_cards_values
        self.top_cards_suits = top_cards_suits
        self.middle_cards_values = middle_cards_values
        self.middle_cards_suit = middle_cards_suit
        self.bottom_cards_values = bottom_cards_values
        self.bottom_cards_suit = bottom_cards_suits
        self.list_win_lost = list_win_lost

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
        #make second player for testing
        player2 = make_player_hand(deck)
        list_values_p2 = []
        list_suits_p2 = []
        for x in player2.hand:
            list_values_p2.append(x.value.value)
            list_suits_p2.append(x.suit.value)
        player_hand2 = make_player_hands(list_values_p2, list_suits_p2)
        player_hand1 = make_player_hands(list_values, list_suits)

        list_players.append(find_player_hand_types(test_community_cards, player_hand1, "player1"))
        list_players.append(find_player_hand_types(test_community_cards, player_hand2, "player2"))

        win_lose = []
        top_cards = []
        middle_cards = []
        bottom_cards = []
        temp_wrapper = find_winning_player(list_players)

        top_type = []
        middle_type = []
        bottom_type =[]

        win_lose.append(temp_wrapper[0])
        top_cards.append(temp_wrapper[1])
        middle_cards.append(temp_wrapper[2])
        bottom_cards.append(temp_wrapper[3])

        for player in list_players:
            jsonStringPlayers = jsonStringPlayers + player.name


        top_value = []
        top_suit = []
        for player in top_cards:
            for hand in player:
                top_type.append(hand.type.name)
                for c in hand.hand:
                    top_value.append(c.value.value)
                    top_suit.append(c.suit.value)

        middle_value = []
        middle_suit = []
        for player in middle_cards:
            for hand in player:
                middle_type.append(hand.type.name)
                for c in hand.hand:
                    middle_value.append(c.value.value)
                    middle_suit.append(c.suit.value)

        bottom_value = []
        bottom_suit = []
        for player in bottom_cards:
            for hand in player:
                bottom_type.append(hand.type.name)
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
        json_top_type = json.dumps(top_type)
        json_middle_cards_value = json.dumps(middle_value)
        json_middle_cards_suit = json.dumps(middle_suit)
        json_middle_type = json.dumps(middle_type)
        json_bottom_cards_value = json.dumps(bottom_value)
        json_bottom_cards_suit = json.dumps(bottom_suit)
        json_bottom_type = json.dumps(bottom_type)

        return jsonify({'values': json_value},
                        {'suits': json_suit},
                        {'win_lose': json_win_lose},
                        {'top_value': json_top_cards_value},
                        {'top_suit': json_top_cards_suit},
                        {'top_type': json_top_type},
                        {'middle_value': json_middle_cards_value},
                        {'middle_suit': json_middle_cards_suit},
                        {'middle_type': json_middle_type},
                        {'bottom_value': json_bottom_cards_value},
                        {'bottom_suit': json_bottom_cards_suit},
                        {'bottom_type': json_bottom_type})

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
