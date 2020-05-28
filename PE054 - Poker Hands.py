file = open('poker.txt', 'r').read()
lines = file.split('\n')

suits_value = {
    'C': 0,
    'D': 1,
    'H': 2,
    'S': 3
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


def draw(ln):
    cards = ln.split(' ')
    hand_p1 = cards[0:5]
    hand_p2 = cards[5:10]
    return hand_p1, hand_p2


def highest_card(hand):
    values = get_values(hand)
    n = 15
    sum_cards = 0
    for i in range(len(values)):
        sum_cards += values[i]/n**(i+1)
    return True, sum_cards


def one_pair(hand):
    cards = n_cards(hand)
    for c in cards:
        if c[1] == 2:
            return True, c[0] + highest_card(hand)[1]
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
            return True, c[0] + highest_card(hand)[1]  # game, tiebreaker
    return False, 0


def straight(hand):
    values = get_values(hand)
    for i in range(0, 4):
        if values[i] - values[i + 1] != 1:
            return False, 0
    return True, highest_card(hand)[1]


def flush(hand):
    suit = hand[0][1]
    for card in hand:
        if card[1] != suit:
            return False, 0
    return True, highest_card(hand)[1]


def full_house(hand):
    pair, tb2 = one_pair(hand)
    three, tb3 = three_of_a_kind(hand)
    return pair and three, tb3+tb2/15


def four_of_a_kind(hand):
    cards = n_cards(hand)
    for c in cards:
        if c[1] == 4:
            return True, c[0]+highest_card(hand)[1]  # game, tiebreaker
    return False, 0


def straight_flush(hand):
    st = straight(hand)[0]
    fl = flush(hand)[0]
    tiebreaker = highest_card(hand)[1]
    return st and fl, tiebreaker  # game, tiebreaker


def royal_flush(hand):
    if not straight_flush(hand)[0]:
        return False, 0
    suit = hand[0][1]
    if 'A' + suit not in hand:
        return False, 0
    elif 'T' + suit not in hand:
        return False, 0
    else:
        return True, suits_value[hand[0][1]]/4  # game, tiebreaker


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


def evaluate(hand):
    r = {
        0: royal_flush(hand),
        1: straight_flush(hand),
        2: four_of_a_kind(hand),
        3: full_house(hand),
        4: flush(hand),
        5: straight(hand),
        6: three_of_a_kind(hand),
        7: two_pairs(hand),
        8: one_pair(hand),
        9: highest_card(hand)
    }
    return r


def compare_hands(p1, p2):
    p1 = evaluate(p1)
    p2 = evaluate(p2)
    i = 0
    while not p1[i][0] and not p2[i][0]:
        i += 1
    if p1[i][0] and p2[i][0]:
        return p1[i][1] > p2[i][1]
    else:
        return p1[i][0] > p2[i][0]


player1_wins = 0
player2_wins = 0
for line in lines:
    player1, player2 = draw(line)
    print(player1, player2)
    if compare_hands(player1, player2):
        player1_wins += 1
        print("player1")
    else:
        player2_wins += 1
        print("player2")
print(player1_wins)
print(player2_wins)

