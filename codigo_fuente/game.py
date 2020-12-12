import turtle
import requests
from bs4 import BeautifulSoup


def usu(a, b):
    """
    Se encarga del LOGIN del usuario, en caso de no tener una cuenta existente, se crea automaticamente
    :param a: Nombre de usuario
    :param b: Contraseña
    :return: True or False
    """
    user = a
    pasw = b
    cb = (a, b)
    f = open("u.txt", "r+")
    k = open("c.txt", "r+")
    c = 0
    lf = f.readline()
    lk = k.readline()
    lf = lf.split(",")
    lf = list(map(str, lf))
    lk = lk.split(",")
    lk = list(map(str, lk))
    if user not in lf:
        f.write(user)
        f.write(",")
        f.close()
        k.write(pasw)
        k.write(",")
        k.close()
        return True
    else:
        ii = lf.index(user)
    if lk[ii] != pasw:
        return False
    else:
        return True


def ujmenu():
    """
    Parametriza el menú de selección de colores en el modo de un jugador
    :return:
    """
    txt = turtle.Turtle()
    global prin, uj, selj, vent
    selj = False
    uj = True

    global vent
    vent.title("PONG")
    vent.bgcolor("black")
    vent.setup(width=650, height=650)
    vent.tracer(0)

    est1 = turtle.Turtle()
    est1.speed(0)
    est1.shape("square")
    est1.color("white")
    est1.penup()
    est1.goto(0, 150)
    est1.shapesize(stretch_wid=5, stretch_len=1)

    txt.color("white")
    txt.penup()
    txt.hideturtle()
    txt.goto(0, -250)
    txt.write("╣Regresar╠", align="center", font=("System", 40, "normal"))
    txt.goto(0, -290)
    txt.write("Tecla Esc", align="center", font=("System", 5, "normal"))

    col = turtle.Turtle()
    col.speed(0)
    col.color("black")
    col.penup()
    col.hideturtle()
    xcor = -190
    for i in range(10):
        l = ["black", "brown", "red1", "Darkorange1", "gold", "LimeGreen", "cyan2", "DodgerBlue3", "purple4", "pink"]
        color = l[i]
        col.color(color)
        col.write("■", align="center", font=("System", 40, "normal"))
        col.goto(xcor, 20)
        xcor += 48

    but = ["black", "brown", "red1", "Darkorange1", "gold", "LimeGreen", "cyan2", "DodgerBlue3", "purple4", "pink"]
    but2 = [235, -188, -141, -96, -43, 0, 43, 96, 141, 188]

    def izq1():
        """
        Define el movimiento a la izquierda del usuario
        :return:
        """
        global cont3

        if uj == True:
            cont3 -= 1
            if cont3 < 1:
                cont3 = 9
            est1.color(but[cont3])
            est1.goto(but2[cont3], 150)

    def der1():
        """
        Define el movimiento a la derecha del usuario
        :return:
        """
        global cont3

        if uj == True:
            cont3 += 1
            if cont3 > 9:
                cont3 = 1
            est1.color(but[cont3])
            est1.goto(but2[cont3], 150)

    def esc():
        """
        Regresa al usuario al menú principal
        :return:
        """
        global dir1
        dir1 = 0
        if dj == True:
            vent.clear()
            pm()

    def ente():
        """
        Inicia el juego de un solo jugador
        :return:
        """
        global dir1
        dir1 = 0
        if uj == True:
            vent.clear()
            solo2()

    vent.listen()
    vent.onkeypress(izq1, "Left")
    vent.onkeypress(der1, "Right")
    vent.onkeypress(esc, "Escape")
    vent.onkeypress(izq1, "Down")
    vent.onkeypress(der1, "Up")
    vent.onkeypress(ente, "Return")


