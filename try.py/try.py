from turtle import *
import random
speed(500) 
bgcolor('dark blue')

DrkB='#002'

def p(x,y):
    penup()
    goto(x,y) 
    pendown()

def b():

    begin_fill()
def e():

    end_fill()

def f(str):
    fillcolor(str)

def c(int):
    circle(int)

def s_head():
    f(DrkB)
    b()
    rt(180)
    fd(260)
    rt(90)
    fd(120)
    circle(-102,180)
    fd(120)
    e()
    p(0,0)

def s_middle():
    f(DrkB)
    b()
    lt(90)
    rt(180)
    fd(280)
    circle(15,180)
    fd(280*2)
    circle(15,180)
    fd(280)
    e()

def s_base():
    f(DrkB)
    b()
    fd(270)
    lt(90)
    fd(30)
    z=1
    for x in range(15):
        fd(z)
        rt(1)
        z+=1
    lt(15)
    lt(90)
    fd(320)
    p(0,0)
    e()
    

def grass():
    p(0,-150)
    f('green')
    b()
    fd(700)
    rt(90)
    for x in range(2):
        fd(900)
        rt(90)
        fd(1400)
        rt(90)
    e()

def stars():

    for x in range(50):

        f('white')
        b()
        speed(500)
        m=random.randint(-999,999)
        n=random.randint(000,999)
        pencolor('white')
        p(m,n)
        circle(2)
        e()
        speed(500)
        pencolor('black')
        p(0,0)

def snake():
    f('dark green')
    p(0,0)
    lt(270)
    fd(275.0)
    b()
    rt(90)
    fd(240)
    circle(-50,180)
    rt(90)
    fd(95)
    lt(90)
    fd(240)
    e()

def down_t():
    p(-340,-150)
    lt(180)
    f('brown')
    b()

    for x in range(2):
        fd(470)
        lt(90)
        fd(11)
        lt(90)
    e()

def uppr_t():
    p(-340,320)
    lt(90)
    fd(6)
    rt(90)
    f('yellow')
    b()
    rt(90)
    fd(25.0)
    lt(30)
    fd(50)
    lt(60)
    fd(70)
    lt(30)
    fd(10)
    lt(120)
    fd(10)
    lt(30)
    fd(60)
    rt(70)
    fd(50)
    e()

    p(-346,320)
    rt(110)

    b()
    lt(90)
    fd(25.0)
    rt(30)
    fd(50)
    rt(60)
    fd(70)
    rt(30)
    fd(10)
    rt(120)
    fd(10)
    rt(30)
    fd(60)
    lt(70)
    fd(50)
    e()

    p(-346,320)
    lt(10)
    lt(90)
    lt(25)
    b()
    for y in range(2):
        fd(40)
        rt(30)
        fd(40)
        rt(150)
    rt(25)
    e()

def damru():
    f('dark red')
    pencolor('white')
    b()
    p(-346,300)
    lt(10)
    
    lt(60)
    fd(30)
    lt(30)
    fd(10)
    lt(90)
    fd(40)
    lt(90)
    fd(10)
    lt(30)
    fd(30)
    lt(60)
    pencolor('black')
    lt(60)

    fd(10)
    rt(60)

    pencolor('white')

    rt(60)

    fd(30)

    rt(30)

    fd(10)

    rt(90)

    fd(40)

    rt(90)

    fd(10)

    rt(30)

    fd(30)

    rt(60)

    e()
    pencolor('black')

def decor():
    p(0,0)
    pensize(10)
    pencolor('white')
    lt(90)
    fd(280)
    pensize(5)
    bk(280*2)

    pensize(15)
    p(-158,130)
    fd(50)
    bk(100)

    pensize(15)
    p(-158,100)
    fd(50)
    bk(100)

    pensize(2)
    p(0,0)
    lt(90)
    fd(30)
    rt(90)
    fd(280)
    bk(280*2)

stars()
s_head()
s_middle()
s_base()
grass()
snake()
down_t()
uppr_t()
damru()
decor()

done()



















    
