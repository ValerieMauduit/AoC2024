# Day 24: Crossed Wires

# First star: The device seems to be trying to produce a number through some boolean logic gates. Each gate has two
# inputs and one output. The gates all operate on values that are either true (1) or false (0).
# - AND gates output 1 if both inputs are 1; if either input is 0, these gates output 0.
# - OR gates output 1 if one or both inputs is 1; if both inputs are 0, these gates output 0.
# - XOR gates output 1 if the inputs are different; if the inputs are the same, these gates output 0.
# Ultimately, the system is trying to produce a number by combining the bits on all wires starting with z. z00 is the
# least significant bit, then z01, then z02, and so on.
# Simulate the system of gates and wires. What decimal number does it output on the wires starting with z?

# Second star: description

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data


def format_data(data):
    outputs = {x.split(': ')[0]: bool(int(x.split(': ')[1])) for x in data[0]}
    gates = {x.split(' -> ')[1]: x.split(' -> ')[0].split(' ') for x in data[1]}
    return outputs, gates


def get_z_outputs(outputs, gates):
    z_outputs_in_gates = [g for g in gates.keys() if g[0] == 'z']
    while len(z_outputs_in_gates) > 0:
        for output, command in gates.items():
            if (command[0] in outputs.keys()) and (command[2] in outputs.keys()):
                if command[1] == 'AND':
                    outputs[output] = outputs[command[0]] & outputs[command[2]]
                elif command[1] == 'OR':
                    outputs[output] = outputs[command[0]] | outputs[command[2]]
                elif command[1] == 'XOR':
                    outputs[output] = outputs[command[0]] ^ outputs[command[2]]
        gates = {k: v for k, v in gates.items() if k not in outputs.keys()}
        z_outputs_in_gates = [g for g in gates.keys() if g[0] == 'z']
    return {k: v for k, v in outputs.items() if k[0] == 'z'}


def calculate(data):
    outputs, gates = format_data(data)
    z_outputs = get_z_outputs(outputs, gates)
    return sum([int(v) * 2 ** int(k[1:]) for k, v in z_outputs.items()])


def theoretical_result(outputs):
    x = sum([int(v) * 2 ** int(k[1:]) for k, v in outputs.items() if k[0] == 'x'])
    y = sum([int(v) * 2 ** int(k[1:]) for k, v in outputs.items() if k[0] == 'y'])
    return x + y


def actual_result(outputs):
    return sum([int(v) * 2 ** int(k[1:]) for k, v in outputs.items() if k[0] == 'z'])


def try_four_swaps(data):
    outputs, gates = format_data(data)
    theo, actual = theoretical_result(outputs), actual_result(outputs)
    nmax = len(list(gates.keys()))
    while actual != theo:
        x = 42


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day24.txt', numbers=False, by_block=True)

    if star == 1:  # The final answer is: 48508229772400
        solution = calculate(data)
    elif star == 2:  # The final answer is:
        solution = calculate(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution