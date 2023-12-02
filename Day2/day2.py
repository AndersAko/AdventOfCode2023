from pathlib import Path


# '8 green, 6 blue, 20 red' -> { 'green':8, 'blue':6, 'red': 20 }
def cubes_in_game(string):
    tokens = string.split(' ')
    color = None
    cubes = {}
    for token in tokens:
        if token.startswith('green'):
            color = 'green'
            cubes[color] = number
        elif token.startswith('blue'):
            color = 'blue'
            cubes[color] = number
        elif token.startswith('red'):
            color = 'red'
            cubes[color] = number
        elif token != '':
            number = int(token)
    return cubes

def solve():
    with open(Path(__file__).with_name('input.txt'), 'r') as f:
        lines = f.read().split('\n')
        sum_possible = 0
        sum_power = 0
        for line in lines:
            game_id = int(line.split(' ')[1][:-1])
            fewest_cubes = {'blue': 0, 'red': 0, 'green': 0}
            possible = True
            for game in line.split(':')[1].split(';'):
                cubes = cubes_in_game(game)
                if cubes.get('red',0) <= 12 and cubes.get('green',0) <= 13 and cubes.get('blue',0) <= 14:
                    print (f'Game {game_id} is possible with {cubes}')
                else:
                    print(f"Game {game_id} is impossible with {cubes}")
                    possible = False
                for color in ['green', 'blue', 'red']:
                    fewest_cubes[color] = max(fewest_cubes[color], cubes.get(color,0))
            if possible: 
                sum_possible += game_id
                print (f'Game {game_id} is possible => {sum_possible}')
            power = fewest_cubes['blue'] * fewest_cubes['green'] * fewest_cubes['red']
            print (f"Game {game_id} => {fewest_cubes} => {power}")
            sum_power += power

        print (f"Total sum of game ids that are possible: {sum_possible}")
        print (f"Total power {sum_power}")

if __name__ == '__main__': solve()