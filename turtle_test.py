import turtle
wn = turtle.Screen()

def makeTurtle(edges):
    for edge in edges:
        for point in edge:
            turtle.goto(point[0] - 100, -point[1] + 100)
            turtle.pendown()
        turtle.penup()
