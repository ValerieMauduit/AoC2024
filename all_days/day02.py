# Day2: Red-Nosed Reports

# First star: The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can
# only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if
# both of the following are true:
# - The levels are either all increasing or all decreasing.
# - Any two adjacent levels differ by at least one and at most three.
# How many reports are safe?

# Second star: The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single
# bad level in what would otherwise be a safe report. It's like the bad level never happened!
# Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the
# report instead counts as safe.
# How many reports are now safe?


import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AoC_tools.read_data import read_data


def is_safe(report):
    transformed_report = report.copy()
    transformed_report.sort()
    reversed_report = report.copy()
    reversed_report.reverse()
    if transformed_report in [report, reversed_report]:
        differences = [abs(report[index + 1] - report[index]) for index in range(len(report) - 1)]
        if min(differences) > 0:
            return max(differences) < 4
        return False
    return False


def is_safe_with_tolerance(report):
    return any([is_safe(report[0:i] + report[(i+1):]) for i in range(len(report))])


def count_safe(reports, with_tolerance=False):
    if with_tolerance:
        return sum([is_safe_with_tolerance(report) for report in reports])
    return sum([is_safe(report) for report in reports])


def run(data_dir, star):
    data = read_data(f'{data_dir}/input-day02.txt', split=' ')

    if star == 1:  # The final answer is: 202
        solution = count_safe(data)
    elif star == 2:  # The final answer is: 271
        solution = count_safe(data, with_tolerance=True)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
