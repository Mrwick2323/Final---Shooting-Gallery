from turtle import *
import random
import math
import time
window = Screen()
window.listen()
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
def distance(a,b) -> int: # not vibecoded im just the goat
    a=a.pos()
    b=b.pos()
    return math.dist(a,b)
class blocks():
    def __init__(self):
        self.blocks=[]
        self.players=[player('red',-40,'a','d','w',self),player('green',40,'Left','Right','Up',self)]
        self.bullets=[]
        self.isupdating=True
        self.upd()
        self.tupd()
    def upd(self):
        window.tracer(0)
        if self.isupdating:
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
            if self.blocks[0][0].ycor()<=-170:
                self.idiot()
        window.ontimer(self.upd,2000)
    def tupd(self):
        window.tracer(3)
        low = self.blocks[0][0].ycor()
        for i in self.bullets:
            if i.ycor()>=low-10:
                # prox = [j for k in range(len(self.blocks)) for j in range(len(self.blocks[k])) if distance(i,self.blocks[k][j])<=50]
                prox=[]
                for j in range(len(self.blocks)):
                    for k in range(len(self.blocks[j])):
                        print(distance(self.blocks[j][k],i))
                        if distance(self.blocks[j][k],i)<=10 and self.blocks[j][k].isvisible():
                            prox.append((k,j))
                print(prox)
                if len(prox)>0:
                    print('hi')
                    window.tracer(4)
                    if i.color()[0]=='red':
                        self.players[0].scorev += 10 if self.blocks[prox[0][1]][prox[0][0]].color()[0]!='green' else 40
                        self.players[0].scoret.upd()
                    else:
                        self.players[1].scorev+=10
                        self.players[1].scoret.upd()
                    self.kill(prox[0][1],prox[0][0])
                    window.tracer(3)
                    i.delete()
            i.forward(10)
            if abs(i.xcor())>130:
                i.setheading(180-i.heading())
        window.tracer(4)
        window.ontimer(self.tupd,120)
    def idiot(self):
        window.tracer(67)
        self.isupdating=False
        for i in turtles():
            i.ht()
        pen=Turtle()
        pen.ht()
        pen.pu()
        pen.speed(0)
        pen.setpos(-40,0)
        pen.pd()
        pen.write('Game Over!')
        window.tracer(68)
    def kill(self,j,k):
        blocks=self.blocks
        if 'green' in blocks[j][k].color():
            blocks[j][k].ht()
            blocks[j].pop(k)
            if j>0:
                blocks[j-1][k].ht()
                blocks[j-1].pop(k)
            if j!=len(self.blocks)-1:
                blocks[j+1][k].ht()
                blocks[j+1].pop(k)
            if k>0:
                blocks[j][k-1].ht()
                blocks[j].pop(k-1)
            if k!=len(self.blocks[j])-1:
                blocks[j][k-1].ht()
                blocks[j].pop(k-1)
        else:
            blocks[j].pop(k)
class score(Turtle):
    def __init__(self,sup):
        super().__init__()
        self.sup=sup
        self.ht()
        self.pu()
        self.color(sup.color()[0])
        self.sety(230)
        self.setx(sup.xcor()-30)
        self.pd()
        self.write(f'{sup.color()[0].title()} Score: {sup.scorev}')
    def upd(self):
        self.clear()
        self.write(f'{self.sup.color()[0].title()} Score: {self.sup.scorev}')

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
        self.supper=superior
        self.pu()
        self.shape('circle')
        self.shapesize(.25)
        self.setheading(superior.heading())
        self.setpos(superior.pos())
        self.color(superior.col)
        self.speed(0)
    def delete(self):
        self.ht()
        self.supper.superior.bullets.remove(self)
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
        window.tracer(16)
        self.scorev=0
        self.scoret=score(self)
        window.tracer(17)
        window.onkeypress(self.sleft,left)
        window.onkeypress(self.sright,right)
        window.onkeypress(self.shoot,shoot)
    def sleft(self):
        print('left')
        self.left(15)
    def sright(self):
        print('right')
        self.right(15)
    def shoot(self):
        print('shoot')
        self.superior.bullets.append(bullet(self))
blockes=blocks()
window.mainloop()