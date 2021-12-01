'''
The multiply unit. Handles division too
Opcodes 2:multiply; 3:divide
'''

class MultiplyUnit:
    # The cycle number
    last_cycle = 0
    # Length of operation in cycles. Multiply takes 10 and division takes 40
    op_length_mul = 10

    op_length_div = 40
    # At first, the multiply unit will not be in an operation
    in_operation = False

    op_code = -1
    left = None
    right = None

    def __init__(self) -> None:
        pass

    def dispatch(self, opcode:int, dest:int, left:int, right:int):
        if self.in_operation == True:
            raise Exception(f'Multiply unit is already doing an operation!!! OP={[self.op_code,self.left,self.right]}')

        if opcode not in [2,3]:
            raise Exception(f'Invalid opcode sent to multiply unit!!!11 Received: {opcode}')

        self.in_operation = True
        self.last_cycle = 0
        self.op_code = opcode
        self.dest = dest
        self.left = left
        self.right = right

        print('Successfully dispatched to multiply unit!!1!')

    def run(self):
        
        if not self.in_operation:
            return
        
        self.last_cycle += 1

        # Reset and return result
        if self.last_cycle >= self.op_length_mul and (self.op_code == 2):
            self.in_operation = False
            self.last_cycle = 0
            return dest, (self.left * self.right) 
        
        # Reset and return result
        if self.last_cycle >= self.op_length_div and (self.op_code == 3):
            self.in_operation = False
            self.last_cycle = 0
            return dest, (self.left / self.right) 


if __name__=='__main__':
    test_vals = [
        [2,4,4,16],
        [3,8,2,4],
        [0,4,4,Exception]
    ]
    multiplyunit = MultiplyUnit()
    
    for test in test_vals:
        print(f'TEST={test}')
        try:
            multiplyunit.dispatch(*test[0:3])
            for cycle in range(1,45):
                print('run', cycle)
                
                result = multiplyunit.run()
                if result:
                    print(result)
                    assert cycle == 10 or cycle == 40
                    assert result == test[3]
        except:
            assert test == test_vals[2]
