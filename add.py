'''
The add unit. Handles subtraction too
Opcodes 0:add; 1:sub
'''

class AddUnit:
    # The cycle number
    last_cycle = 0
    # Length of operation in cycles. Add and sub take 2
    op_length = 2
    # At first, the add unit will not be in an operation
    in_operation = False

    op_code = -1
    left = None
    right = None

    def __init__(self) -> None:
        pass

    def dispatch(self, opcode:int, dest:int, left:int, right:int):
        if self.in_operation == True:
            raise Exception(f'Add unit is already doing an operation!!! OP={[self.op_code,self.left,self.right]}')

        if opcode not in [0,1]:
            raise Exception(f'Invalid opcode sent to add unit!!!11 Received: {opcode}')

        self.in_operation = True
        self.last_cycle = 0
        self.op_code = opcode
        self.dest = dest
        self.left = left
        self.right = right

        print('Successfully dispatched to add unit!!1!')

    def run(self):
        
        if not self.in_operation:
            return
        
        self.last_cycle += 1

        # Reset and return result
        if self.last_cycle >= self.op_length:
            self.in_operation = False
            self.last_cycle = 0
            return dest, (self.left + self.right) if self.op_code == 0 else (self.left - self.right)


if __name__=='__main__':
    test_vals = [
        [0,4,6,10],
        [1,2,3,-1],
        [2,4,4,Exception]
    ]
    addunit = AddUnit()
    
    for test in test_vals:
        print(f'TEST={test}')
        try:
            addunit.dispatch(*test[0:3])
            for cycle in range(1,5):
                print('run', cycle)
                
                result = addunit.run()
                if result:
                    assert cycle == 2
                    assert result == test[3]
                    print(result)
        except:
            assert test == test_vals[2]