def djmenu():
    """
    Parametriza el menu de selección de colores en modo de dos jugadores
    :return:
    """
    txt = turtle.Turtle()
    global prin, dj, selj, vent
    selj = False
    dj = True

    global vent
    vent.title("PONG")
    vent.bgcolor("black")
    vent.setup(width=650, height=650)
    vent.tracer(0)

    est1 = turtle.Turtle()
    est1.speed(0)
    est1.shape("square")
    est1.color("white")
    est1.penup()
    est1.goto(0, 150)
    est1.shapesize(stretch_wid=5, stretch_len=1)

    est2 = turtle.Turtle()
    est2.speed(0)
    est2.shape("square")
    est2.color("white")
    est2.penup()
    est2.goto(0, -50)
    est2.shapesize(stretch_wid=5, stretch_len=1)

    txt.color("white")
    txt.penup()
    txt.hideturtle()
    txt.goto(0, -250)
    txt.write("╣Regresar╠", align="center", font=("System", 40, "normal"))
    txt.goto(0, -290)
    txt.write("Tecla Esc", align="center", font=("System", 5, "normal"))

    col = turtle.Turtle()
    col.speed(0)
    col.color("black")
    col.penup()
    col.hideturtle()
    xcor = -190
    for i in range(10):
        l = ["black", "brown", "red1", "Darkorange1", "gold", "LimeGreen", "cyan2", "DodgerBlue3", "purple4", "pink"]
        color = l[i]
        col.color(color)
        col.write("■", align="center", font=("System", 40, "normal"))
        col.goto(xcor, 20)
        xcor += 48

    but = ["black", "brown", "red1", "Darkorange1", "gold", "LimeGreen", "cyan2", "DodgerBlue3", "purple4", "pink"]
    but2 = [235, -188, -141, -96, -43, 0, 43, 96, 141, 188]

    def izq1():
        """
        Define el movimiento a la izquierda del jugador 1
        :return:
        """
        global cont3

        if dj == True:
            cont3 -= 1
            if cont3 < 1:
                cont3 = 9
            est1.color(but[cont3])
            est1.goto(but2[cont3], 150)

    def der1():
        """
        Define el movimiento a la derecha del jugador 1
        :return:
        """
        global cont3

        if dj == True:
            cont3 += 1
            if cont3 > 9:
                cont3 = 1
            est1.color(but[cont3])
            est1.goto(but2[cont3], 150)

    def izq2():
        """
        Define el movimiento a la izquierda del jugador 2
        :return:
        """
        global cont4

        if dj == True:
            cont4 -= 1
            if cont4 < 1:
                cont4 = 9
            est2.color(but[cont4])
            est2.goto(but2[cont4], -50)

    def der2():
        """
        Define el movimiento a la derecha del jugador 2
        :return:
        """
        global cont4

        if dj == True:
            cont4 += 1
            if cont4 > 9:
                cont4 = 1
            est2.color(but[cont4])
            est2.goto(but2[cont4], -50)

    def esc():
        """
        Permite salir a los jugadores al menú principal
        :return:
        """
        global dir1
        dir1 = 0
        if dj == True:
            vent.clear()
            pm()

    def ente():
        """
        Permite entrar a los jugadores al juedo de dos
        :return:
        """
        global dir1
        dir1 = 0
        if dj == True:
            vent.clear()
            solo()

    vent.listen()
    vent.onkeypress(izq1, "Left")
    vent.onkeypress(der1, "Right")
    vent.onkeypress(izq2, "a")
    vent.onkeypress(der2, "d")
    vent.onkeypress(esc, "Escape")
    vent.onkeypress(izq1, "Down")
    vent.onkeypress(der1, "Up")
    vent.onkeypress(izq2, "s")
    vent.onkeypress(der2, "w")
    vent.onkeypress(ente, "Return")


def gmenu(x):
    """
    Parametriza la selección del modo de juego, o el retornar al menú principal
    :param x: cuando 0, permite la salida al menú principal, cuando 1, abre el menú de selección, cuando 2, abre el menú de el modo de juego de dos jugadores, cuando 3, permite el modo de juejo de 1 jugador
    :return:
    """
    txt = turtle.Turtle()
    global prin, selj, uj, dj, vent, dir1
    prin = False
    selj = True

    if x == 1:
        txt.speed(0)
        txt.color("white")
        txt.penup()
        txt.hideturtle()
        txt.goto(0, 170)
        txt.write("Un jugador", align="center", font=("System", 55, "normal"))
        txt.goto(0, -80)
        txt.write("Dos Jugadores", align="center", font=("System", 55, "normal"))
        txt.goto(0, -250)
        txt.write("╣Regresar╠", align="center", font=("System", 40, "normal"))
    elif x == 0:
        dir1 = 1
        vent.clear()
        pm()
    elif x == 2:
        dir1 = 1
        vent.clear()
        djmenu()
    elif x == 3:
        dir1 = 1
        vent.clear()
        ujmenu()


