from copy import deepcopy
from dataclasses import dataclass
from enum import IntEnum, auto, Enum
from pathlib import Path
from typing import Tuple
from more_itertools import peekable
import re

@dataclass
class Module:
    name: str
    inputs: dict
    outputs: list[str]
    state: bool     # False = low
    module_type: str

def parse(lines: list[str]) -> dict:
    re_module = re.compile(r"(%|&)?(\w+) -> (.*)")
    modules = dict()
    for line in lines:
        m_type, name, outputs = re_module.findall(line)[0]
        modules[name] = Module(name, dict(), [o.strip() for o in outputs.split(',')], False, m_type)

    for con in (modules[m] for m in modules if modules[m].module_type == '&'):
        con.inputs = { m.name: False for m in modules.values() if con.name in m.outputs}
    return modules

def press_button1(modules) -> Tuple[int, int]:
    pulse_count = (1,0)
    pulses = [(False, 'broadcaster', 'button')]
    while pulses:
        next_pulses = []
        for in_state, target, source in pulses:
            out_state = None
            if target not in modules: 
                continue
            target_module = modules[target]
            if target_module.name == 'broadcaster':
                out_state = in_state
            elif target_module.name == 'rx':
                target_module.state = in_state
            elif target_module.module_type == '%' and not in_state:
                target_module.state = not target_module.state
                out_state = target_module.state
            elif target_module.module_type == '&':
                target_module.inputs[source] = in_state
                out_state = not all(target_module.inputs.values())

            if out_state is not None:
                next_pulses.extend((out_state, name, target_module.name) for name in target_module.outputs)
        pulse_count = ( pulse_count[0] + sum(1 for x,_,_ in next_pulses if not x),
                        pulse_count[1] + sum(1 for x,_,_ in next_pulses if x))
        pulses = next_pulses
    return pulse_count

def press_button2(modules, order) -> Tuple[int, int]:
    pulses = [(False, 'broadcaster', 'button')]
    while pulses:
        next_pulses = []
        for in_state, target, source in pulses:
            out_state = None
            if target not in modules: 
                continue
            target_module = modules[target]
            if target_module.name == 'broadcaster':
                out_state = in_state
            elif target_module.name == 'rx':
                target_module.state = in_state
            elif target_module.module_type == '%' and not in_state:
                target_module.state = not target_module.state
                out_state = target_module.state
                if not hasattr(target_module, 'order'): 
                    target_module.order = order
                    order += 1
            elif target_module.module_type == '&':
                target_module.inputs[source] = in_state
                out_state = not all(target_module.inputs.values())

            if out_state is not None:
                next_pulses.extend((out_state, name, target_module.name) for name in target_module.outputs)
        pulses = next_pulses
    return order

def solve1(modules_input) -> int:
    modules = parse(modules_input)
    sum_low, sum_high = 0,0
    for i in range(1000):
        num_low, num_high = press_button1(modules)
        sum_low += num_low
        sum_high += num_high
    return sum_high *sum_low    

def solve2(modules_input) -> int:
    modules = parse(modules_input)
    order = 0
    for _ in range(3000):
        order = press_button2(modules, order)

    flip_list = [m.name for m in sorted(modules.values(), key=lambda x: x.order if hasattr(x, 'order') else 99) if m.module_type == '%']
    print(" ".join('{:2d}'.format(modules[m].order) for m in flip_list))
    print(" ".join(m[:2] for m in flip_list))
    
    count = 0
    modules = parse(modules_input)
    modules['rx'] = Module('rx', dict(), [], True, 'rx')
    while modules['rx'].state:
        count += 1
        press_button2(modules, 0)
        print("  ".join(str(int(modules[m].state)) for m in flip_list))

    return count

def solve():
    with open(Path(__file__).with_name('input.txt'), 'r') as f:
        lines = f.read().split('\n')
        answer = solve1(lines)
        print (f"Part1: {answer}")

        answer = solve2(lines)
        print (f"Part2: {answer}")



if __name__ == '__main__': solve()