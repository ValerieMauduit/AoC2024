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

# Second star: Fortunately, the Elves are trying to order so much fence that they qualify for a bulk discount!
# Under the bulk discount, instead of using the perimeter to calculate the price, you need to use the number of sides
# each region has. Each straight section of fence counts as a side, regardless of how long it is.
# What is the new total price of fencing all regions on your map?

import os
import sys
import re

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data
from AoC_tools.work_with_maps import AocMap
from AoC_tools.work_with_lists import transpose


def calculate_perimeter(coordinates):
    perimeter = 0
    for coord in coordinates:
        neighbours_in_parcel = [c for c in get_neighbours(coord) if c in coordinates]
        perimeter += 4 - len(neighbours_in_parcel)
    return perimeter


def calculate_sides(coordinates):
    xmin, xmax = min([coord // 1000 for coord in coordinates]) - 1, max([coord // 1000 for coord in coordinates]) + 1
    ymin, ymax = min([coord % 1000 for coord in coordinates]) - 1, max([coord % 1000 for coord in coordinates]) + 1
    lines = [[1000 * x + y for x in range(xmin, xmax + 1)] for y in range(ymin, ymax + 1)]
    columns = transpose(lines)
    border_count = 0
    for line in range(1, ymax - ymin + 1):
        borders = ''.join([
            str((lines[line - 1][c] in coordinates) & (lines[line][c] not in coordinates))[0]
            for c in range(xmax - xmin + 1)
        ])
        border_count += len(re.findall('T+', borders))
        borders = ''.join([
            str((lines[line - 1][c] not in coordinates) & (lines[line][c] in coordinates))[0]
            for c in range(xmax - xmin + 1)
        ])
        border_count += len(re.findall('T+', borders))
    for col in range(1, xmax - xmin + 1):
        borders = ''.join([
            str((columns[col - 1][l] in coordinates) & (columns[col][l] not in coordinates))[0]
            for l in range(ymax - ymin + 1)
        ])
        border_count += len(re.findall('T+', borders))
        borders = ''.join([
            str((columns[col - 1][l] not in coordinates) & (columns[col][l] in coordinates))[0]
            for l in range(ymax - ymin + 1)
        ])
        border_count += len(re.findall('T+', borders))
    return border_count


def get_neighbours(int_coords):
    x0, y0 = int_coords // 1000, int_coords % 1000
    return [1000 * x + y for x, y in zip([x0 - 1, x0 + 1, x0, x0], [y0, y0, y0 - 1, y0 + 1])]


def fencing_price(data, with_discount=False):
    garden = AocMap(data)
    # Create all the parcels
    parcels = []
    for plant in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        plant_coords = [c[0] * 1000 + c[1] for c in garden.get_marker_coords(plant)]
        while len(plant_coords) > 0:
            parcel = [plant_coords[0]]
            plant_coords = plant_coords[1:]
            neighbours = parcel
            while len(neighbours) > 0:
                next_neighbours = []
                for coord in neighbours:
                    next_neighbours += get_neighbours(coord)
                neighbours = list(set([v for v in next_neighbours if v in plant_coords]))
                parcel = parcel + neighbours
                plant_coords = [c for c in plant_coords if c not in neighbours]
            parcels += [parcel]
    # Get metrics of the parcels and calculate price
    price = 0
    if with_discount:
        for parcel in parcels:
            price += len(parcel) * calculate_sides(parcel)
    else:
        for parcel in parcels:
            price += len(parcel) * calculate_perimeter(parcel)
    return price


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day12.txt', numbers=False)

    if star == 1:  # The final answer is: 1461752
        solution = fencing_price(data)
    elif star == 2:  # The final answer is: 904114
        solution = fencing_price(data, with_discount=True)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
