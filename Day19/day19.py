from copy import deepcopy
from typing import NamedTuple, Tuple
from enum import IntEnum, auto, Enum
import re
from typing import List, Dict
from pathlib import Path

class RuleSet(NamedTuple):
    category: str
    condition: str
    value: int
    destination: str

def process_part(part:dict, current_workflow_name:str, workflows:dict) -> bool:
    if current_workflow_name == 'A':
        return True
    if current_workflow_name == 'R':
        return False
    
    current_workflow = workflows[current_workflow_name]
    for rule in current_workflow:
        if (rule.condition == '>' and part[rule.category] > rule.value or 
            rule.condition == '<' and part[rule.category] < rule.value or
            rule.condition == 'default'):
            return process_part(part, rule.destination, workflows)
    assert False

def parse(input:str):
    lines = (l for l in input.split('\n'))
    parts : List[Dict] = [] # Each part is a dict of property:value
    workflows = dict()  # workflow name: list of rules as RuleSet, eg 's>2770:qs' => RuleSet('s', '>', 2770, 'qs')
    workflow_re = re.compile(r"(\w+)\{(.+)\}")
    rule_re = re.compile(r"((\w)(<|>)(\d+):(\w+))|(\w+)")
    # rule_re = re.compile(r"(\w)(<|>)(\d+):(\w+)")
    for line in lines:
        if line == '': break
        name, rules = workflow_re.findall(line)[0]
        workflows[name] = [RuleSet(n,c,int(v),d) if n else RuleSet('','default',0,catch_all) for _,n,c,v,d,catch_all in rule_re.findall(rules)]

    part_re = re.compile(r"(\w)=(\d*)")
    for line in lines:
        categories = part_re.findall(line)
        parts.append({cat:int(value) for cat,value in categories})
    return workflows, parts

def solve1(input: str) -> int:
    workflows, parts = parse(input)    
    accepted = []
    for part in parts:
        if process_part(part, 'in', workflows):
            accepted.append(part)
    
    print(accepted)
    result = sum(sum(p.values()) for p in accepted)
    return result

def get_limits(limits: dict, path, current_workflow_name:str, workflows:dict) -> list[dict]:
    if current_workflow_name == 'A':
        print (f"{limits} from {path}")
        return [limits]
    if current_workflow_name == 'R':
        return []
    limits = deepcopy(limits)
    current_workflow = workflows[current_workflow_name]
    list_of_limits = []
    for rule in current_workflow:
        new_limit = deepcopy(limits)
        if rule.condition == '<':
            new_limit[rule.category] = (new_limit[rule.category][0], min(new_limit[rule.category][1], rule.value-1))
            limits[rule.category] = (max(limits[rule.category][0], rule.value), limits[rule.category][1])
        elif rule.condition == '>':
            new_limit[rule.category] = (max(new_limit[rule.category][0], rule.value+1), new_limit[rule.category][1])
            limits[rule.category] = (limits[rule.category][0], min(limits[rule.category][1], rule.value))
        if rule.condition == 'default' or new_limit[rule.category][0] <= new_limit[rule.category][1]: 
            list_of_limits.extend(get_limits(new_limit, path + [current_workflow_name], rule.destination, workflows))
    return list_of_limits

def count_combinations(limits: dict) -> int:
    num_combinations = 1
    for c_min, c_max in limits.values():
        num_combinations *= c_max - c_min +1
    return num_combinations

def solve2(input:str) -> int:
    workflows,_ = parse(input)
    combinations = get_limits({'x':(1,4000),'m':(1,4000),'a':(1,4000),'s':(1,4000)}, [], 'in', workflows)
    print(combinations)
    num_combinations = sum (count_combinations(c) for c in combinations)
    return num_combinations

def solve():
    with open(Path(__file__).with_name('input.txt'), 'r') as f:
        answer = solve1(f.read())
        print (f"Part1: {answer}")

        f.seek(0)
        answer = solve2(f.read())
        print (f"Part2: {answer}")

if __name__ == '__main__': 
    solve()