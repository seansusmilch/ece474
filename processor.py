'''
This file will have all the actual processor stuff
'''
from rezsta import ResStation
from helpers import parse_input

register_file = [0] * 8
rat = [None] * 8

'''
This Block sends the instructions to the corresponding
reservation stations.
'''

add_rs = [ResStation('RS1'),ResStation('RS2'),ResStation('RS3')]
mul_rs = [ResStation('RS4'),ResStation('RS5')]

cycles, instructions, rf = parse_input()

def issue(rs, op_code, dest, tag_left, tag_right, val_left, val_right):
    rs.new_instruction(op_code, dest, tag_left, tag_right, val_left, val_right)
    rat[dest] = rs.tag


for x in range(cycles):
    if instructions:
        # try to issue instruction
        op_code, dest, rleft, rright = instructions[0]

        tag_left = None
        tag_right = None
        val_left = None
        val_right = None

        if rat[rleft] != None:
            tag_left = rat[rleft]
        else:
            val_left = rf[rleft]

        if rat[rright] != None:
            tag_right = rat[rright]
        else:
            val_right = rf[rright]

        if op_code in [0,1]:
            for rs in add_rs:
                if rs.is_empty():
                    issue(rs, op_code, dest, tag_left, tag_right, val_left, val_right)
                    del instructions[0]
                    break
        if op_code in [2,3]:
            for rs in mul_rs:
                if rs.is_empty():
                    issue(rs, op_code, dest, tag_left, tag_right, val_left, val_right)
                    del instructions[0]
                    break

       

