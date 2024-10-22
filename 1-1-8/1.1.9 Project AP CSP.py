#Picture Idea - Landscape: grass, clouds, sun.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

def clouds():
    painter.setheading(90)
    painter.pendown()
    for circle in range (2):
        painter.begin_fill()
        painter.fillcolor("white")
        painter.circle(25)
        painter.end_fill()
        painter.penup()
        painter.right(90)
        painter.begin_fill()
        painter.fillcolor("white")
        painter.pendown()
        painter.circle(25)
        painter.end_fill()
    painter.penup()

def sky():
    painter.begin_fill()
    painter.fillcolor("skyblue")
    for side in range(2):
        painter.forward(498)
        painter.right(90)
        painter.forward(422)
        painter.right(90)
    painter.end_fill()

#Picture border
painter.pensize(3)
painter.color('black')
painter.penup()
painter.goto(-250,-250 )
painter.pendown()
for side in range(4):
    painter.forward(500)
    painter.left(90)
painter.penup()

#Setting Sky up
painter.pensize(1)
painter.goto(-249,249)
painter.pendown()
sky()
painter.penup()

#Setting Up Tree
painter.goto(0,-173)
painter.setheading(90)
painter.color("brown")

#Creating tree trunk
painter.pendown()
painter.pensize(45)
painter.forward(225)
painter.penup()

#Creating leaves
painter.pensize(1)
painter.color('green')
painter.pendown()
for circles in range(3):
    painter.begin_fill()
    painter.fillcolor("green")
    painter.circle(50)
    painter.end_fill()
    painter.penup()
    painter.right(90)
    painter.begin_fill()
    painter.fillcolor("green")
    painter.pendown()
    painter.circle(50)
    painter.end_fill()
painter.penup()



#Setting grass up
painter.pensize(1)
painter.goto(-249,-249)
painter.setheading(90)
painter.pendown()

#Creating grass
painter.begin_fill()
painter.fillcolor("lightgreen")
for side in range(2):
    painter.forward(75)
    painter.right(90)
    painter.forward(498)
    painter.right(90)
painter.end_fill()
painter.penup()

#Creating clouds
painter.goto(-100, 150)
clouds()

painter.goto(200,0)
clouds()

painter.goto(-175,0)
clouds()

#Setting Up Sun
painter.penup()
painter.pensize(1)
painter.goto(173,173)
painter.speed(3)
painter.color("yellow")
painter.shape("circle")
painter.setheading(180)
painter.forward(400)

wn = trtl.Screen()
wn.mainloop()