def webs(x):
    """
    Permite la obtención de la definición de Pong, de la página Wikipedia
    :param x: cuando 1, abre el menú de información. Cuando 0, permite salir al menú principal
    :return:
    """
    global inf, prin
    inf = True
    prin = False
    res = requests.get(url="https://es.wikipedia.org/wiki/Pong", )
    soup = BeautifulSoup(res.content, 'html.parser')
    text = soup.get_text()
    div = [line for line in text.split("\n") if line != ""]

    ntext = []

    for i in range(len(div)):
        a = div[i]
        if "Juego[editar]" == a:
            ntext = div[i + 1]
            ntext = ntext[:-4]

    ntext = ntext.split()
    va = list(map(str, ntext))
    va.append("-1")

    b = 40
    n = 0
    lin = []
    ont = 0
    m = []

    for i in range(len(va)):
        d = va[i] + " "
        c = len(d)
        n = c + n

        if d == "-1 ":
            if lin:
                e = "".join(map(str, lin)).strip(" ")
                m.append(e)
                lin = []
                ont = ont + 1

        elif (n + len(va[i + 1]) + 1) > b + 1:
            lin.append(d)
            n = 0
            e = "".join(map(str, lin)).strip(" ")
            m.append(e)
            lin = []
            ont = ont + 1
        else:
            lin.append(d)
    txt = turtle.Turtle()

    if x == 1:
        txt.speed(0)
        txt.color("white")
        txt.penup()
        txt.hideturtle()
        ypos = 250
        for i in range(ont):
            ypos -= 30
            txt.goto(0, ypos)
            txt.write(m[i], align="center", font=("System", 20, "normal"))
        ypos = -270
        txt.goto(260, ypos)
        txt.write("ENTER para salir", align="center", font=("System", 5, "normal"))
    elif x == 0:
        global vent
        vent.clear()
        pm()


vent = turtle.Screen()
vent.title("PONG")
vent.bgcolor("black")
vent.setup(width=650, height=650)
vent.tracer(0)
cont = 0
cont2 = 0
dir1 = 0
dir2 = 0
prin = True
inf = False
selj = False
uj = False
ujl = False
dj = False
djl = False
cont3 = 0
cont4 = 0
col1 = 0
col2 = 0


def pm():
    """
    Menú principal, da las opciones de empezar a jugar, o ir al menú de información
    :return:
    """
    global inf, selj, uj, dj
    prin = True
    inf = False
    selj = False
    uj = False
    dj = False

    global vent
    vent.title("PONG")
    vent.bgcolor("black")
    vent.setup(width=650, height=650)
    vent.tracer(0)

    est = turtle.Turtle()
    est.speed(0)
    est.shape("square")
    est.color("white")
    est.penup()
    est.goto(0, -15)
    est.shapesize(stretch_wid=1, stretch_len=1)

    pun = turtle.Turtle()
    pun.speed(0)
    pun.color("white")
    pun.penup()
    pun.hideturtle()
    pun.goto(0, 230)
    pun.write("PONG", align="center", font=("System", 60, "normal"))
    pun.goto(1, 35)
    pun.write("w", align="center", font=("System", 20, "normal"))
    pun.goto(1, 0)
    pun.write("↑", align="center", font=("System", 20, "normal"))
    pun.goto(0, 80)
    pun.write("Mover ■ con", align="center", font=("System", 20, "normal"))
    pun.goto(0, -30)
    pun.write("a ←    → d", align="center", font=("System", 20, "normal"))
    pun.goto(1, -60)
    pun.write("↓", align="center", font=("System", 20, "normal"))
    pun.goto(1, -95)
    pun.write("s", align="center", font=("System", 20, "normal"))
    pun.goto(0, -140)
    pun.write("Y seleccionar con ENTER", align="center", font=("System", 10, "normal"))
    pun.goto(0, -300)
    pun.write("redesign by: Miguel Parrado", align="center", font=("System", 5, "normal"))
    pun.goto(280, -300)
    pun.write("ⓘ", align="center", font=("System", 40, "normal"))
    pun.goto(0, 150)
    pun.write("Controles", align="center", font=("System", 30, "normal"))
    pun.goto(0, -100)
    pun.write("Jugador 1                                            Jugador 2", align="center",
              font=("System", 26, "normal"))
    pun.goto(0, 0)
    pun.write("      ↑                                       w     ", align="center", font=("System", 35, "normal"))
    pun.goto(0, -200)
    pun.write("      ↓                                       s     ", align="center", font=("System", 35, "normal"))
    pun.goto(0, -250)
    pun.write("╣Jugar╠", align="center", font=("System", 40, "normal"))

    but = [(0, -170), (278, -230)]
    but2 = [(0, -170), (0, 260), (0, 0)]

    def izq():
        """
        Permite el movimiento del puntero hacia la izquierda
        :return:
        """

        global cont, cont2

        if prin == True:
            cont -= 1
            if cont < 0:
                cont = 1
            est.goto(but[cont])

        if inf == True:
            cont = 1
            est.goto(but[cont])

        if selj == True:
            cont2 -= 1
            if cont2 < 0:
                cont2 = 2
            est.goto(but2[cont2])

    def der():
        """
        Permite el movimiento del puntero a la derecha
        :return:
        """

        global cont, cont2

        if prin == True:
            cont += 1
            if cont > 1:
                cont = 0
            est.goto(but[cont])

        if inf == True:
            cont = 1
            est.goto(but[cont])

        elif selj == True:
            cont2 += 1
            if cont2 > 2:
                cont2 = 0
            est.goto(but2[cont2])

    def ent():
        """
        Permite seleccionar según donde se ubique el puntero
        :return:
        """
        global dir1, cont, vent
        dir1 += 1

        if dir1 > 1:
            dir1 = 0

        if est.xcor() == 278:
            pun.clear()
            webs(dir1)

        if est.ycor() == -170:
            pun.clear()
            gmenu(dir1)

        if est.ycor() == 0 and selj == True:
            gmenu(2)

        if est.ycor() == 260 and selj == True:
            gmenu(3)

    vent.listen()
    vent.onkeypress(der, "Right")
    vent.onkeypress(izq, "Left")
    vent.onkeypress(ent, "Return")
    vent.onkeypress(der, "a")
    vent.onkeypress(izq, "d")
    vent.onkeypress(der, "s")
    vent.onkeypress(izq, "w")
    vent.onkeypress(der, "Down")
    vent.onkeypress(izq, "Up")

    while True:
        vent.update()


