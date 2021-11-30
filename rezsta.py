class ResStation:
    tag_left = -1
    tag_right = -1
    val_left = None
    val_right = None
    op_code = -1
    dest = -1
    ready = False

    def __init__(self, rs_tag:int):
        self.ready = False

    def set_value(self, tag:int, val:int):
        if tag == self.tag_left:
            self.val_left = val
        if tag == self.tag_right:
            self.val_right = val
        self.is_ready()

    def new_instruction(self, instruction:list):
        self.ready = False

        self.op_code = instruction.pop(0)
        self.dest = instruction.pop(0)
        self.tag_left = instruction.pop(0)
        self.tag_right = instruction.pop(0)

        self.val_left = None
        self.val_right = None
    
    def is_ready(self):
        self.ready = self.val_right != None and self.val_right != None
        return self.ready

    def get_inst_with_values(self):
        if not self.is_ready():
            print('instruction not ready yet!!!')
            return None
        
        return [self.op_code, self.dest, self.val_left, self.val_right]


if __name__=='__main__':
    test_inst = [1,2,3,4]

    rs = ResStation(11)
    rs.new_instruction(test_inst)

    rs.set_value(3, 5)
    print(rs.is_ready()==False)
    rs.set_value(4, 4)
    if rs.is_ready():
        print(rs.get_inst_with_values())