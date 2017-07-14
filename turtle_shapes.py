import turtle

window = turtle.Screen()
window.bgcolor("red")

def draw_square():
    Pikachu = turtle.Turtle()
    Pikachu.shape("turtle")
    Pikachu.color("yellow")
    Pikachu.speed(2)

    n = 0
    while (n < 4):
        Pikachu.forward(100)
        Pikachu.right(90)
        n = n + 1

def draw_circle():
    Panda1 = turtle.Turtle()
    Panda1.shape("arrow")
    Panda1.color("blue")
    Panda1.speed(2)
    Panda1.circle(100)

def draw_triangle():
    Panda2 = turtle.Turtle()
    Panda2.shape("turtle")
    Panda2.color("black")

    l = 0
    while (l < 3):
        Panda2.forward(100)
        Panda2.right(120)
        l = l + 1

draw_square()
draw_circle()
draw_triangle()
