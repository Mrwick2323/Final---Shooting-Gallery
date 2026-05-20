from turtle import *
import random
window = Screen()
window.setup(500,500)
window.bgcolor("black")
pen=Turtle()
pen.speed(0)
pen.pu()
pen.color("white")
pen.hideturtle()
pen.setpos(-130,-250)
pen.pd()
pen.begin_fill()
pen.setx(130)
pen.sety(250)
pen.setx(-130)
pen.sety(-250)
pen.end_fill()
pen.pu()
class blocks():
    def __init__(self):
        self.blocks=[]
        self.players=[player('red',-40,'a','d','w',self)]
        self.bullets=[]
        self.upd()
        self.tupd()
    def upd(self):
        window.tracer(0)
        if [] in self.blocks:
            self.blocks.remove([])
        for i in self.blocks:
            for j in i:
                j.sety(j.ycor()-20)
        self.blocks.append([])
        if len(self.blocks)>1:
            for i in range(11):
                self.blocks[-1].append(block(20*i-100,self.blocks[-2][-1].col+1)) if len(self.blocks[-1])==0 else self.blocks[-1].append(block(20*i-100,self.blocks[-1][-1].col+1))
        else:
            for i in range(11):
                self.blocks[-1].append(block(20*i-100,i))
        window.tracer(1)
        window.ontimer(self.upd,1000)
    def tupd(self):
        window.tracer(3)
        for i in self.players:
            if i.lflag and not i.rflag:
                i.left(15)
            if i.rflag and not i.lflag:
                i.right(15)
        for i in self.bullets:
            i.forward(10)
        window.tracer(4)
        window.ontimer(self.tupd,120)
class block(Turtle):
    def __init__(self,x,col):
        super().__init__()
        self.col=col
        self.ht()
        self.pu()
        self.speed(0)
        self.sety(220)
        self.setx(x)
        self.color(['light grey','grey','dark grey'][col%3])
        if random.randint(0,9)==0:
            self.color('green')
        self.shape('square')
        self.st()
class bullet(Turtle):
    def __init__(self,superior):
        super().__init__()
        self.setheading(superior.heading())
        self.setpos(superior.pos())
        self.color(superior.col)
        self.speed(0)
class player(Turtle):
    def __init__(self,col,x,left,right,shoot,superior):
        super().__init__()
        self.superior=superior
        self.lflag=False
        self.rflag=False
        self.pu()
        self.col=col
        self.speed(0)
        self.setheading(90)
        self.color(col)
        self.shape('turtle')
        self.sety(-190)
        self.setx(x)
        window.onkeypress(self.sleft,left)
        window.onkeypress(self.sright,right)
        window.onkeypress(self.shoot,shoot)
    def sleft(self):
        self.left(15)
    def sright(self):
        self.right(15)
    def shoot(self):
        self.superior.bullets.append(bullet(self))
blockes=blocks()
window.mainloop()