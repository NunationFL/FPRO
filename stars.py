import turtle
bicho = turtle.Turtle()
sc = turtle.Screen ()
bicho.shape("circle")
sc.bgcolor ("blue")
bicho.color("white")
bicho.pensize(3)
n=int(input("How many sides shall your star be made of? "))
for _ in range (n):
    bicho.fd(135)
    bicho.stamp()
    bicho.bk(135)
    bicho.lt(360/n)
sc.exitonclick ()
turtle.bye ()