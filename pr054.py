class Card:
    def __init__(self, card):
        self.value2number = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12,
                             'K': 13, 'A': 14}

        self.value = self.value2number[card[0]]
        self.suit = card[1]

    def __str__(self):
        return f'value: {self.value} \n suit: {self.suit}'


class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.values = [card.value for card in self.cards]
        self.suits = [card.suit for card in self.cards]
        self.freq_dict = self.frequency(self.values)
        self.freq = list(self.frequency(self.values).values())

    @staticmethod
    def frequency(arr):
        d_ = dict()
        for a in arr:
            if a not in d_:
                d_[a] = 0
            d_[a] += 1
        return d_

    def get_highest_card(self):
        return max(self.values)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(card.__str__())
        return '\n===\n'.join(res)

    def is_flush(self):
        if len(set(self.suits)) == 1:
            highest_card = max(self.values)
            return True, highest_card, None
        else:
            return False, None

    def is_straight(self):
        t = sorted(self.values)
        diffs = [j - i for i, j in zip(t[:-1], t[1:])]
        if len(set(diffs)) == 1 and 1 in diffs:  # not taken into account A 2 3 4 5
            highest_card = max(self.values)
            return True, highest_card, None
        else:
            return False, None

    def is_straight_flush(self):
        return self.is_straight()[0] and self.is_flush()[0], max(self.values), max(self.values)

    def is_four_of_a_king(self):
        if 4 in self.freq:
            res = True
        else:
            res = False
        if res:
            highest_card = max([i for i in self.values if self.freq_dict[i] == 4])
            highest_card_ = max([i for i in self.values if self.freq_dict[i] != 4])
            return True, highest_card, highest_card_
        else:
            return False, None

    def is_full_house(self):
        if 3 in self.freq and 2 in self.freq:
            res = True
        else:
            res = False
        if res:
            highest_card = max([i for i in self.values if self.freq_dict[i] == 3])
            return True, highest_card, None
        else:
            return False, None

    def is_three_of_a_king(self):
        if 3 in self.freq and 2 not in self.freq:
            res = True
        else:
            res = False
        if res:
            highest_card = max([i for i in self.values if self.freq_dict[i] == 3])
            highest_card_ = max([i for i in self.values if self.freq_dict[i] != 3])
            return True, highest_card, highest_card_
        else:
            return False, None

    def is_two_pairs(self):
        if self.freq.count(2) == 2:
            res = True
        else:
            res = False
        if res:
            highest_card = max([i for i in self.values if self.freq_dict[i] == 2])
            highest_card_ = max([i for i in self.values if self.freq_dict[i] != 2])
            return True, highest_card, highest_card_
        else:
            return False, None

    def is_one_pair(self):
        if 2 in self.freq:
            res = True
        else:
            res = False
        if res:
            highest_card = max([i for i in self.values if self.freq_dict[i] == 2])
            highest_card_ = max([i for i in self.values if self.freq_dict[i] != 2])
            return True, highest_card, highest_card_
        else:
            return False, None

    @property
    def score(self):
        if self.is_straight_flush()[0]:
            return 0, self.is_straight_flush()[1], self.is_straight_flush()[2]
        elif self.is_four_of_a_king()[0]:
            return 1, self.is_four_of_a_king()[1], self.is_four_of_a_king()[2]
        elif self.is_full_house()[0]:
            return 2, self.is_full_house()[1], self.is_full_house()[2]
        elif self.is_flush()[0]:
            return 3, self.is_flush()[1], self.is_flush()[2]
        elif self.is_straight()[0]:
            return 4, self.is_straight()[1], self.is_straight()[2]
        elif self.is_three_of_a_king()[0]:
            return 5, self.is_three_of_a_king()[1], self.is_three_of_a_king()[2]
        elif self.is_two_pairs()[0]:
            return 6, self.is_two_pairs()[1], self.is_two_pairs()[2]
        elif self.is_one_pair()[0]:
            return 7, self.is_one_pair()[1], self.is_one_pair()[2]
        else:
            return 8, self.get_highest_card()


f = open('p054_poker.txt', 'r')
s = f.read()

hands = s.split('\n')
hands = hands[:-1]

res = 0

for hand_pair in hands:

    hand1 = hand_pair[:14]
    hand2 = hand_pair[15:]

    cards = list()
    for card in hand1.split(' '):
        card_ = Card(card)
        cards.append(card_)
    hand1 = Hand(cards)

    cards = list()
    for card in hand2.split(' '):
        card_ = Card(card)
        cards.append(card_)

    hand2 = Hand(cards)
    if hand1.score[0] < hand2.score[0]:
        res += 1
    elif hand1.score[0] > hand2.score[0]:
        pass
    else:
        if hand1.score[1] > hand2.score[1]:
            res += 1
        elif hand1.score[1] < hand2.score[1]:
            pass
        else:
            if hand1.score[2] > hand2.score[2]:
                res += 1

print(res)