def solo():
    """
    Define el juego de dos personas. al llegar a 10 puntos, se devuelve automaticamente al menú principal
    :return:
    """
    global cont3, cont4
    global vent
    vent.title("PONG")
    vent.bgcolor("black")
    vent.setup(width=650, height=650)
    vent.tracer(0)
    l = ["white", "brown", "red1", "Darkorange1", "gold", "LimeGreen", "cyan2", "DodgerBlue3", "purple4", "pink"]

    est = turtle.Turtle()
    est.speed(0)
    est.shape("square")
    est.color("white")
    est.penup()
    est.goto(0, 0)
    est.shapesize(stretch_wid=50, stretch_len=.2)

    est2 = turtle.Turtle()
    est2.speed(0)
    est2.shape("square")
    est2.color("black")
    est2.penup()
    est2.goto(0, 0)
    est2.shapesize(stretch_wid=1, stretch_len=1)

    p1 = turtle.Turtle()
    p1.speed(0)
    p1.shape("square")
    p1.color(l[cont3])
    p1.penup()
    p1.goto(-290, 0)
    p1.dy = 5
    p1.shapesize(stretch_wid=5, stretch_len=1)

    p2 = turtle.Turtle()
    p2.speed(0)
    p2.shape("square")
    p2.color(l[cont4])
    p2.penup()
    p2.goto(290, 0)
    p2.dy = 5
    p2.shapesize(stretch_wid=5, stretch_len=1)

    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color(1, 1, 1)
    ball.penup()
    ball.goto(0, 0)
    vel = 0.2
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
        :return: hace que la paleta del jugador 2 se mueva hacia arriba
        """
        if p2.ycor() >= 240:
            p2.dy = 0
            p2.sety(p2.ycor() + p2.dy)
        else:
            p2.dy = 20
            p2.sety(p2.ycor() + p2.dy)

    def down1():
        """
            :return: hace que la paleta del jugador 1 se mueva hacia abajo
            """
        if p1.ycor() <= -240:
            p1.dy = 0
            p1.sety(p1.ycor() + p1.dy)
        else:
            p1.dy = -20
            p1.sety(p1.ycor() + p1.dy)

    def down2():
        """
            :return: hace que la paleta del jugador 2 se mueva hacia abajo
            """
        if p2.ycor() <= -240:
            p2.dy = 0
            p2.sety(p2.ycor() + p2.dy)
        else:
            p2.dy = -20
            p2.sety(p2.ycor() + p2.dy)

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
            ball.dy = ball.dy * -1
            conta = conta + 1
            pun.clear()
            pun.write(("{}        {}".format(conta, contb)), align="center", font=("system", 40, "normal"))

        elif ball.xcor() <= -290:
            ball.goto(0, 0)
            ball.dx = ball.dx * (-1)
            contb = contb + 1
            ball.dy = ball.dy * -1
            pun.clear()
            pun.write(("{}        {}".format(conta, contb)), align="center", font=("system", 40, "normal"))

        if ((280 < ball.xcor() + 5)
                and (p2.ycor() + 50 > ball.ycor() > p2.ycor() - 50)):
            ball.dx = ball.dx * (-1)

        elif (-280 > ball.xcor() - 5) \
                and (p1.ycor() + 50 > ball.ycor() > p1.ycor() - 50):
            ball.dx = ball.dx * -1

        if contb == 10 or conta == 10:
            vent.clear()
            pm()
            break


def solo2():
    """
    Ejecuta el juego de un solo jugador. al momento en que la pelota pase de la paleta, se pierde automaticamente. no existen puntajes.
    :return:
    """
    global cont3, cont4
    global vent
    vent.title("PONG")
    vent.bgcolor("black")
    vent.setup(width=650, height=650)
    vent.tracer(0)
    l = ["white", "brown", "red1", "Darkorange1", "gold", "LimeGreen", "cyan2", "DodgerBlue3", "purple4", "pink"]

    est = turtle.Turtle()
    est.speed(0)
    est.shape("square")
    est.color("white")
    est.penup()
    est.goto(0, 0)
    est.shapesize(stretch_wid=50, stretch_len=.2)

    est2 = turtle.Turtle()
    est2.speed(0)
    est2.shape("square")
    est2.color("black")
    est2.penup()
    est2.goto(0, 0)
    est2.shapesize(stretch_wid=1, stretch_len=1)

    p1 = turtle.Turtle()
    p1.speed(0)
    p1.shape("square")
    p1.color(l[cont3])
    p1.penup()
    p1.goto(-290, 0)
    p1.dy = 5
    p1.shapesize(stretch_wid=5, stretch_len=1)

    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color(1, 1, 1)
    ball.penup()
    ball.goto(0, 0)
    vel = 0.2
    ball.dx = vel
    ball.dy = vel

    def up1():
        """
        :return: hace que la paleta del jugador se mueva coor hacia arriba
        """
        if p1.ycor() >= 240:
            p1.dy = 0
            p1.sety(p1.ycor() + p1.dy)
        else:
            p1.dy = 20
            p1.sety(p1.ycor() + p1.dy)

    def down1():
        """
            :return: hace que la paleta del jugador se mueva hacia abajo
            """
        if p1.ycor() <= -240:
            p1.dy = 0
            p1.sety(p1.ycor() + p1.dy)
        else:
            p1.dy = -20
            p1.sety(p1.ycor() + p1.dy)

    vent.listen()
    vent.onkeypress(up1, "w")
    vent.onkeypress(up1, "Up")
    vent.onkeypress(down1, "s")
    vent.onkeypress(down1, "Down")

    while True:
        vent.update()

        ball.setx(ball.xcor() + ball.dx)

        ball.sety(ball.ycor() + ball.dy)

        if ball.ycor() > 300:
            ball.dy = ball.dy * (-1)

        elif ball.ycor() < -300:
            ball.dy = ball.dy * (-1)

        elif ball.xcor() >= 290:
            ball.dx = ball.dx * (-1)

        elif ball.xcor() <= -290:
            vent.clear()
            pm()
            break

        elif (-280 > ball.xcor() - 5) \
                and (p1.ycor() + 50 > ball.ycor() > p1.ycor() - 50):
            ball.dx = ball.dx * -1


sc = turtle.Screen()
sc.setup(400, 300)
e = False
nn = 0

pun = turtle.Turtle()
pun.speed(0)
pun.color("white")
pun.penup()
pun.hideturtle()
pun.goto(0, 0)
pun.write("LOGIN", align="center", font=("system", 40, "normal"))

while e == False:
    if nn > 0:
        pun.clear()
        pun.write("intentelo de nuevo", align="center", font=("system", 40, "normal"))

    a = turtle.textinput("Login", "Usuario")
    b = turtle.textinput("Login", "contraseña")
    e = usu(a, b)
    nn += 1
sc.clear()
pm()
