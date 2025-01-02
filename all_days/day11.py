# Day 11: Plutonian Pebbles

# First star: As you observe them for a while, you find that the stones have a consistent behavior. Every time you
# blink, the stones each simultaneously change according to the first applicable rule in this list:
# - If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# - If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left
#   half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new
#   right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# - If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is
#   engraved on the new stone.
# Consider the arrangement of stones in front of you. How many stones will you have after blinking 25 times?

# Second star: The Historians sure are taking a long time. To be fair, the infinite corridors are very large.
# How many stones would you have after blinking a total of 75 times?

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data


def one_blink(data):
    after = []
    for x in data:
        if x == 0:
            after += [1]
        else:
            length = len(str(x))
            if length % 2 == 0:
                cut_at = length // 2
                after += [int(str(x)[:cut_at]), int(str(x)[cut_at:])]
            else:
                after += [x * 2024]
    return after


def one_smart_blink(data):
    after = {}
    for value, count in data.items():
        if value == 0:
            if 1 in after.keys():
                after[1] += count
            else:
                after[1] = count
        else:
            length = len(str(value))
            if length % 2 == 0:
                cut_at = length // 2
                value1 = int(str(value)[:cut_at])
                if value1 in after.keys():
                    after[value1] += count
                else:
                    after[value1] = count
                value2 = int(str(value)[cut_at:])

                if value2 in after.keys():
                    after[value2] += count
                else:
                    after[value2] = count
            else:
                new_val = value * 2024
                if new_val in after.keys():
                    after[new_val] += count
                else:
                    after[new_val] = count
    return after


def get_star1(data, blinks=25):
    for i in range(blinks):
        if i % 5 == 0:
            print(i)
        data = one_blink(data)
    return len(data)


def get_star_smart_way(data, blinks=75):
    values = list(set(data))
    smart_dataset = {value: data.count(value) for value in values}
    for i in range(blinks):
        if i % 5 == 0:
            print(i)
        smart_dataset = one_smart_blink(smart_dataset)
    return sum(smart_dataset.values())


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day11.txt', split=' ')
    data = data[0]

    if star == 1:  # The final answer is: 233875
        solution = get_star1(data)
    elif star == 2:  # The final answer is: 277444936413293
        solution = get_star_smart_way(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
