from turtle import *
class blocks():
    def __init__(self):
        self.blocks=[]
    def upd(self):
        self.blocks.append([])
        for i in range(11):
            self.blocks[0].append(block())
class block(Turtle):
    def __init__(self):
        super().__init__()
        