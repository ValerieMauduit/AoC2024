# Day 17: Chronospatial Computer

# First star: This seems to be a 3-bit computer: its program is a list of 3-bit numbers (0 through 7), like 0,1,2,3. The
# computer also has three registers named A, B, and C, but these registers aren't limited to 3 bits and can instead hold
# any integer.
# The computer knows eight instructions, each identified by a 3-bit number (called the instruction's opcode). Each
# instruction also reads the 3-bit number after it as an input; this is called its operand.
# A number called the instruction pointer identifies the position in the program from which the next opcode will be
# read; it starts at 0, pointing at the first 3-bit number in the program. Except for jump instructions, the instruction
# pointer increases by 2 after each instruction is processed (to move past the instruction's opcode and its operand). If
# the computer tries to read an opcode past the end of the program, it instead halts.
# So, the program 0,1,2,3 would run the instruction whose opcode is 0 and pass it the operand 1, then run the
# instruction having opcode 2 and pass it the operand 3, then halt.
# There are two types of operands; each instruction specifies the type of its operand. The value of a literal operand is
# the operand itself. For example, the value of the literal operand 7 is the number 7. The value of a combo operand can
# be found as follows:
# - Combo operands 0 through 3 represent literal values 0 through 3.
# - Combo operand 4 represents the value of register A.
# - Combo operand 5 represents the value of register B.
# - Combo operand 6 represents the value of register C.
# - Combo operand 7 is reserved and will not appear in valid programs.
# The eight instructions are as follows:
# - The adv instruction (opcode 0) performs division. The numerator is the value in the A register. The denominator is
#   found by raising 2 to the power of the instruction's combo operand. (So, an operand of 2 would divide A by 4 (2^2);
#   an operand of 5 would divide A by 2^B.) The result of the division operation is truncated to an integer and then
#   written to the A register.
# - The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then
#   stores the result in register B.
# - The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3
#   bits), then writes that value to the B register.
# - The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, it jumps
#   by setting the instruction pointer to the value of its literal operand; if this instruction jumps, the instruction
#   pointer is not increased by 2 after this instruction.
# - The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in
#   register B. (For legacy reasons, this instruction reads an operand but ignores it.)
# - The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a
#   program outputs multiple values, they are separated by commas.)
# - The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B
#   register. (The numerator is still read from the A register.)
# - The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C
#   register. (The numerator is still read from the A register.)
# Using the information provided by the debugger, initialize the registers to the given values, then run the program.
# Once it halts, what do you get if you use commas to join the values it output into a single string?

# Second star: What is the lowest positive initial value for register A that causes the program to output a copy of
# itself?

import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


def get_value(operand, register):
    if operand < 4:
        return operand
    elif operand == 4:
        return register['A']
    elif operand == 5:
        return register['B']
    elif operand == 6:
        return register['C']
    else:
        raise Exception


def one_operation(operator, operand, pointer, register):
    output, pointer = None, pointer + 2
    if operator == 0:
        # The adv instruction (opcode 0) performs division. The numerator is the value in the A register. The
        # denominator is found by raising 2 to the power of the instruction's combo operand. The result of the division
        # operation is truncated to an integer and then written to the A register.
        register['A'] = int(register['A'] / (2**get_value(operand, register)))
    elif operator == 1:
        # The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand,
        # then stores the result in register B.
        register['B'] = register['B'] ^ operand
    elif operator == 2:
        # The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its
        # lowest 3 bits), then writes that value to the B register.
        register['B'] = get_value(operand, register) % 8
    elif operator == 3:
        # The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero,
        # it jumps by setting the instruction pointer to the value of its literal operand; if this instruction jumps,
        # the instruction pointer is not increased by 2 after this instruction.
        if register['A'] != 0:
            pointer = operand
    elif operator == 4:
        # The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result
        # in register B. (For legacy reasons, this instruction reads an operand but ignores it.)
        register['B'] = register['B'] ^ register['C']
    elif operator == 5:
        # The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value.
        output = str(get_value(operand, register) % 8)
    elif operator == 6:
        # The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the
        # B register. (The numerator is still read from the A register.)
        register['B'] = int(register['A'] / (2 ** get_value(operand, register)))
    elif operator == 7:
        # The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the
        # C register. (The numerator is still read from the A register.)
        register['C'] = int(register['A'] / (2 ** get_value(operand, register)))
    else:
        raise Exception
    return register, output, pointer


def operate(data):
    pos, output = 0, []
    register, program = data['register'], data['program']
    while pos < len(program):
        operator, operand = program[pos], program[pos + 1]
        register, operation_output, pos = one_operation(operator, operand, pos, register)
        if operation_output:
            output += [operation_output]
    return {'register': register, 'output': ','.join(output)}


def get_best_register(data):
    output = ' '
    register_a = 90938893795500
    program_string = ','.join([str(x) for x in data['program']])
    while output != program_string:
        register_a = register_a + 1
        if register_a > 90938893811945:
            print(register_a)
        output = operate(
            {
                'register': {'A': register_a, 'B': data['register']['B'], 'C': data['register']['C']},
                'program': data['program']
            }
        )['output']
    return register_a, output


def run(data_dir, star):
    data = {'register': {'A': 66171486, 'B': 0, 'C': 0}, 'program': [2, 4, 1, 6, 7, 5, 4, 6, 1, 4, 5, 5, 0, 3, 3, 0]}

    if star == 1:  # The final answer is: 2,3,6,2,1,6,1,2,1
        data['register']['A'] = 90938893811944
        solution = operate(data)
    elif star == 2:  # The final answer is: 90938893795561
        solution = get_best_register(data)
    else:
        raise Exception('Star number must be either 1 or 2.')

    print(f'The solution (star {star}) is: {solution}')
    return solution
