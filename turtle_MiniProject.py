import turtle

def draw_triangle(some_turtle):
    some_turtle.right(60)
    for i in range(1,4):
        some_turtle.forward(30)
        some_turtle.right(120)
    some_turtle.left(60)

def draw_triangles(new_turtle):
    for n in range(-7,8):
        m = abs(n)
        new_turtle.up()
        new_turtle.goto(15*n, -15*(3**(1/2.0))*m)
        new_turtle.down()
        draw_triangle(new_turtle)

    for p in (-5,-3,-1,1,3,5):
        q = abs(p)
        new_turtle.up()
        new_turtle.goto(15*p, -15*(3**(1/2.0))*(q+2))
        new_turtle.down()
        draw_triangle(new_turtle)

    for j in (-1,1):
        new_turtle.up()
        new_turtle.goto(-30*j, -90*(3**(1/2.0)))
        new_turtle.down()
        draw_triangle(new_turtle)

    for k in (-3,-1,1,3):
        new_turtle.up()
        new_turtle.goto(15*k, -15*(3**(1/2.0))*7)
        new_turtle.down()
        draw_triangle(new_turtle)

window = turtle.Screen()
window.bgcolor("red")
Panda2 = turtle.Turtle()
Panda2.shape("turtle")
Panda2.color("yellow")
Panda2.speed(1)
draw_triangles(Panda2)

