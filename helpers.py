'''
This file will have helper functions that assist the processor
I'm thinking like getting the input data, and printing the output table
'''

from pathlib import Path
from beautifultable import BeautifulTable
from os import get_terminal_size

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

def print_table(add_rs:list, mul_rs:list, rf:list, rat:list, instructions:list):
    term_size = get_terminal_size().columns
    # term_size = 155

    rs_tbl = BeautifulTable(
        maxwidth=term_size if term_size > 80 else 80, 
        default_alignment=BeautifulTable.ALIGN_LEFT
        )
    rs_tbl.set_style(BeautifulTable.STYLE_COMPACT)
    rs_tbl.columns.header = ['', 'Busy', 'Op', 'Vj', 'Vk', 'Qj', 'Qk', 'Disp']
    count = 1
    for rs in add_rs+mul_rs:
        # rs = ResStation(rs)
        print(rs.rs_tag, rs.op_code)
        row = [f'RS{count}']
        count+=1
        
        busy = not (rs.is_empty())
        row.append(busy)
        
        if busy:
            row.append(rs.op_code)
            row.append(rs.val_left)
            row.append(rs.val_right)
            row.append(rs.tag_left)
            row.append(rs.tag_right)
            row.append('0')
        else:
            row += [''] * 6

        rs_tbl.rows.append(row)
    print(rs_tbl)

    ratrf_tbl = BeautifulTable(
        maxwidth=term_size if term_size > 80 else 80, 
        default_alignment=BeautifulTable.ALIGN_LEFT
        )
    ratrf_tbl.set_style(BeautifulTable.STYLE_COMPACT)

    ratrf_tbl.columns.header = ['', 'RF', 'RAT']

    for x in range(len(rf)):
        row = [f'{x}:', rf[x], rat[x]]
        ratrf_tbl.rows.append(row)
    print(ratrf_tbl)

    iq_tbl = BeautifulTable(
        maxwidth=term_size if term_size > 80 else 80, 
        default_alignment=BeautifulTable.ALIGN_LEFT
        )
    iq_tbl.set_style(BeautifulTable.STYLE_COMPACT)

    op = {
        0:'ADD',
        1:'SUB',
        2:'MUL',
        3:'DIV'
    }

    for inst in instructions:
        inst[0] = op[inst[0]]
        for x in range(3):
            inst[x+1] = f'R{inst[x+1]}'
            
        iq_tbl.rows.append(inst)
    print('Instruction Queue')
    print(iq_tbl)

if __name__=='__main__':
    print('Parse Input Test')
    cycles, insts, rf = parse_input()
    print(cycles == 7)
    print(insts == [[0, 2, 4, 6], [2, 4, 3, 5]])
    print(rf == [3, 4, 6, 21, 3, 4, 9, 0])

    from rezsta import ResStation
    print('Table Test')
    a = [ResStation(10), ResStation(12)]
    b = [ResStation(19)]

    a[0].new_instruction([1,4,7,5])
    b[0].new_instruction([4,5,2,8])
    print_table(a,b,range(8),range(8),[[0, 2, 4, 6], [2, 4, 3, 5]])