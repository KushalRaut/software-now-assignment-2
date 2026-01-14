import turtle

def edge(length, depth):
    if depth == 0:
        turtle.forward(length)
        return

    length /= 3

    edge(length, depth - 1)
    turtle.right(60)
    edge(length, depth - 1)
    turtle.left(120)
    edge(length, depth - 1)
    turtle.right(60)
    edge(length, depth - 1)

def square(sides, length, depth):
    angle = 360/sides
    for _ in range(sides):
        edge(length, depth)
        turtle.right(angle)   # CLOCKWISE square (critical)

# -------- MAIN --------
# turtle.speed(0)
# turtle.hideturtle()
# turtle.setup(800, 800)

# side_length = 300
# depth = 3
sides = int(input("Enter the number of sides: "))
length = int(input("Enter the number of length: "))
depth = int(input("Enter the number of depth: "))

turtle.speed(0)
turtle.hideturtle()
turtle.setup(800, 800)
# turtle.penup()
# turtle.goto(-150, 150)
# turtle.setheading(0)      # face right
# turtle.pendown()
turtle.penup()
turtle.goto(-length/2, length/2)
turtle.setheading(0)      # face right
turtle.pendown()
square(sides, length, depth)

turtle.done()