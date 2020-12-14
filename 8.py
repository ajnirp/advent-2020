import sys

with open('8.txt') as f:
    program = [line.strip() for line in f.readlines()]

def run_program(program):
    accumulator = 0
    program_counter = 0
    has_executed = set() # set of values of program counter for which the
    # corresponding instruction has been executed.
    while True:
        if program_counter in has_executed:
            return accumulator
        instruction = program[program_counter]
        has_executed.add(program_counter) # technically it hasn't been
        # executed yet, but that's fine for now.
        old_program_counter = program_counter
        if instruction.startswith('nop'):
            program_counter += 1
        elif instruction.startswith('acc'):
            accumulator += int(instruction[4:])
            program_counter += 1
        elif instruction.startswith('jmp'):
            program_counter += int(instruction[4:])

# Run a program. If it loops forever, return False, else return the accumulator.
def terminates(program):
    accumulator = 0
    program_counter = 0
    has_executed = set()
    while True:
        if program_counter in has_executed:
            return False
        if program_counter == len(program):
            return accumulator
        if program_counter > len(program):
            print("shouldn't happen - unexpected termination", file=sys.stderr)
            sys.exit(1)
        instruction = program[program_counter]
        has_executed.add(program_counter)
        old_program_counter = program_counter
        if instruction[:3] == 'nop':
            program_counter += 1
        elif instruction[:3] == 'acc':
            accumulator += int(instruction.split()[1])
            program_counter += 1
        elif instruction[:3] == 'jmp':
            program_counter += int(instruction.split()[1])

# Given a program which will terminate if we change exactly one nop to jmp or
# jmp to nop (while preserving the instruction operand), find that instruction
# and return the accumulator value after running that program
def find_faulty_instruction(program):
    for idx, line in enumerate(program):
        if line.startswith('acc'):
            continue
        program_copy = [l for l in program]
        opcode = 'nop' if line.startswith('jmp') else 'jmp'
        program_copy[idx] = f'{opcode} {line[4:]}'
        retval = terminates(program_copy)
        if retval is False:
            continue
        else:
            return retval
    return "Failed to find the faulty instruction"

print('Part 1', run_program(program))
print('Part 2', find_faulty_instruction(program))