from collections import OrderedDict

file = open('poker.txt', 'r')
test_line = "TS QH 6C 8H TH 5H 3C 3H 9C 9D"

suits_value = {
    'C': 1,
    'D': 2,
    'H': 3,
    'S': 4
}

cards_value = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}


def draw(line):
    cards = line.split(' ')
    hand_p1 = cards[0:5]
    hand_p2 = cards[5:10]
    return hand_p1, hand_p2


def highest_card(hand):
    values = get_values(hand)
    n = 15
    sum_cards = 0
    for i in range(len(values)):
        sum_cards += values[i]/n**(i+1)
    return sum_cards, 0


def one_pair(hand):
    cards = n_cards(hand)
    for c in cards:
        if c[1] == 2:
            return True, c[0] + highest_card(hand)[0]
    return False, 0


def two_pairs(hand):
    cards = n_cards(hand)
    pairs = 0
    tiebreaker = 0
    for c in cards:
        if c[1] == 2:
            tiebreaker += c[0]/15**pairs
            pairs += 1
    return pairs == 2, tiebreaker


def three_of_a_kind(hand):
    cards = n_cards(hand)
    for c in cards:
        if c[1] == 3:
            return True, c[0] + highest_card(hand)[0]  # game, tiebreaker
    return False, 0


def straight(hand):
    values = get_values(hand)
    for i in range(0, 4):
        if values[i] != (values[i + 1] - 1):
            return False, 0
    return True, highest_card(hand)[0]


def flush(hand):
    # check if they are all the same suit
    suit = hand[0][1]
    for card in hand:
        if card[1] != suit:
            return False, 0
    return True, highest_card(hand)[0]


def full_house(hand):
    pair, tb2 = one_pair(hand)
    three, tb3 = three_of_a_kind(hand)
    return pair and three, tb3


def four_of_a_kind(hand):
    cards = n_cards(hand)
    for c in cards:
        if c[1] == 4:
            return True, c[0]  # game, tiebreaker
    return False, 0


def straight_flush(hand):
    return straight(hand) and flush(hand), highest_card(hand)[0]  # game, tiebreaker


def royal_flush(hand):
    if not straight_flush(hand):
        return False, 0
    suit = hand[0][1]
    if 'A' + suit not in hand:
        return False, 0
    elif 'T' + suit not in hand:
        return False, 0
    else:
        return True, 0  # game, tiebreaker


def get_values(hand):
    values = []
    for card in hand:
        c = card[0]
        c = cards_value[c]
        values.append(c)
    values.sort(reverse=True)
    return values


def n_cards(hand):
    values = get_values(hand)
    cards = []
    for v in values:
        if not cards:
            cards.append([v, 1])
        elif v == cards[-1][0]:
            cards[-1][1] += 1
        else:
            cards.append([v, 1])
    return cards


def compare_hands(p1, p2):
    


a, b = draw(test_line)
print(b)
print(two_pairs(b))
