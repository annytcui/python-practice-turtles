import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    # Create a turtle Panda2 - Draw a square
    Panda2 = turtle.Turtle()
    Panda2.shape("turtle")
    Panda2.color("yellow")
    Panda2.speed(2)
    for i in range(1,37):
        draw_square(Panda2)
        Panda2.right(10)

draw_art()
