from pathlib import Path

def solve():
    with open(Path(__file__).with_name('input.txt'), 'r') as f:
        lines = f.read().split('\n')
        found_part_start = set()
        parts = []
        sum_gears = 0
        for line in range(len(lines)):
            for char in range(len(lines[line])):
                if lines[line][char].isdigit() or lines[line][char] == '.': 
                    continue
                # symbol
                part_nos = [(line + l, char + c) for l in [-1, 0, 1] for c in [-1, 0, 1] 
                            if line + l >= 0 and line + l < len(lines) and 
                               char + c >= 0 and char + c < len(lines[line + l]) and 
                               lines[line + l][char + c].isdigit()]
                if len(part_nos) > 0:
                    part_nos_for_this = []
                    print(f"part number at: {part_nos}")
                    for l,c in part_nos:
                        # start of part_no
                        start = c
                        while start > 0 and lines[l][start-1].isdigit():
                            start-=1

                        end = c                        
                        while end < len(lines[l])-1 and lines[l][end+1].isdigit():
                            end+=1
                        if (l,start) not in found_part_start:
                            part_nos_for_this.append(lines[l][start:end+1])
                        found_part_start.add((l,start))
                    parts.extend(part_nos_for_this)
                    if lines[line][char] == '*' and len(part_nos_for_this) == 2: 
                        gear_ratio = int(part_nos_for_this[0]) * int(part_nos_for_this[1]) 
                        print (f"Gear ratio: {part_nos_for_this[0]} * {part_nos_for_this[1]} = {gear_ratio}")
                        sum_gears += gear_ratio

        print (f"Parts: {parts}")
        print (f"=> Sum: {sum(int(p) for p in parts)}")
        print (f"Sum of gear ratios: {sum_gears}")

if __name__ == '__main__': solve()