import turtle




def dreptunghi():
    t = turtle.Pen()
    t.up()
    t.goto(-50, 50)
    t.down()

    t.fillcolor("red")

    for _ in range(2):
        t.begin_fill()
        t.forward(200)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.end_fill()

    t.up()
    t.goto(25, 13)
    t.down()

    t.fillcolor("pink")

    for _ in range(2):
        t.begin_fill()
        t.forward(50)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.end_fill()
        t.reset()

def inimioara():
    t = turtle.Pen()
    t.up()
    t.goto(-50, 50)
    t.down()

    t.color("red")
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.setheading(60)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()
    t.reset()

def casute():
    t = turtle.Pen()
    x = turtle.Pen()
    # casa 1
    t.up()
    t.goto(-250, -100)
    t.down()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(4):
        t.forward(200)
        t.left(90)
    t.end_fill()
    t.fillcolor("brown")
    t.up()
    t.goto(-190, -100)
    t.down()
    t.begin_fill()
    for _ in range(2):
        t.forward(75)
        t.left(90)
        t.forward(80)
        t.left(90)
    t.end_fill()
    t.fillcolor("blue")
    t.begin_fill()
    # geam
    t.up()
    t.goto(-155, 10)
    t.down()
    t.circle(35)
    t.end_fill()
    # acoperis
    t.fillcolor("brown")
    t.begin_fill()
    t.up()
    t.goto(-250, 100)
    t.down()
    t.forward(200)
    t.left(120)
    t.forward(200)
    t.left(120)
    t.forward(200)
    t.end_fill()
    # casa 2

    x.up()
    x.goto(0, -100)
    x.down()
    for _ in range(4):
        x.forward(200)
        x.left(90)
    x.fillcolor("green")
    x.begin_fill()
    x.up()
    x.goto(60, -100)
    x.down()
    for _ in range(2):
        x.forward(75)
        x.left(90)
        x.forward(80)
        x.left(90)
    x.end_fill()
    x.fillcolor("blue")
    x.begin_fill()
    # geam
    x.up()
    x.goto(95, 10)
    x.down()
    x.circle(35)
    x.end_fill()
    # acoperie
    x.fillcolor("green")
    x.begin_fill()
    x.up()
    x.goto(0, 100)
    x.down()
    x.forward(200)
    x.left(120)
    x.forward(200)
    x.left(120)
    x.forward(200)

    x.end_fill()

while True:
    alegere = input("Alege o desenare:\n1. Dreptunghiuri\n2. Inimă\n3. Case\nOrice altă tastă pentru a ieși.\nAlegerea ta: ")

    if alegere == "1":
        dreptunghi()
    elif alegere == "2":
        inimioara()
    elif alegere == "3":
        casute()
    else:
        break  # Exit the loop when any other key is pressed

turtle.done()  # Close the Turtle graphics window when exiting
