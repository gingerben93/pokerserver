from enum import Enum
import random
import collections
import itertools

class Suit(Enum):
    Spades = 0
    Clubs = 1
    Hearts = 2
    Diamonds = 3

class Number(Enum):
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14

class HandType(Enum):
    StraightFlush = 8
    FourKind = 7
    FullHouse = 6
    Flush = 5
    Stright = 4
    ThreeKind = 3
    TwoPair = 2
    Pair = 1
    HighCard = 0

class Card:
    def __init__(self, value = None, suit = None):
        self.value = value
        self.suit = suit

    def __getitem__(self, value):
        return value

class Hand:
    def __init__(self, hand = None, type = None):
        self.hand = hand
        self.type = type

class Player:
    def __init__(self, name = None, top = None, middle = None, bottom = None):
        self.name = name
        self.top = top
        self.middle = middle
        self.bottom = bottom

class Player_data():
    def __init__(self, player_name = None,
                 top_cards_values = None,
                 top_cards_suits = None,
                 middle_cards_values = None,
                 middle_cards_suits = None,
                 bottom_cards_values = None,
                 bottom_cards_suits = None,
                 list_win_lost = None):
        self.player_name = player_name
        self.top_cards_values = top_cards_values
        self.top_cards_suits = top_cards_suits
        self.middle_cards_values = middle_cards_values
        self.middle_cards_suits = middle_cards_suits
        self.bottom_cards_values = bottom_cards_values
        self.bottom_cards_suit = bottom_cards_suits
        self.list_win_lost = list_win_lost

#using bubble sort temporaly
def sort_cards(list_cards):
    for i in range(len(list_cards)-1):
        for j in range(len(list_cards)-1):
            if list_cards[j].value.value < list_cards[j + 1].value.value:
                temp = list_cards[j]
                list_cards[j] = list_cards[j + 1]
                list_cards[j + 1] = temp
    return list_cards

#make 52 card deck
def make_deck():
    deck = []
    for x in range(0,4):
        for y in range(2,14):
            deck.append(Card(Number(y),Suit(x)))
    return deck

#random 5 community cards
def make_community_cards(deck):
    community_cards = []

    for x in range(0,5):
        current_card = deck[random.randint(0,len(deck)-1)]
        community_cards.append(current_card)
        deck.remove(current_card)

    return community_cards

#makes 7 random cards from deck and return them in hand class
def make_player_hand(deck):
    player_cards = []

    for x in range(0,7):
        current_card = deck[random.randint(0,len(deck)-1)]
        player_cards.append(current_card)
        deck.remove(current_card)

    player_hand = Hand(player_cards, None)

    return player_hand

#used for testing certain hands; might be used to load in number from data base
#takes two list of ints; should be 7 ints; indexes should match up; return hand
def make_player_hands(list_number, list_suit):
    #make player hand
    cards = []
    for i in range(len(list_number)):
        cards.append(Card(Number(list_number[i]), Suit(list_suit[i])))
    player_hand = Hand(cards, None)
    return player_hand

#takes two list of cards
def find_player_hand_types(community_cards, player_hand, player_name):
    top = [community_cards[0],
           community_cards[1],
           community_cards[2],
           community_cards[3],
           community_cards[4],
           player_hand.hand[0]]

    middle = [community_cards[0],
              community_cards[1],
              community_cards[2],
              community_cards[3],
              community_cards[4],
              player_hand.hand[1],
              player_hand.hand[2]]

    bottom1 = [community_cards[0],
              community_cards[1],
              community_cards[2],
              community_cards[3],
              community_cards[4],
              player_hand.hand[3],
              player_hand.hand[4]]

    bottom2 = [community_cards[0],
              community_cards[1],
              community_cards[2],
              community_cards[3],
              community_cards[4],
              player_hand.hand[3],
              player_hand.hand[5]]

    bottom3 = [community_cards[0],
              community_cards[1],
              community_cards[2],
              community_cards[3],
              community_cards[4],
              player_hand.hand[3],
              player_hand.hand[6]]

    bottom4 = [community_cards[0],
              community_cards[1],
              community_cards[2],
              community_cards[3],
              community_cards[4],
              player_hand.hand[4],
              player_hand.hand[5]]

    bottom5 = [community_cards[0],
              community_cards[1],
              community_cards[2],
              community_cards[3],
              community_cards[4],
              player_hand.hand[4],
              player_hand.hand[6]]

    bottom6 = [community_cards[0],
              community_cards[1],
              community_cards[2],
              community_cards[3],
              community_cards[4],
              player_hand.hand[5],
              player_hand.hand[6]]

    top_hand = what_is_hand(top)
    middle_hand = what_is_hand(middle)
    bottom_hand = get_bottom_hand(community_cards, player_hand.hand[3:])

    player_temp = Player(player_name, top_hand, middle_hand, bottom_hand)

    print(player_name)
    print("------------------------------")
    print(player_temp.top.type)
    for i in player_temp.top.hand:
        print(i.value, i.suit)
    print("------------------------------")
    print(player_temp.middle.type)
    for i in player_temp.middle.hand:
        print(i.value, i.suit)
    print("------------------------------")
    print(player_temp.bottom.type)
    for i in player_temp.bottom.hand:
        print(i.value, i.suit)
    return player_temp

