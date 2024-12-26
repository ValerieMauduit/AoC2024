# Day 21: Keypad Conundrum

# First star: The door to that area is locked, but the computer can't open it; it can only be opened by physically
# typing the door codes (your puzzle input) on the numeric keypad on the door.
# The numeric keypad has four rows of buttons: 789, 456, 123, and finally an empty gap followed by 0A.
# Unfortunately, the area outside the door is currently depressurized and nobody can go near the door. A robot needs to
# be sent instead.
# The robot has no problem navigating the ship and finding the numeric keypad, but it's not designed for button pushing:
# it can't be told to push a specific button directly. Instead, it has a robotic arm that can be controlled remotely via
# a directional keypad.
# The directional keypad has two rows of buttons: a gap / ^ (up) / A (activate) on the first row and < (left) / v (down)
# / > (right) on the second row.
# When the robot arrives at the numeric keypad, its robotic arm is pointed at the A button in the bottom right corner.
# After that, this directional keypad remote control must be used to maneuver the robotic arm.
# Unfortunately, the area containing this directional keypad remote control is currently experiencing high levels of
# radiation and nobody can go near it. A robot needs to be sent instead.
# When the robot arrives at the directional keypad, its robot arm is pointed at the A button in the upper right corner.
# After that, a second, different directional keypad remote control is used to control this robot (in the same way as
# the first robot, except that this one is typing on a directional keypad instead of a numeric keypad).
# Unfortunately, the area containing this second directional keypad remote control is currently -40 degrees! Another
# robot will need to be sent to type on that directional keypad, too.
# Unfortunately, the area containing this third directional keypad remote control is currently full of Historians, so no
# robots can find a clear path there. Instead, you will have to type this sequence yourself.
# The complexity of a single code is equal to the result of multiplying these two values:
# - The length of the shortest sequence of button presses you need to type on your directional keypad in order to cause
#   the code to be typed on the numeric keypad.
# - The numeric part of the code (ignoring leading zeroes).
# Find the fewest number of button presses you'll need to perform in order to cause the robot in front of the door to
# type each code. What is the sum of the complexities of the five codes on your list?


# Second star: This time, many more robots are involved. In summary, there are the following keypads:
# - One directional keypad that you are using.
# - 25 directional keypads that robots are using.
# - One numeric keypad (on a door) that a robot is using.
# Find the fewest number of button presses you'll need to perform in order to cause the robot in front of the door to
# type each code. What is the sum of the complexities of the five codes on your list?

import os
import sys
import time

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

MOVES_TO_DIGICOD = {
    '0': {
        '0': 'A', '1': 'LUA', '2': 'UA', '3': 'URA', '4': 'UULA', '5': 'UUA', '6': 'RUUA', '7': 'UUULA',
        '8': 'UUUA', '9': 'RUUUA', 'A': 'RA'
    }, '1': {
        '0': 'RDA', '1': 'A', '2': 'RA', '3': 'RRA', '4': 'UA', '5': 'URA', '6': 'URRA', '7': 'UUA',
        '8': 'RUUA', '9': 'RRUUA', 'A': 'RRDA'
    }, '2': {
        '0': 'DA', '1': 'LA', '2': 'A', '3': 'RA', '4': 'LUA', '5': 'UA', '6': 'URA', '7': 'LUUA', '8': 'UUA',
        '9': 'UURA', 'A': 'DRA'
    }, '3': {
        '0': 'LDA', '1': 'LLA', '2': 'LA', '3': 'A', '4': 'LLUA', '5': 'LUA', '6': 'UA', '7': 'LLUUA',
        '8': 'LUUA', '9': 'UUA', 'A': 'DA'
    }, '4': {
        '0': 'RDDA', '1': 'DA', '2': 'DRA', '3': 'DRRA', '4': 'A', '5': 'RA', '6': 'RRA', '7': 'UA',
        '8': 'URA', '9': 'URRA', 'A': 'RRDDA'
    }, '5': {
        '0': 'DDA', '1': 'LDA', '2': 'DA', '3': 'DRA', '4': 'LA', '5': 'A', '6': 'RA', '7': 'LUA', '8': 'UA',
        '9': 'URA', 'A': 'DDRA'
    }, '6': {
        '0': 'LDDA', '1': 'LLDA', '2': 'LDA', '3': 'DA', '4': 'LLA', '5': 'LA', '6': 'A', '7': 'LLUA',
        '8': 'LUA', '9': 'UA', 'A': 'DDA'
    }, '7': {
        '0': 'RDDDA', '1': 'DDA', '2': 'DDRA', '3': 'DDRRA', '4': 'DA', '5': 'DRA', '6': 'DRRA', '7': 'A',
        '8': 'RA', '9': 'RRA', 'A': 'RRDDDA'
    }, '8': {
        '0': 'DDDA', '1': 'LDDA', '2': 'DDA', '3': 'DDRA', '4': 'LDA', '5': 'DA', '6': 'DRA', '7': 'LA',
        '8': 'A', '9': 'RA', 'A': 'DDDRA'
    }, '9': {
        '0': 'LDDDA', '1': 'LLDDA', '2': 'LDDA', '3': 'DDA', '4': 'LLDA', '5': 'LDA', '6': 'DA', '7': 'LLA',
        '8': 'LA', '9': 'A', 'A': 'DDDA'
    }, 'A': {
        '0': 'LA', '1': 'ULLA', '2': 'LUA', '3': 'UA', '4': 'UULLA', '5': 'LUUA', '6': 'UUA', '7': 'UUULLA',
        '8': 'LUUUA', '9': 'UUUA', 'A': 'A'
    },
}
MOVES_TO_KEYPAD = {
    'U': {'U': 'A', 'A': 'RA', 'L': 'DLA', 'D': 'DA', 'R': 'DRA'},
    'A': {'U': 'LA', 'A': 'A', 'L': 'DLLA', 'D': 'LDA', 'R': 'DA'},
    'L': {'U': 'RUA', 'A': 'RRUA', 'L': 'A', 'D': 'RA', 'R': 'RRA'},
    'D': {'U': 'UA', 'A': 'URA', 'L': 'LA', 'D': 'A', 'R': 'RA'},
    'R': {'U': 'LUA', 'A': 'UA', 'L': 'LLA', 'D': 'LA', 'R': 'A'},
}


