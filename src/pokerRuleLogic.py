from enum import Enum

class Suit(Enum):
    Spades = 0
    Clubs = 1
    Hearts = 2
    Diamonds = 3

class Number(Enum):
    Two = 0
    Three = 1
    Four = 2
    Five = 3
    Six = 4
    Seven = 5
    Eight = 6
    Nine = 7
    Ten = 8
    Jack = 9
    Queen = 10
    King = 11
    Ace = 12

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

#using bubble sort temporaly
def sort_cards(list_cards):
    for i in range(len(list_cards)-1):
        for j in range(len(list_cards)-1):
            if list_cards[j].value.value < list_cards[j + 1].value.value:
                temp = list_cards[j]
                list_cards[j] = list_cards[j + 1]
                list_cards[j + 1] = temp
    return list_cards

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
    bottom_hand1 = find_Omaha_hand(bottom1)
    bottom_hand2 = find_Omaha_hand(bottom2)
    bottom_hand3 = find_Omaha_hand(bottom3)
    bottom_hand4 = find_Omaha_hand(bottom4)
    bottom_hand5 = find_Omaha_hand(bottom5)
    bottom_hand6 = find_Omaha_hand(bottom6)

    list_bottom_hands  = []
    list_bottom_hands.append(bottom_hand1)
    list_bottom_hands.append(bottom_hand2)
    list_bottom_hands.append(bottom_hand3)
    list_bottom_hands.append(bottom_hand4)
    list_bottom_hands.append(bottom_hand5)
    list_bottom_hands.append(bottom_hand6)

    best_hand_bottom = find_best_hand(list_bottom_hands)

    player_temp = Player(player_name, top_hand, middle_hand, best_hand_bottom)

    print(player_name)
    print("------------------------------")
    for i in player_temp.top.hand:
        print(i.value, i.suit)
    print("------------------------------")
    for i in player_temp.middle.hand:
        print(i.value, i.suit)
    print("------------------------------")
    for i in player_temp.bottom.hand:
        print(i.value, i.suit)
    return player_temp

def find_Omaha_hand(list_cards):
    hand1 = [list_cards[0], list_cards[1], list_cards[2], list_cards[-1], list_cards[-2]]
    hand2 = [list_cards[0], list_cards[1], list_cards[3], list_cards[-1], list_cards[-2]]
    hand3 = [list_cards[0], list_cards[1], list_cards[4], list_cards[-1], list_cards[-2]]
    hand4 = [list_cards[0], list_cards[2], list_cards[3], list_cards[-1], list_cards[-2]]
    hand5 = [list_cards[0], list_cards[2], list_cards[4], list_cards[-1], list_cards[-2]]
    hand6 = [list_cards[0], list_cards[3], list_cards[4], list_cards[-1], list_cards[-2]]
    hand7 = [list_cards[1], list_cards[2], list_cards[3], list_cards[-1], list_cards[-2]]
    hand8 = [list_cards[1], list_cards[2], list_cards[4], list_cards[-1], list_cards[-2]]
    hand9 = [list_cards[1], list_cards[3], list_cards[4], list_cards[-1], list_cards[-2]]
    hand10 = [list_cards[2], list_cards[3], list_cards[4], list_cards[-1], list_cards[-2]]

    list_hands = []

    list_hands.append(what_is_hand(hand1))
    list_hands.append(what_is_hand(hand2))
    list_hands.append(what_is_hand(hand3))
    list_hands.append(what_is_hand(hand4))
    list_hands.append(what_is_hand(hand5))
    list_hands.append(what_is_hand(hand6))
    list_hands.append(what_is_hand(hand7))
    list_hands.append(what_is_hand(hand8))
    list_hands.append(what_is_hand(hand9))
    list_hands.append(what_is_hand(hand10))

    for h in list_hands:
        print("------------------------------")
        for c in h.hand:
            print(c.value, c.suit)

    print("find OH hand")
    list_best_hand = find_best_hand(list_hands)

    return list_best_hand


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
        elif list_cards[i].value.value == 0 and list_cards[0].value.value == 12:
            list_straight.append(list_cards[0])
        #clear straight if next value not == or 1 less
        else:
            list_straight = []

        if len(list_straight) >= 5:
            return list_straight

    #if no straight
    return None

#give list and number of dups you want: returns 5 cards
def find_duplicates(list_cards, num_dup):
    cur_num_dups = 0
    list_dups = []
    for x in list_cards:
        for y in list_cards:
            if x.value == y.value:
                list_dups.append(y)
                cur_num_dups += 1
            if cur_num_dups == num_dup:
                return list_dups
        list_dups = []
        cur_num_dups = 0
    return None

