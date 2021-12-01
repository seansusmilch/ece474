'''
This file will have all the actual processor stuff
'''
from rezsta import ResStation
from helpers import parse_input

register_file = [0] * 8
rat = [0] * 5

'''
This Block sends the instructions to the corresponding
reservation stations.
'''

add_rs = [ResStation(11),ResStation(12),ResStation(13)]
mul_rs = [ResStation(14),ResStation(15)]

cycles, instructions, rf = parse_input()

for x in range(cycles):
    if instructions:
        # try to issue instruction
        op_code, dest, rleft, rright = instructions[0]
        if op_code in [0,1]:
            for rs in add_rs:
                if rs.is_empty():
                    rs.new_instruction(instructions[0])
                    del instructions[0]
                    break
        if op_code in [2,3]:
            for rs in mul_rs:
                if rs.is_empty():
                    rs.new_instruction(instructions[0])
                    del instructions[0]
                    break