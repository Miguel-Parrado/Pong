import turtle

vent = turtle.Screen()
vent.title("PONG")
vent.bgcolor("black")
vent.setup(width=650, height=650)
vent.tracer(0)


def solo():
    est = turtle.Turtle()
    est.speed(0)
    est.shape("square")
    est.color("white")
    est.penup()
    est.goto(0, 0)
    est.shapesize(stretch_wid=31, stretch_len=31)

    est2 = turtle.Turtle()
    est2.speed(0)
    est2.shape("square")
    est2.color("black")
    est2.penup()
    est2.goto(0, 0)
    est2.shapesize(stretch_wid=30, stretch_len=30)

    p1 = turtle.Turtle()
    p1.speed(0)
    p1.shape("square")
    p1.color("red")
    p1.penup()
    p1.goto(-290, 0)
    p1.dy = 5
    p1.shapesize(stretch_wid=5, stretch_len=1)

    p2 = turtle.Turtle()
    p2.speed(0)
    p2.shape("square")
    p2.color("cyan")
    p2.penup()
    p2.goto(290, 0)
    p2.shapesize(stretch_wid=5, stretch_len=1)

    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color(1, 1, 1)
    ball.penup()
    ball.goto(0, 0)
    vel = 0.3
    ball.dx = vel
    ball.dy = vel

    conta = 0
    contb = 0

    pun = turtle.Turtle()
    pun.speed(0)
    pun.color("grey")
    pun.penup()
    pun.hideturtle()
    pun.goto(0, 150)
    pun.write(("{}        {}".format(conta, contb)), align="center", font=("system", 40, "normal"))

    def up1():
        """
        :return: hace que la paleta del jugador 1 se mueva coor unidades hacia arriba
        """
        if p1.ycor() >= 240:
            p1.dy = 0
            p1.sety(p1.ycor() + p1.dy)
        else:
            p1.dy = 20
            p1.sety(p1.ycor() + p1.dy)

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
        if p1.ycor() <= -240:
            p1.dy = 0
            p1.sety(p1.ycor() + p1.dy)
        else:
            p1.dy = -20
            p1.sety(p1.ycor() + p1.dy)

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

        if ball.ycor() > 300:
            ball.dy = ball.dy * (-1)

        elif ball.ycor() < -300:
            ball.dy = ball.dy * (-1)

        elif ball.xcor() >= 290:
            ball.goto(0, 0)
            ball.dx = ball.dx * (-1)
            conta = conta + 1
            pun.clear()
            pun.write(("{}        {}".format(conta, contb)), align="center", font=("system", 40, "normal"))

        elif ball.xcor() <= -290:
            ball.goto(0, 0)
            ball.dx = ball.dx * (-1)
            contb = contb + 1
            pun.clear()
            pun.write(("{}        {}".format(conta, contb)), align="center", font=("system", 40, "normal"))

        if ((280 < ball.xcor() + 5)
                and (p2.ycor() + 50 > ball.ycor() > p2.ycor() - 50)):
            ball.dx = ball.dx * (-1)

        elif (-280 > ball.xcor() - 5) and (p1.ycor() + 50 > ball.ycor() > p1.ycor() - 50):
            ball.dx = ball.dx * -1


solo()
