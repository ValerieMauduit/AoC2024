# Day 12: Garden Groups

# First star: Each garden plot grows only a single type of plant and is indicated by a single letter on your map. When
# multiple garden plots are growing the same type of plant and are touching (horizontally or vertically), they form a
# region.
# In order to accurately calculate the cost of the fence around a single region, you need to know that region's area and
# perimeter.
# - The area of a region is simply the number of garden plots the region contains.
# - Each garden plot is a square and so has four sides. The perimeter of a region is the number of sides of garden plots
#   in the region that do not touch another garden plot in the same region.
# Due to "modern" business practices, the price of fence required for a region is found by multiplying that region's
# area by its perimeter. The total price of fencing all regions on a map is found by adding together the price of fence
# for every region on the map.
# What is the total price of fencing all regions on your map?

# Second star: description

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data
from AoC_tools.work_with_maps import AocMap


def plot_coords(garden, position, plant, all_points=None):
    if all_points is None:
        all_points = [position]
    plot_neighbours = [
        coord
        for coord in garden.get_neighbours_coordinates(diagonals=False)
        if (garden.get_point(coord) == plant) & (coord not in all_points)
    ]
    if not plot_neighbours:
        return all_points
    else:
        all_points + [plot_coords(garden, neighbour, plant, all_points) for neighbour in plot_neighbours]

    return ['area', 'perimeter', ['coords']]


def fencing_price(data):
    garden = AocMap(data)
    price = 0
    for x in range(garden.width):
        for y in range(garden.height):
            plant = garden.get_point([x, y])
            if plant != '.':
                area, perimeter, coords = plot_metrics(garden, [x, y], plant)
                price += area * perimeter
                garden.set_points(coords, '.')
    return price


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day12.txt')

    if star == 1:  # The final answer is:
        solution = fencing_price(data)
    elif star == 2:  # The final answer is:
        solution = my_func(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