def get_bottom_hand(community_cards, player_bottom_cards):
    community_card_combination = list(itertools.combinations(community_cards, 3))
    player_hand_combinations = list(itertools.combinations(player_bottom_cards, 2))

    all_combinations = []
    for x in community_card_combination:
        for y in player_hand_combinations:
            all_combinations.append(x+y)

    all_hands = []
    for x in all_combinations:
        all_hands.append(what_is_hand(x))

    return find_best_hand(all_hands)

def find_flush(list_cards):
    list_spades = []
    list_clubs = []
    list_hearts = []
    list_diamonds = []

    for i in range(len(list_cards)):
        if list_cards[i].suit == Suit.Spades:
            list_spades.append(list_cards[i])
        elif list_cards[i].suit == Suit.Clubs:
            list_clubs.append(list_cards[i])
        elif list_cards[i].suit == Suit.Hearts:
            list_hearts.append(list_cards[i])
        #diamonds
        else:
            list_diamonds.append(list_cards[i])

    if len(list_spades) >= 5:
        return list_spades
    elif len(list_clubs) >= 5:
        return list_clubs
    elif len(list_hearts) >= 5:
        return list_hearts
    elif len(list_diamonds) >= 5:
        return list_diamonds

    #if no flush found
    return None

def find_straight(list_cards):
    list_straight = []

    #use % to role over for check of 2 and ace
    for i in range(len(list_cards)):
        #check if no cards in straight and add first card
        if len(list_straight) == 0:
            list_straight.append(list_cards[i])

        if list_cards[i].value.value - 1 == list_cards[(i+1) % len(list_cards)].value.value:
            list_straight.append(list_cards[i+1])
        #if valuse is same do nothing
        elif list_cards[i].value.value == list_cards[(i+1) % len(list_cards)].value.value:
            continue
        #if last card is two and first card is ace
        elif list_cards[i].value.value == 2 and list_cards[0].value.value == 14:
            list_straight.append(list_cards[0])
        #clear straight if next value not == or 1 less
        else:
            list_straight = []

        if len(list_straight) >= 5:
            return list_straight

    #if no straight
    return None

#give list and number of dups you want: returns 5 cards
def find_duplicates(list_cards):

    list_list_dups = []
    list_dups = []

    list_dups.append(list_cards[0])

    for i in range(len(list_cards)-1):
        if list_cards[i].value.value == list_cards[i + 1].value.value:
            list_dups.append(list_cards[i + 1])
        else:
            list_list_dups.append(list_dups)
            list_dups = []
            list_dups.append(list_cards[i+1])

    list_list_dups.append(list_dups)
    return list_list_dups

def get_unique_list(list_cards_a, list_cards_b):
    for c in list_cards_a:
        if c in list_cards_b:
            list_cards_b.remove(c)
    return list_cards_b

#returns type of Hand
def what_is_hand(list_cards):
    make_list = list(list_cards)
    list_sorted_cards = sort_cards(make_list)

    list_flush = find_flush(list_sorted_cards)

    #check for royal list_flush
    if list_flush != None:
        list_straight_flush = find_straight(list_flush)
        if list_straight_flush != None:
            for i in list_straight_flush:
                return Hand(list_straight_flush, HandType.StraightFlush)

    list_list_dups = find_duplicates(list_sorted_cards)

    #check for  four of a kind
    list_dups_4kind = []
    for l in list_list_dups:
        if len(l) == 4:
            list_dups_4kind = l
            break

    if len(list_dups_4kind) == 4:
        #found 4 kind so add next highest card
        list_remainer_cards = get_unique_list(list_dups_4kind, list_sorted_cards)
        list_dups_4kind.append(list_remainer_cards[0])
        return Hand(list_dups_4kind, HandType.FourKind)

    #check for full house
    list_dups_3kind = []
    for l in list_list_dups:
        if len(l) == 3:
            list_dups_3kind = l
            break

    if len(list_dups_3kind) == 3:
        list_remainer_cards = get_unique_list(list_dups_3kind, list_sorted_cards)
        list_remainer_dups = find_duplicates(list_remainer_cards)

        list_dups_2kind = []
        for l in list_remainer_dups:
            if len(l) >= 2:
                list_dups_2kind = l
                break

        if len(list_dups_2kind) >= 2:
            list_fullhouse = list_dups_3kind + list_dups_2kind[:2]
            return Hand(list_fullhouse, HandType.FullHouse)

    #check for flush
    if list_flush != None:
        return Hand(list_flush[:5], HandType.Flush)

    #check for straight
    list_straight = find_straight(list_sorted_cards)
    if list_straight != None:
        return Hand(list_straight[:5], HandType.Stright)

    #check for 3 kind
    if len(list_dups_3kind) == 3:
        list_remainer_cards = get_unique_list(list_dups_3kind, list_sorted_cards)
        return Hand(list_dups_3kind + list_remainer_cards[:2], HandType.ThreeKind)

    #check for two pair
    list_dups_2kind_1 = []
    for l in list_list_dups:
        if len(l) == 2:
            list_dups_2kind_1 = l
            break

    if len(list_dups_2kind_1) == 2:
        list_remainer_cards = get_unique_list(list_dups_2kind_1, list_sorted_cards)
        list_remainer_dups = find_duplicates(list_remainer_cards)
        list_dups_2kind_2 = []

        for l in list_remainer_dups:
            if len(l) == 2:
                list_dups_2kind_2 = l
                break

        if len(list_dups_2kind_2) == 2:
            list_remainer_cards_2 = get_unique_list(list_dups_2kind_2, list_remainer_cards)
            list_2pair = list_dups_2kind_1 + list_dups_2kind_2 + list_remainer_cards_2[:1]
            return Hand(list_2pair, HandType.TwoPair)

    #check for pair

    if len(list_dups_2kind_1) == 2:
        list_remainer_cards = get_unique_list(list_dups_2kind_1, list_sorted_cards)
        return Hand(list_dups_2kind_1 + list_remainer_cards[:3], HandType.Pair)

    #check for high card
    return Hand(list_sorted_cards[:5], HandType.HighCard)

