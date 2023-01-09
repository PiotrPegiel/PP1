import turtle
import random
def parallelogram(strx, stry, col, fil, lenx, leny, rot):
    t.speed(0)
    t.penup()
    t.color(col, fil)
    t.goto(strx, stry)
    t.pendown()
    t.begin_fill()
    t.rt(rot)
    for i in range(2):
        t.fd(lenx)
        t.lt(30)
        t.fd(leny)
        t.lt(180-30)
    t.end_fill()
    t.lt(rot)

def trapeze(strx, stry, col, fil, lenx, leny, rot):
    t.speed(0)
    t.penup()
    t.color(col, fil)
    t.goto(strx, stry)
    t.pendown()
    t.begin_fill()
    t.rt(rot)
    t.fd(lenx)
    t.rt(70)
    t.bk(leny)
    t.lt(70)
    t.bk(lenx/2)
    t.goto(strx, stry)
    t.end_fill()
    t.lt(rot)

def circle(strx, stry, col, fil, rad, rot):
    t.speed(0)
    t.penup()
    t.color(col, fil)
    t.goto(strx, stry)
    t.pendown()
    t.rt(rot)
    t.begin_fill()
    t.circle(rad)
    t.end_fill()
    t.lt(rot)

def cross(strx, stry, col, fil, len, rot):
    t.speed(0)
    t.penup()
    t.color(col, fil)
    t.goto(strx, stry)
    t.pendown()
    t.rt(rot)
    t.begin_fill()
    for i in range(4):
        t.fd(len)
        t.rt(90) 
        t.fd(len)
        t.lt(90)
        t.fd(len)
        t.lt(90)        
    t.end_fill()
    t.lt(rot)
def rhombus(strx, stry, col, fil, len, rot):
    t.speed(0)
    t.penup()
    t.color(col, fil)
    t.goto(strx, stry)
    t.pendown()
    t.rt(rot)
    t.begin_fill()
    for i in range(4):
        t.fd(len)
        t.rt(70) 
        t.bk(len)
        t.rt(180-70)       
    t.end_fill()
    t.lt(rot)
