from turtle import *
import random
window = Screen()
window.setup(500,500)
window.bgcolor("black")
pen=Turtle()
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









class row(Turtle):
    def __init__(self,row,height):
        super().__init__()
        self.row=row
        self.speed(0)
        self.height=height
        self.shape('square')
        self.hideturtle()
        self.pu()
    def draw(self):
        window.tracer(3)
        self.clearstamps()
        self.sety(self.height)
        self.setx(-110)
        for i in self.row:
            self.color(['light grey','grey','dark grey','#00FF00'][int(i)-1])
            self.stamp()
            self.setx(self.xcor()+21.9)
        window.tracer(4)
class blockhandler(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.shape('square')
        self.pu()
        self.blocks=[]
        self.blocks.append(self.genrow())
        self.turts=[]
        self.draw()
    def genrow(self):
        if len(self.blocks)==0:
            return (s:='12312312312')[:(w:=random.randint(0,10))]+'4'+s[w+1:]
        else:
            s=''.join([str(i%3+1) for i in range(int(self.blocks[-1][-1]),int(self.blocks[-1][-1])+11)])
            return s[:(w:=random.randint(0,10))]+'4'+s[w+1:]
        window.ontimer(self.genrow,2000)
    def draw(self):
        self.blocks.append(self.genrow())
        if len(self.turts)!=len(self.blocks):
            self.turts.append(row(self.blocks[-1],250))
        for i in self.turts:
            window.tracer(0)
            i.height-=20
            i.clearstamps()
            window.ontimer(i.draw)
            window.tracer(1)
        window.ontimer(self.draw,1000)
class player(Turtle):
    def __init__(self,color,lekey,rikey):
        super().__init__()
        self.lf=False
        self.rf=False
        self.speed(0)
        self.color(color)
        self.bullets=[]
        window.onkey(self.uml,lekey)
        window.onkey(self.umr,rikey)
        window.onkeypress(self.ml,lekey)
        window.onkeypress(self.mr,rikey)
        self.move()
    def ml(self):
        self.lf=True
    def mr(self):
        self.rf=True
    def uml(self):
        self.lf=False
    def umr(self):
        self.rf=False
    def move(self):
        if self.lf and not self.rf:
            self.left(1)
        if self.rf and not self.lf:
            self.right(1)
        window.ontimer(self.move,12)
class bullet(Turtle):
    def __init__(self,host):
        super().__init__()
        self.host=host
        self.color(host.color())
        self.setpos(host.position())
        self.setheading(host.heading())
        
p1=player('red','a','d')

    
blocks = blockhandler()
window.listen()









window.mainloop()