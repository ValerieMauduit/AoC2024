# Day 14: Restroom Redoubt

# First star: You make a list (your puzzle input) of all of the robots' current positions (p) and velocities (v), one
# robot per line.
# Each robot's position is given as p=x,y where x represents the number of tiles the robot is from the left wall and y
# represents the number of tiles from the top wall (when viewed from above). So, a position of p=0,0 means the robot is
# all the way in the top-left corner.
# Each robot's velocity is given as v=x,y where x and y are given in tiles per second. Positive x means the robot is
# moving to the right, and positive y means the robot is moving down.
# The robots outside the actual bathroom are in a space which is 101 tiles wide and 103 tiles tall.
# The robots are good at navigating over/under each other (due to a combination of springs, extendable legs, and
# quadcopters), so they can share the same tile and don't interact with each other.
# These robots have a unique feature for maximum bathroom security: they can teleport. When a robot would run into an
# edge of the space they're in, they instead teleport to the other side, effectively wrapping around the edges.
# The Historian can't wait much longer, so you don't have to simulate the robots for very long. Where will the robots be
# after 100 seconds?
# To determine the safest area, count the number of robots in each quadrant after 100 seconds. Robots that are exactly
# in the middle (horizontally or vertically) don't count as being in any quadrant. Multiplying these four quadrant
# counts together gives a total safety factor.
# Predict the motion of the robots in your list within a space which is 101 tiles wide and 103 tiles tall. What will the
# safety factor be after exactly 100 seconds have elapsed?

# Second star: During the bathroom break, someone notices that these robots seem awfully similar to ones built and used
# at the North Pole. If they're the same type of robots, they should have a hard-coded Easter egg: very rarely, most of
# the robots should arrange themselves into a picture of a Christmas tree.
# What is the fewest number of seconds that must elapse for the robots to display the Easter egg?

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from itertools import groupby
from operator import itemgetter
from AoC_tools.read_data import read_data
from AoC_tools.work_with_maps import AocMap


def initialize_robots(data):
    robots = []
    for line in data:
        splitted = line.split('v')
        robots += [{
            'p': [int(x) for x in splitted[0][2:].split(',')],
            'v': [int(x) for x in splitted[1][1:].split(',')]
        }]
    return robots


def positions(robots, steps=100, width=101, height=103):
    return [
        {
            'p': [(robot['p'][0] + steps * robot['v'][0]) % width, (robot['p'][1] + steps * robot['v'][1]) % height],
            'v': robot['v']
        }
        for robot in robots
    ]


def safety_result(data, steps=100, width=101, height=103):
    robots = positions(initialize_robots(data), steps, width, height)
    quadrants = [0, 0, 0, 0]
    h_bar, v_bar = height // 2, width // 2
    for robot in robots:
        if robot['p'][0] < v_bar:
            if robot['p'][1] < h_bar:
                quadrants[0] += 1
            elif robot['p'][1] > h_bar:
                quadrants[1] += 1
        elif robot['p'][0] > v_bar:
            if robot['p'][1] < h_bar:
                quadrants[2] += 1
            elif robot['p'][1] > h_bar:
                quadrants[3] += 1
    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


def existing_line(points, min_length, height=103):
    found = False
    line = 0
    position = [0, 0]
    while (not found) & (line < height):
        points_in_line = list(set([p[0] for p in points if p[1] == line]))
        points_in_line.sort()
        lines = [list(map(itemgetter(1), g)) for k, g in groupby(enumerate(points_in_line), lambda x: x[0] - x[1])]
        if lines:
            if max([len(line) for line in lines]) >= min_length:
                found = True
                position = [[line[0] for line in lines if len(line) >= min_length][0], line]
        line += 1
    return found, position


def existing_column(points, position, min_h):
    column = [p for p in points if (p[0] == position[0]) & (p[1] >= position[1]) & (p[1] <= position[1] + min_h)]
    return len(column) >= min_h


def find_rectangle(data, min_w=5, min_h=5, width=101, height=103):
    robots = initialize_robots(data)
    found = False
    steps = 0
    while not found:
        steps += 1
        robots = positions(robots, steps=1, width=width, height=height)
        line_found, line_origin = existing_line([r['p'] for r in robots], min_w, height)
        if line_found:
            found = existing_column([r['p'] for r in robots], line_origin, min_h)
        if steps % 100 == 0:
            print(steps)
    robot_map = AocMap.empty_from_size(width, height)
    for robot in robots:
        robot_map.set_point(robot['p'])
    robot_map.display()
    return steps


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day14.txt', numbers=False)

    if star == 1:  # The final answer is: 219512160
        solution = safety_result(data)
    elif star == 2:  # The final answer is:
        solution = find_rectangle(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
