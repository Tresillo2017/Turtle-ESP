from turtle import *
from random import randint

def square():
    color(pr2)
    width(g)
    left(90)
    forward(200)
    #color("red")
    #width(12)
    right(90)
    forward(200)
    #color("blue")
    #width(5)
    right(90)
    forward(200)
    #color("purple")
    #width(13)
    right(90)
    forward(200)
def triangle():
    for i in range(3):
        width(g)
        color(pr2)
        forward(150)
        left(120)
        width(randint(1,8))
def rombo():
        width(g)
        color(pr2)
        left(45)
        forward(100)
        for i in range(3):
            left(90)
            forward(100)
def cruz():
    color(pr2)
    width(g)
    #color("red")
    begin_fill()
    left(90)
    forward(40)
    #color("blue")
    left(90)
    forward(40)
    right(90)
    forward(100)
    right(90)
    forward(40)
    left(90)
    forward(40)
    right(90)
    forward(90)
    right(90)
    forward(40)
    left(90)
    forward(40)
    right(90)
    forward(100)
    right(90)
    forward(40)
    left(90)
    #color("green")
    forward(40)
    #color("blue")
    right(90)
    forward(90)
    color(re)
    end_fill()
for i in range(5):
    pr = input("Que figura quieres dibujar (square, triangle, rombo, cruz): ")
    pr2 = input("De que color quieres la figura? (En ingles): ")
    gr = input("Que grosor quieres?, tambien pudes ponerlo aleatorio escribiendo la palabra 'aleatorio': ")
    if gr == "aleatorio":
        g = randint(1, 10)
    else:
        g = int(gr)
    if pr == "square":
        square()
        if pr == "triangle":
            triangle()
            if pr == "rombo":
                rombo()
                if pr == "cruz":
                    re = input("De que color quieres el relleno? (En ingles): ")
                    cruz()              
else:
    print("Lo siento esa figura no esta en la base de datos")
exitonclick()