#takes list hands returns best hand
def find_best_hand(list_hands):
    best_hand = Hand(list_hands[0].hand, list_hands[0].type)
    for h in range(len(list_hands)):
        if best_hand.type.value < list_hands[h].type.value:
            best_hand = list_hands[h]
        elif best_hand.type.value == list_hands[h].type.value:
            for i in range(len(best_hand.hand)):
                if best_hand.hand[i].value.value < list_hands[h].hand[i].value.value:
                    best_hand = list_hands[h]
                    break
                if best_hand.hand[i].value.value > list_hands[h].hand[i].value.value:
                    break

    return best_hand

#compares player against super to check if player wins
def compare_against_super_player(player_hand, best_hand):
    win = True

    if player_hand.type == best_hand.type:
        for c in range(len(player_hand.hand)):
            if player_hand.hand[c].value.value < best_hand.hand[c].value.value:
                print("lose")
                win = False
                lose1 = "lose"
                return lose1
                break
        if win:
            print("win")
            win1 = "win"
            return win1
    else:
        print("lose")
        lose2 = "lose"
        return lose2

def find_winning_player(list_players):
    if list_players == None:
        print("something wnet so so wrong")

    list_top_hands = []
    list_middle_hands = []
    list_bottom_hands = []

    for p in list_players:
        list_top_hands.append(p.top)
        list_middle_hands.append(p.middle)
        list_bottom_hands.append(p.bottom)

    #make a 'super player'; has all winning hands
    best_top = find_best_hand(list_top_hands)
    best_middle = find_best_hand(list_middle_hands)
    best_bottom = find_best_hand(list_bottom_hands)

    list_player_win_lose = []
    for p in list_players:
        temp_win_lose = []
        temp_win_lose.append(compare_against_super_player(p.top, best_top))
        temp_win_lose.append(compare_against_super_player(p.middle, best_middle))
        temp_win_lose.append(compare_against_super_player(p.bottom, best_bottom))
        list_player_win_lose.append(temp_win_lose)

    #make player data object for returning to client
    list_player_data = []
    for i in range(0, len(list_players)):
        #set community cards on return from method
        top_value = []
        top_suit = []
        middle_value = []
        middle_suit = []
        bottom_value = []
        bottom_suit = []
        win_lose = []
        for x in range(0, len(list_players[i].top.hand)):
            top_value.append(list_players[i].top.hand[x].value.value)
            top_suit.append(list_players[i].top.hand[x].suit.value)
            middle_value.append(list_players[i].middle.hand[x].value.value)
            middle_suit.append(list_players[i].middle.hand[x].suit.value)
            bottom_value.append(list_players[i].bottom.hand[x].value.value)
            bottom_suit.append(list_players[i].bottom.hand[x].suit.value)

        new_player = Player_data(list_players[i].name,
                    top_value,
                    top_suit,
                    middle_value,
                    middle_suit,
                    bottom_value,
                    bottom_suit,
                    list_player_win_lose[i])

        list_player_data.append(new_player)
    return list_player_data

#deck = make_deck()
#community_cards = make_community_cards(deck)
#
#print("------------------------------")
#for i in community_cards:
#    print(i.value, i.suit)
#print("------------------------------")
#
##make players
#list_players = []
#
#player_hand1 = make_player_hand(deck)
#print("------------------------------")
#for i in player_hand1.hand:
#    print(i.value, i.suit)
#print("------------------------------")
#
#list_players.append(find_player_hand_types(community_cards, player_hand1, "player1"))
#
##test players
#find_winning_player(list_players)

