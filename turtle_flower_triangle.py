import turtle

def draw_triangle(some_turtle):
    some_turtle.forward(100)
    some_turtle.left(120)
    some_turtle.forward(50)
    some_turtle.left(90)
    some_turtle.forward(50*3**(1/2.0))
    some_turtle.left(150)

def draw_flower(new_turtle):
    for i in range(1,37):
        draw_triangle(new_turtle)
        new_turtle.right(10)

window = turtle.Screen()
window.bgcolor("red")
Panda2 = turtle.Turtle()
Panda2.shape("turtle")
Panda2.color("yellow")
Panda2.speed(5)
draw_flower(Panda2)
