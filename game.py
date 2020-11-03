import turtle

vent = turtle.Screen()
vent.title("PONG")
vent.bgcolor("black")
vent.setup(width=810, height=610)
vent.tracer(0)

p1 = turtle.Turtle()
p1.speed(0)
p1.shape("square")
p1.color("red")
p1.penup()
p1.goto(-390,0)
p1.shapesize(stretch_wid = 5, stretch_len =1)

p2 = turtle.Turtle()
p2.speed(0)
p2.shape("square")
p2.color("cyan")
p2.penup()
p2.goto(390,0)
p2.shapesize(stretch_wid = 5, stretch_len =1)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = 0.5

est = turtle.Turtle()
est.speed(0)
est.shape("square")
est.color("white")
est.penup()
est.goto(0,0)
est.shapesize(stretch_wid =30, stretch_len =0.2)

conta = 0
contb = 0

pun = turtle.Turtle()
pun.speed(0)
pun.color("grey")
pun.penup()
pun.hideturtle()
pun.goto(0,250)
pun.write(("{}        {}".format(conta,contb)), align = "center", font = ("system", 40, "normal"))

def up1():
    """
    :return: hace que la paleta del jugador 1 se mueva coor unidades hacia arriba
    """
    coor = p1.ycor()
    coor = coor + 20
    p1.sety(coor)
def up2():
    """
    :return: hace que la paleta del jugador 2 se mueva coor unidades hacia arriba
    """
    coor = p2.ycor()
    coor = coor + 20
    p2.sety(coor)
def down1():
    """
        :return: hace que la paleta del jugador 1 se mueva coor unidades hacia abajo
        """
    coor = p1.ycor()
    coor = coor - 20
    p1.sety(coor)
def down2():
    """
        :return: hace que la paleta del jugador 2 se mueva coor unidades hacia abajo
        """
    coor = p2.ycor()
    coor = coor - 20
    p2.sety(coor)

vent.listen()
vent.onkeypress(up1, "w")
vent.onkeypress(up2, "Up")
vent.onkeypress(down1, "s")
vent.onkeypress(down2, "Down")

while True:
    vent.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.dy = ball.dy * (-1)
    elif ball.ycor() < -300:
        ball.dy = ball.dy * (-1)
    elif ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx = ball.dx * (-1)
        conta = conta + 1
        pun.clear()
        pun.write(("{}        {}".format(conta, contb)), align="center", font=("system", 40, "normal"))

    elif ball.xcor() < -400:
        ball.goto(0,0)
        ball.dx = ball.dx * (-1)
        contb = contb + 1
        pun.clear()
        pun.write(("{}        {}".format(conta, contb)), align="center", font=("system", 40, "normal"))

    if ((ball.xcor() > 380 and ball.xcor() < 400)
        and (ball.ycor() < p2.ycor() + 50
        and ball.ycor() > p2.ycor() - 50)):
        ball.dx = ball.dx * (-1)
    elif ((ball.xcor() < -380 and ball.xcor() > -400)
        and (ball.ycor() < p1.ycor() + 50
        and ball.ycor() > p1.ycor() - 50)):
        ball.dx = ball.dx * (-1)