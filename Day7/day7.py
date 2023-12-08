from enum import IntEnum, auto, Enum
from pathlib import Path

class HandType(IntEnum):
    HighCard = auto()
    Pair = auto()
    TwoPair = auto()
    Three = auto()
    FullHouse = auto()
    Four = auto()
    Five = auto()

CARD_LABELS = list("23456789TJQKA")
CARD_LABELS2 = list("J23456789TQKA")

def hand_type(cards:str) -> HandType:
    counts = []
    for card in cards:
        counts.append(len([1 for c in cards if c == card]))

    if counts[0] == 5:
        return HandType.Five
    if any(c == 4 for c in counts):
        return HandType.Four
    if any(c == 3 for c in counts) and any(c == 2 for c in counts):
        return HandType.FullHouse
    if any(c == 3 for c in counts):
        return HandType.Three
    if len([1 for c in counts if c == 2]) == 4:
        return HandType.TwoPair
    if any(c == 2 for c in counts):
        return HandType.Pair
    return HandType.HighCard

def hand_type2(cards:str) -> HandType:
    counts = []
    for card in cards:
        counts.append(len([1 for c in cards if c == card or c == 'J']))

    if any(c == 5 for c in counts):
        return HandType.Five
    if any(c == 4 for c in counts):
        return HandType.Four
    if 'J' in cards and hand_type(cards) is HandType.TwoPair or hand_type(cards) is HandType.FullHouse:
        return HandType.FullHouse
    if any(c == 3 for c in counts):
        return HandType.Three
    if len([1 for c in counts if c == 2]) == 4 and 'J' not in cards:
        return HandType.TwoPair
    if any(c == 2 for c in counts):
        return HandType.Pair
    return HandType.HighCard

def solve():
    with open(Path(__file__).with_name('input.txt'), 'r') as f:
        lines = f.read().split('\n')
        # Part 1
        lines.sort(key = lambda h: (hand_type(h.split(' ')[0]), [CARD_LABELS.index(c) for c in h.split(' ')[0]] ))
        print (lines)
        winnings = 0
        for i in range(len(lines)):
            bid = int(lines[i].split(' ')[1])
            winnings += bid * (i + 1)
            print (i, lines[i], bid, bid * (i + 1))
        print (winnings)

        # Part 2
        lines.sort(key = lambda h: (hand_type2(h.split(' ')[0]), [CARD_LABELS2.index(c) for c in h.split(' ')[0]] ))
        winnings = 0
        for i in range(len(lines)):
            bid = int(lines[i].split(' ')[1])
            cards = lines[i].split(' ')[0]
            winnings += bid * (i + 1)
            print (i, lines[i], hand_type2(cards))
        print (winnings)

if __name__ == '__main__': solve()