from collections import namedtuple
from pathlib import Path

MapRange = namedtuple("MapRange", "dest, source, length")

def convert(source:int, conversions:list[MapRange]) -> int:
    for conversion in conversions:
        if source >= conversion.source and source < conversion.source + conversion.length:
            return source + conversion.dest -conversion.source 
    return source

def convert_range(source: list[int], conversions: list[MapRange]) -> list[int]:
    result = []
    for pair in range(len(source)//2):
        ptr = source[pair*2]
        pair_len = source[pair*2 + 1]
        for conversion in conversions:
            if ptr < conversion.source:
                new_range_len = min(conversion.source - ptr, pair_len) 
                result.extend([ptr, new_range_len])
                pair_len -= new_range_len
                ptr = conversion.source
                if pair_len == 0: break
            if ptr >= conversion.source and ptr < conversion.source + conversion.length:
                new_range_len = min(conversion.source + conversion.length - ptr, pair_len) 
                result.extend([ptr + conversion.dest - conversion.source, new_range_len])
                ptr += new_range_len
                pair_len -= new_range_len
                if pair_len == 0: break
        else:
            result.extend([ptr, pair_len])
    return result   

def solve():
    with open(Path(__file__).with_name('input.txt'), 'r') as f:
        lines = f.read().split('\n')
        seeds = [int(s) for s in lines[0].split(':')[1].strip().split(' ') if s != '']

        print (f"Seeds: {seeds}")

        # dict {"from" : (to, list[MapRange])}
        conversions = dict()
        from_type = ""
        to_type = ""
        for line in lines[2:]:
            if line.endswith('map:'):
                from_to = line.split(' ')[0].split('-')
                from_type = from_to[0]
                to_type = from_to[2]
                conversions[from_type] = (to_type, [])
            elif line == '': 
                continue
            else:
                digits = [int(d) for d in line.split(' ') if d !='']
                conversions[from_type][1].append(MapRange(digits[0], digits[1], digits[2]))
            # if line = xx-to-yy map: Set to and from, create empty MapRange list
            # if empty: skip
            # if digits: Split on ' ',  append to MapRange list
            pass
        for c in conversions.values():
            c[1].sort(key=lambda x : x.source)

        # Part 1
        state = "seed"
        inventory = seeds
        while state != "location":
            # find "to" state 
            # Convert all seeds in inventory
            inventory = [convert(x, conversions[state][1]) for x in inventory]
            state = conversions[state][0]
            print (f"Inventory: {state} {inventory}")

        print (f"Lowest location: {min(inventory)}")

        # Part 2

        print ("\nPart2")
        state = "seed"
        inventory = seeds
        print (f"Seeds: {seeds}")
        while state != "location":
            inventory = convert_range(inventory, conversions[state][1])
            state = conversions[state][0]
            print (f"Inventory: {state} {inventory}")

        print (f"Lowest location: {min(inventory[i*2] for i in range(len(inventory)//2))}")

if __name__ == '__main__': solve()