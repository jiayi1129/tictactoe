from turtle import Turtle
import time
import math

def drawcircle(x, y):
    circle = Turtle()
    circle.hideturtle()
    circle.penup()
    circle.pencolor("blue")
    circle.shape("circle")
    circle.shapesize(8,8,5)
    circle.speed(0)
    circle.setpos(x, y)
    circle.forward(0)
    circle.showturtle()

def drawcross(x, y):
    cross = Turtle()
    cross.hideturtle()
    cross.pensize(5)
    cross.color("red")
    cross.penup()
    cross.setposition(x-50, y+50)
    cross.pendown()
    cross.setposition(x+50, y-50)
    cross.penup()
    cross.setposition(x+50, y+50)
    cross.pendown()
    cross.setposition(x-50, y-50)
    cross.speed(0)
    cross.setpos(x, y)
    cross.speed(0)
    cross.penup()
    cross.forward(0)

class Box(Turtle):

    turn = "O"

    def __init__(self, x, y):
        Turtle.__init__(self)
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.fillcolor("")
        self.shape("square")
        self.shapesize(10,10,5)
        self.speed(0)
        self.setpos(x, y)
        self.value = None
        self.showturtle()

    def clicked(self, x, y):
        x, y = self.xcor(), self.ycor()

        if self.value == None:
            self.value = Box.turn
            Box.turn = None
            if self.value == "O":
                drawcircle(x, y)
                Box.turn = "X"
            elif self.value == "X":
                drawcross(x, y)
                Box.turn = "O"

class Victory(Turtle):
    def __init__(self, player):
        Turtle.__init__(self, visible = False)
        self.penup()
        self.color("white")
        self.setpos(-450, 0)
        self.forward(0)
        self.write("{} wins!".format(player), font = ("Arial", 20, "normal"))

        # reset game
        time.sleep(2)
        self.clear()

class Machine(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.setpos(400, 0)
        self.shape("square")
        self.shapesize(5, 5, 5)
        self.pencolor("red")
        self.forward(0)

class Best_move():
    def __init__(self):
        self.Xvalue = math.inf
        self.Ovalue = -math.inf
        self.Xx = None
        self.Xy = None
        self.Ox = None
        self.Oy = None
        self.depth = 0
