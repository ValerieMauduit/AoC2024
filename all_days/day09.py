# Day 9: Disk Fragmenter

# First star: He shows you the disk map (your puzzle input) he's already generated.
# The disk map uses a dense format to represent the layout of files and free space on the disk. The digits alternate
# between indicating the length of a file and the length of free space.
# Each file on disk also has an ID number based on the order of the files as they appear before they are rearranged,
# starting with ID 0.
# The amphipod would like to move file blocks one at a time from the end of the disk to the leftmost free space block
# (until there are no gaps remaining between file blocks).
# The final step of this file-compacting process is to update the filesystem checksum. To calculate the checksum, add up
# the result of multiplying each of these blocks' position with the file ID number it contains. The leftmost block is in
# position 0. If a block contains free space, skip it instead.
# Compact the amphipod's hard drive using the process he requested. What is the resulting filesystem checksum?

# Second star: This time, attempt to move whole files to the leftmost span of free space blocks that could fit the file.
# Attempt to move each file exactly once in order of decreasing file ID number starting with the file with the highest
# file ID number. If there is no span of free space to the left of a file that is large enough to fit the file, the file
# does not move.
# Start over, now compacting the amphipod's hard drive using this new method instead. What is the resulting filesystem
# checksum?

import os
import sys
import numpy as np

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data


def check_sum(data):
    blocks = data
    ids = [-1 if i % 2 == 1 else int(i / 2) for i in range(len(blocks))]
    # Compact the blocks
    while -1 in ids:
        blank = ids.index(-1)
        if blocks[blank] > blocks[-1]:
            blocks = blocks[:blank] + [blocks[-1], blocks[blank] - blocks[-1]] + blocks[(blank + 1):-2]
            ids = ids[:blank] + [ids[-1], -1] + ids[(blank + 1):-2]
        elif blocks[blank] < blocks[-1]:
            blocks = blocks[:-1] + [blocks[-1] - blocks[blank]]
            ids = ids[:blank] + [ids[-1]] + ids[(blank + 1):]
        else:
            blocks = blocks[:-2]
            ids = ids[:blank] + [ids[-1]] + ids[(blank + 1):-2]
    positions = list(np.cumsum(blocks))
    return sum([ids[i] * sum(range(max(0, positions[i - 1]), positions[i])) for i in range(len(blocks))])


def check_sum_no_fragmentation(data):
    blocks = data
    ids = [-1 if i % 2 == 1 else int(i / 2) for i in range(len(blocks))]
    print(f'Count of files = {max(ids)}')
    # Compact the blocks
    for f in range(max(ids), 0, -1):
        if (f % 100 == 0):
            print(f)
        pos_f = ids.index(f)
        block_f = blocks[pos_f]
        p, free_block = 0, False
        while (not free_block) & (p < pos_f):
            if (ids[p] == -1) & (blocks[p] >= block_f):
                free_block = True
                blocks = blocks[:p] + [block_f, blocks[p] - block_f] + blocks[(p + 1):]
                ids = ids[:p] + [f, -1] + ids[(p + 1):(pos_f)] + [-1] + ids[(pos_f + 1):]
                # group contiguous -1
                p2 = 1
                while p2 < len(ids):
                    if ids[(p2 - 1):(p2 + 1)] == [-1, -1]:
                        ids = ids[:(p2 - 1)] + ids[p2:]
                        blocks = blocks[:(p2 - 1)] + [sum(blocks[(p2 - 1): (p2 + 1)])] + blocks[(p2 + 1):]
                    else:
                        p2 += 1
            else:
                p += 1
    # Compute the checksum
    positions = list(np.cumsum(blocks))
    return sum([max(ids[i], 0) * sum(range(max(0, positions[i - 1]), positions[i])) for i in range(len(blocks))])


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day09.txt')
    data = [int(x) for x in str(data[0])]

    if star == 1:  # The final answer is: 6346871685398
        solution = check_sum(data)
    elif star == 2:  # The final answer is: 6373055193464
        solution = check_sum_no_fragmentation(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
