# complete and bug-tested

import random
class bag:
    def __init__(self, num):
        self.size = num
        self.data = range(num)
        random.shuffle(self.data)
    def isEmpty(self):
        if len(self.data):
            return False
        else:
            return True
    def refill(self):
            self.data = range(self.size)
            random.shuffle(self.data)
    def grab(self):
        if self.isEmpty():
            self.refill()
        return self.data.pop()
