from pathlib import Path

def solve():
    with open(Path(__file__).with_name('input.txt'), 'r') as f:
        lines = f.read().split('\n')
        cards = [1 for _ in lines]
        total_score = 0 
        for line in lines:
            parts = line.split(':')
            card_no = int([c for c in parts[0].split(' ') if c != ''][1])
            winning_nos = [int(n) for n in parts[1].split('|')[0].strip().split(' ') if n != '']
            my_nos = [int(n) for n in line.split(':')[1].split('|')[1].strip().split(' ') if n != '']
            matching = [no for no in my_nos if no in winning_nos]
            score = 2**(len(matching)-1) if len(matching) > 0 else 0

            print (f"{cards[card_no-1]} * Card {card_no} Winning: {winning_nos} My: {my_nos} => {matching} {score}")            
            total_score += score

            for extra in range(card_no+1, card_no+1+len(matching)):
                if extra <= len(lines): cards[extra-1] += cards[card_no-1]

        print (f"=> Part 1 score: {total_score}")
        print (f"Cards: {cards} => {sum(cards)}")

if __name__ == '__main__': solve()