# Day 23: LAN Party

# First star: The network map provides a list of every connection between two computers.
# Each line of text in the network map represents a single connection. Connections aren't directional.
# LAN parties typically involve multiplayer games, so maybe you can locate it by finding groups of connected computers.
# Start by looking for sets of three computers where each computer in the set is connected to the other two computers.
# Find all the sets of three inter-connected computers. How many contain at least one computer with a name that starts
# with t?

# Second star: Since it doesn't seem like any employees are around, you figure they must all be at the LAN party. If
# that's true, the LAN party will be the largest set of computers that are all connected to each other. That is, for
# each computer at the LAN party, that computer will have a connection to every other computer at the LAN party.
# The LAN party posters say that the password to get into the LAN party is the name of every computer at the LAN party,
# sorted alphabetically, then joined together with commas. (The people running the LAN party are clearly a bunch of
# nerds.)

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data


def update_dict(dictionary, key, value):
    if key in dictionary.keys():
        dictionary[key] += [value]
    else:
        dictionary[key] = [value]
    return dictionary


def map_computers(data, initial='t'):
    computer_neighbors = {}
    for pair in data:
        if pair[0][0] == initial:
            computer_neighbors = update_dict(computer_neighbors, pair[0], pair[1])
        if pair[1][0] == initial:
            computer_neighbors = update_dict(computer_neighbors, pair[1], pair[0])
    return computer_neighbors


def count_lans(data):
    neighbourhood = map_computers(data, 't')
    print(neighbourhood)
    input('...')
    lans = []
    for head, computer_set in neighbourhood.items():
        for i in range(len(computer_set) - 1):
            for j in range(i + 1, len(computer_set)):
                if ([computer_set[i], computer_set[j]] in data) | ([computer_set[j], computer_set[i]] in data):
                    lan = [head, computer_set[i], computer_set[j]]
                    lan.sort()
                    lans += ['-'.join(lan)]
    lans = set(lans)
    return len(lans)


def find_max_full_network(data):
    computer_neighbors = {}
    for pair in data:
        computer_neighbors = update_dict(computer_neighbors, pair[0], pair[1])
        computer_neighbors = update_dict(computer_neighbors, pair[1], pair[0])
    computers = list(computer_neighbors.keys())
    computers.sort()
    print(computers)
    all_networks = []
    for c in computers:
        print(c)
        all_networks += find_all_full_networks([c], computer_neighbors)
    max_length = max([len(n) for n in all_networks])
    return ','.join([n for n in all_networks if len(n) == max_length][0])


def find_all_full_networks(network, neighbor_mapping):
    common_neighbors = [c for c in neighbor_mapping.keys() if all([(c in neighbor_mapping[n]) & (c > n) for n in network])]
    if len(common_neighbors) == 0:
        return [network]
    else:
        networks = []
        for c in common_neighbors:
            networks += find_all_full_networks(network + [c], neighbor_mapping)
        return networks


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day23.txt', numbers=False, split='-')

    if star == 1:  # The final answer is: 1269
        solution = count_lans(data)
    elif star == 2:  # The final answer is: ad,jw,kt,kz,mt,nc,nr,sb,so,tg,vs,wh,yh
        solution = find_max_full_network(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
