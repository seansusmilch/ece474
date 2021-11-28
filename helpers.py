'''
This file will have helper functions that assist the processor
I'm thinking like getting the input data, and printing the output table
'''

from pathlib import Path

def parse_input():
    """Returns all input data used in the processor

    Returns:
        cycles: int - the number of cycles to simulate
        instructions: list[list[int]] list of instructions
        rf: list[int] initial values of the register file
    """    
    input_lines = []
    input_path = Path('./input.txt')
    if input_path.exists():
        file_lines = open(input_path, 'r').readlines()
        for line in file_lines:
            input_lines.append(line.strip())
    else:
        in_str = input('Paste in the input\n')
        input_lines = in_str.split('\n')

    print(input_lines)

    num_of_instructions = int(input_lines.pop(0))
    cycles = int(input_lines.pop(0))
    instructions = []
    
    for x in range(num_of_instructions):
        inst = input_lines.pop(0)
        inst = inst.split(' ')
        inst = list(map(int, inst))
        instructions.append(inst)
    
    rf = input_lines
    rf = list(map(int, rf))

    return cycles, instructions, rf



if __name__=='__main__':
    print('Helpers test')
    cycles, insts, rf = parse_input()
    print(cycles == 7)
    print(insts == [[0, 2, 4, 6], [2, 4, 3, 5]])
    print(rf == [3, 4, 6, 21, 3, 4, 9, 0])