def command_door(code, robots=3):
    group = 64
    position = 'A'
    robot = ''
    for v in code:
        move = MOVES_TO_DIGICOD[position][v]
        robot += move
        position = v
    next_code = robot
    moves = {}
    for count in range(1, robots):
        input(count)
        start = time.time()
        next_robot = ''
        sequence_of_moves = [x + 'A' for x in next_code.split('A')][:-1]
        sequence_of_moves = [
            ''.join(sequence_of_moves[(group * n):((n + 1) * group)])
            for n in range(int(len(sequence_of_moves) / group) + 1)
        ]
        for move in sequence_of_moves:
            if move in moves.keys():
                next_robot += moves[move]
            else:
                position = 'A'
                sub_move = ''
                for v in move:
                    m = MOVES_TO_KEYPAD[position][v]
                    sub_move += m
                    position = v
                moves[move] = sub_move
                next_robot += sub_move
        next_code = next_robot
        stop = time.time()
        print(f' - longueur : {len(next_code)}')
        print(f' - Exec (s) : {stop - start}')

    return next_code


def complexity_sum(codes, robots=3):
    complexity = 0
    for code in codes:
        print(code)
        complexity += int(code[:-1]) * len(command_door(code, robots))
    return complexity


def long_chain(codes, steps=25):
    # First define the possible results for 5 steps
    next_move = {}
    for code in set(
            [v for x in MOVES_TO_DIGICOD.values() for v in x.values()]
            + [v for x in MOVES_TO_KEYPAD.values() for v in x.values()]
    ):
        position = 'A'
        new_code = ''
        for x in code:
            new_code += MOVES_TO_KEYPAD[position][x]
            position = x
        next_move[code] = [x + 'A' for x in new_code.split('A')][:-1]

    # Then run each robot n (steps) times
    robots = {}
    for code in codes:
        print(code)
        robot = ''
        position = 'A'
        for v in code:
            move = MOVES_TO_DIGICOD[position][v]
            robot += move
            position = v
        last_robot_command = [x + 'A' for x in robot.split('A')][:-1]
        set_of_codes = list(set(last_robot_command))
        moves_by_step = []
        for step in range(steps):
            moves_by_step += [{c: next_move[c] for c in set_of_codes}]
            set_of_codes = list(set([c for v in moves_by_step[-1].values() for c in v]))
        length_of_codes = {k: len(''.join(v)) for k, v in moves_by_step[-1].items()}
        for step in range(2, steps + 1):
            length_of_codes = {k: sum([length_of_codes[x] for x in v]) for k, v in moves_by_step[-step].items()}
        robots[code] = sum([length_of_codes[x] for x in last_robot_command])
        print(f'Robot for code door {code}, length = {robots[code]}')
    return robots


def run(data_dir, star):
    data = ['341A', '480A', '286A', '579A', '149A']

    if star == 1:  # The final answer is: 132532
        solution = complexity_sum(data)
    elif star == 2:  # The final answer is: 165644591859332
        solution = sum([int(k[:-1]) * v for k, v in long_chain(data).items()])
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
