from collections import OrderedDict

file = open('poker.txt', 'r')
test_line = "4D AH KD 9H KS TC KC QC AC JC"

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


def straight(hand):
    values = []
    for card in hand:
        c = card[0]
        c = cards_value[c]
        values.append(c)
    values.sort()
    print(values)
    for i in range(0, 4):
        if values[i] != (values[i + 1] - 1):
            return False
    return True


def flush(hand):
    # check if they are all the same suit
    suit = hand[0][1]
    for card in hand:
        if card[1] != suit:
            return False
    return True


def straight_flush(hand):
    return straight(hand) and flush(hand)


def royal_flush(hand):
    if not straight_flush(hand):
        return False
    suit = hand[0][1]
    if 'A' + suit not in hand:
        return False
    elif 'T' + suit not in hand:
        return False
    else:
        return True


def n_kind(n, hand):
    values = []
    for card in hand:
        c = card[0]
        c = cards_value[c]
        values.append(c)
    values.sort()
    for i in range(len(hand) - n + 1):
        r = True
        for j in range(n - 1):
            if values[i + j] != values[i + j + 1]:
                r = False
        if r:
            return True
    return False

def two_pairs():



a, b = draw(test_line)
print(n_kind(3, a))