def get_unique_list(list_cards_a, list_cards_b):
    for c in list_cards_a:
        if c in list_cards_b:
            list_cards_b.remove(c)
    return list_cards_b

#returns type of Hand
def what_is_hand(list_cards):
    list_cards = sort_cards(list_cards)

    list_flush = find_flush(list_cards)

    #check for royal list_flush
    if list_flush != None:
        list_straight_flush = find_straight(list_flush)
        if list_straight_flush != None:
            for i in list_straight_flush:
                return Hand(list_straight_flush, HandType.StraightFlush)

    #check for  four of a kind
    list_dups_4kind = find_duplicates(list_cards, 4)
    if list_dups_4kind != None:
        #found 4 kind so add next highest card
        list_remainer_cards = get_unique_list(list_dups_4kind, list_cards)
        list_dups_4kind.append(list_remainer_cards[0])
        return Hand(list_dups_4kind, HandType.FourKind)

    #check for full house
    list_dups_3kind = find_duplicates(list_cards, 3)
    if list_dups_3kind != None:
        list_remainer_cards = get_unique_list(list_dups_3kind, list_cards)
        list_dups_2kind = find_duplicates(list_remainer_cards, 2)
        if list_dups_2kind != None:
            list_fullhouse = list_dups_3kind + list_dups_2kind
            return Hand(list_fullhouse, HandType.FullHouse)

    #check for flush
    if list_flush != None:
        return Hand(list_flush[:5], HandType.Flush)

    #check for straight
    list_straight = find_straight(list_cards)
    if list_straight != None:
        return Hand(list_straight[:5], HandType.Stright)

    #check for 3 kind
    if list_dups_3kind != None:
        list_remainer_cards = get_unique_list(list_dups_3kind, list_cards)
        return Hand(list_dups_3kind + list_remainer_cards[:2], HandType.Stright)

    #check for two pair
    list_dups_2kind_1 = find_duplicates(list_cards, 2)
    if list_dups_2kind_1 != None:
        list_remainer_cards = get_unique_list(list_dups_2kind_1, list_cards)
        list_dups_2kind_2 = find_duplicates(list_remainer_cards, 2)
        if list_dups_2kind_2 != None:
            list_remainer_cards_2 = get_unique_list(list_dups_2kind_2, list_remainer_cards)
            list_2pair = list_dups_2kind_1 + list_dups_2kind_2 + list_remainer_cards_2[:1]
            return Hand(list_2pair, HandType.TwoPair)

    #check for pair
    if list_dups_2kind_1 != None:
        list_remainer_cards = get_unique_list(list_dups_2kind_1, list_cards)
        return Hand(list_dups_2kind_1 + list_remainer_cards[:3], HandType.Pair)

    #check for high card
    return Hand(list_cards[:5], HandType.HighCard)

#takes list hands returns best hand
def find_best_hand(list_hands):
    best_hand = Hand(list_hands[0].hand, list_hands[0].type)
    for h in range(len(list_hands)):
        if best_hand == None:
            best_hand = [list_hands[h]]
        elif best_hand.type.value < list_hands[h].type.value:
            best_hand = list_hands[h]
        elif best_hand.type.value == list_hands[h].type.value:
            for i in range(len(best_hand.hand)):
                if best_hand.hand[i].value.value < list_hands[h].hand[i].value.value:
                    best_hand = list_hands[h]

    print(best_hand.type)
    return best_hand

def compare_against_super_player(player_hand, best_hand):

    win = True

    if player_hand.type == best_hand.type:
        for c in range(len(player_hand.hand)):
            if player_hand.hand[c].value.value < best_hand.hand[c].value.value:
                print("lose")
                win = False
                break
        if win:
            print("win")
    else:
        print("lose")

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

    for p in list_players:
        compare_against_super_player(p.top, best_top)
        compare_against_super_player(p.middle, best_middle)
        compare_against_super_player(p.bottom, best_bottom)

#for testing make community cards
test_community_cards = []
test_community_cards.append(Card(Number(7),Suit(0)))
test_community_cards.append(Card(Number(7),Suit(1)))
test_community_cards.append(Card(Number(6),Suit(2)))
test_community_cards.append(Card(Number(6),Suit(1)))
test_community_cards.append(Card(Number(5),Suit(1)))

#make players
list_players = []
player_hand1 = make_player_hands([5,2,2,7,6,2,2],[2,2,2,2,2,2,2])
player_hand2 = make_player_hands([1,3,3,7,5,3,3],[3,3,3,3,3,3,3])

list_players.append(find_player_hand_types(test_community_cards, player_hand1, "player1"))
list_players.append(find_player_hand_types(test_community_cards, player_hand2, "player2"))

#test players
find_winning_player(list_players)

