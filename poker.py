import random

# 生成一副牌
_poker_value = ['3', '4', '5', '6', '7',
                '8', '9', '0', 'J', 'Q', 'K', 'A', '2']
_poker_suit = ['spades', 'hearts', 'clubs', 'diamonds']
_pokers = []
for i in _poker_suit:
    for j in _poker_value:
        _pokers.append(j + i)
_pokers += ['Bjoker', 'Rjoker']


class Poker(object):
    def __init__(self):
        self.pokers = _pokers

    def xi(self):
        random.shuffle(self.pokers)
        self.pokers = self.pokers[::-1]
        random.shuffle(self.pokers)

    def fa(self):
        self.xi()
        L1 = []
        L2 = []
        L3 = []
        L4 = self.pokers[-3:]
        for i in range(0, 51, 3):
            L1.append(self.pokers[i])
            L2.append(self.pokers[i + 1])
            L3.append(self.pokers[i + 2])
        return self.mapai(L1), self.mapai(L2), self.mapai(L3), self.mapai(L4)

    def mapai(self, pokers):
        tmp_value = _poker_value
        tmp_suit = _poker_suit
        tmp_value += ['B', 'R']
        tmp_suit += ['joker']
        if isinstance(pokers[0], str):
            pokers = sorted(pokers, key=lambda x: [tmp_value.index(
                        x[0]),tmp_suit.index(x[1:])], reverse=True)
        else:
            pokers = sorted(pokers, key=lambda x: [tmp_value.index(
                        x.name[0]),tmp_suit.index(x.name[1:])])
        return pokers