def signature(strx, stry):
    t.speed(0)
    t.penup()
    t.pencolor("white")
    t.goto(strx, stry)
    t.pendown()
    t.bk(10)
    t.fd(10)
    t.rt(90)
    t.fd(10)
    t.rt(90)
    t.fd(10)
    t.bk(10)
    t.lt(90)
    t.fd(10)
    t.rt(90)
    t.fd(10)
    t.penup()
    t.fd(10)
    t.pendown()
    t.rt(90)
    t.fd(10)
    t.fd(10)
    t.lt(90)
    t.penup()
    t.fd(10)
    t.pendown()
    t.lt(90)
    t.fd(10)
    t.fd(10)
    t.rt(90)
    t.penup()
    t.fd(10)
    t.pendown()
    t.rt(90)
    t.fd(10)
    t.fd(10)
    t.penup()
    t.bk(10)
    t.lt(90)
    t.fd(10)
    t.pendown()
    t.fd(10)
    t.penup()
    t.fd(10)
    t.pendown()
    t.lt(90)
    t.fd(10)
    t.bk(20)
    t.penup()
    t.rt(90)
    t.fd(10)
    t.lt(90)
    t.fd(5)
    t.pendown()
    t.bk(5)
    t.rt(90)
    t.fd(10)
    t.lt(90)
    t.fd(10)
    t.lt(90)
    t.fd(10)
    t.rt(90)
    t.fd(10)
    t.rt(90)
    t.fd(10)
    t.rt(90)
    t.fd(5)
    t.penup()
    t.fd(15)
    t.lt(90)
    t.fd(10)
    t.lt(90)
    t.fd(5)
    t.pendown()
    t.bk(5)
    t.rt(90)
    t.fd(10)
    t.lt(90)
    t.fd(10)
    t.lt(90)
    t.fd(10)
    t.rt(90)
    t.fd(10)
    t.rt(90)
    t.fd(10)
    t.rt(90)
    t.fd(5)
    t.penup()
    t.bk(5)
    t.lt(90)
    t.fd(10)
    t.rt(90)
    t.pendown()
    t.fd(10)
    t.penup()
    t.fd(5)
    t.pendown()
    t.fd(5)
    t.penup()
    t.lt(90)
    t.fd(10)
    t.pendown()
    t.fd(10)
    t.bk(10)
    t.lt(90-26.56)
    t.fd(22.36)
    t.rt(90-26.56)
    t.bk(10)

    t.penup()
    t.fd(20)
    t.pendown()
    t.fd(10)
    t.lt(63.43)
    t.bk(22.36)
    t.rt(63.43)
    t.fd(10)

    t.penup()
    t.fd(30)
    t.pendown()
    t.lt(90)
    t.fd(20)
    t.rt(90)
    t.bk(10)
    t.penup()
    t.fd(20)
    t.pendown()
    t.fd(10)
    t.rt(90)
    t.fd(10)
    t.rt(90)
    t.fd(10)
    t.bk(10)
    t.lt(90)
    t.fd(10)
    t.rt(90)
    t.fd(10)
    t.penup()
    t.bk(20)
    t.rt(90)
    t.pendown()
    t.fd(5)
    t.penup()
    t.fd(5)
    t.pendown()
    t.fd(15)
    t.penup()
    t.bk(20)
    t.rt(90)
    t.fd(10)
    t.pendown()
    t.fd(10)
    t.lt(90)
    t.fd(20)
    t.lt(90)
    t.fd(10)
    t.lt(90)
    t.fd(10)
    t.lt(90)
    t.fd(5)
    t.penup()
    t.fd(15)
    t.rt(90)
    t.fd(10)
    t.lt(90)
    t.pendown()
    t.fd(10)
    t.lt(90)
    t.fd(10)
    t.lt(90)
    t.fd(10)
    t.bk(10)
    t.rt(90)
    t.fd(10)
    t.lt(90)
    t.fd(10)
    t.rt(90)
    t.fd(5)
    t.penup()
    t.bk(5)
    t.rt(90)
    t.fd(30)
    t.rt(90)
    t.pendown()
    t.fd(20)
    t.rt(90)
    t.fd(10)
    t.rt(90)
    t.fd(10)
    t.rt(90)
    t.fd(10)
    t.penup()

    




# 5 figur x 4 (max 1min drawing time) each in defined function
# rysowanie imienia i nazwiska za pomocą funkcji
s = turtle.getscreen()
t = turtle.Turtle()
turtle.bgcolor("blue")
for i in range(4):
    x = random.randint(-400,400)
    y = random.randint(-400,400)
    parallelogram(x,y,"red","white",100,20,10)
for i in range(4):
    x = random.randint(-400,400)
    y = random.randint(-400,400)
    trapeze(x,y,"green","red",70,40,0)
for i in range(4):
    x = random.randint(-400,400)
    y = random.randint(-400,400)
    circle(x,y,"white","blue",50,90)
for i in range(4):
    x = random.randint(-400,400)
    y = random.randint(-400,400)
    cross(x,y,"yellow","yellow",60,5)
for i in range(4):
    x = random.randint(-400,400)
    y = random.randint(-400,400)
    rhombus(x,y,"blue","pink",20,-90)
signature(400,400)


# t.right(90)
# t.forward(100)
# t.left(90)
# t.backward(100)
# t.goto(100,100)
# t.home()
# t.circle(60)
# t.dot(20)
# turtle.title("My Turtle Program")
# t.shapesize(1,5,10)
# t.shapesize(10,5,1)
# t.shapesize(1,10,5)
# t.shapesize(1,1,1)
# t.pensize(5)
# t.forward(100)
# t.fillcolor("red")
# t.pencolor("green")
# t.color("green", "red")
# t.begin_fill()
# t.fd(100)
# t.lt(120)
# t.end_fill()
# t.shape("turtle")
# t.shape("arrow")
# t.shape("circle")
# t.speed(1)
# t.speed(10)
# t.pen(pencolor="purple", fillcolor="orange", pensize=10, speed=9)
# t.penup()
# t.pendown()
# t.undo()
# t.clear()
# t.reset()
# t.stamp()
# t.clearstamp(0)
# c = t.clone()