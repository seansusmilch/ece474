class ResStation:
    tag_left = -1
    tag_right = -1
    val_left = None
    val_right = None
    op_code = -1
    dest = -1
    ready = False
    empty = True
    dispatched = False

    def __init__(self, rs_tag):
        self.ready = False
        self.tag = rs_tag

    def set_value(self, tag:int, val:int):
        if self.empty: return

        if tag == self.tag_left:
            self.val_left = val
        if tag == self.tag_right:
            self.val_right = val
        self.is_ready()

    def is_empty(self):
        return self.empty

    def new_instruction(self, op_code:int, dest:int, tag_left, tag_right, val_left, val_right):
        self.ready = False
        self.empty = False
        self.op_code = op_code
        self.dest = dest
        self.tag_left = tag_left
        self.tag_right = tag_right

        self.val_left = val_left
        self.val_right = val_right
        self.is_ready()
    
    def is_ready(self):
        if self.empty: return False
        if self.dispatched: return False
        self.ready = self.val_left != None and self.val_right != None
        return self.ready

    def get_inst_with_values(self):
        if not self.is_ready():
            print('instruction not ready yet!!!')
            return None
        # self.empty = True
        self.dispatched = True

        return [self.op_code, self.dest, self.val_left, self.val_right]

    def free(self):
        if self.empty:
            print(f'{self.tag} is already free!!111')
        self.empty = True
        self.dispatched = False


if __name__=='__main__':
    test_inst = [1,2,3,4]

    rs = ResStation(11)
    rs.new_instruction(test_inst)

    rs.set_value(3, 5)
    print(rs.is_ready()==False)
    rs.set_value(4, 4)
    if rs.is_ready():
        print(rs.get_inst_with_values())