
import re
from pathlib import Path



def number(string):
    digits = [d for d in string if d.isdigit()]
    num_digits = len(digits)
    result = digits[0] + digits[num_digits-1] if num_digits > 0 else ''
    return result

def convert(number: str):
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    if number.isdigit(): return number
    return str(next(i+1 for i in range(9) if numbers[i]==number))

def number2(string):
    first_number_re = re.compile(r"\d|one|two|three|four|five|six|seven|eight|nine")
    last_number_re = re.compile(r"(\d|one|two|three|four|five|six|seven|eight|nine)(?!(\d|one|two|three|four|five|six|seven|eight|nine))")
    first = first_number_re.search(string)
    last = last_number_re.search(string)
    digits = numbers_re.findall(string)
    if len(digits) == 0: return None 
    converted = [ convert(d) for d in digits]
    result = convert(digits[0]) + convert(digits[len(digits)-1])
    return result

def find_number(string, reverse):
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in reversed(range(len(string))) if reverse else range(len(string)):
        if string[i].isdigit(): return string[i]
        for num in range(len(numbers)):
            if string[i:].startswith(numbers[num]):
                return str(num+1)

def cal_number(string):
    num = find_number(string, False) + find_number(string, True)
    return num

def solve():
    with open(Path(__file__).with_name('input.txt'), 'r') as f:
        lines = f.read().split('\n')
        sum = 0
        for line in lines:
            num = cal_number(line)
            print(line, ' => ', num)
            sum += int(num)

        print("Total sum: ", sum)

if __name__ == '__main__': solve()