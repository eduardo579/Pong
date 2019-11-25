import turtle
import os
#import winsound

wn = turtle.Screen()
wn.title("Ping-pong por Eduardo")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Puntos

score_a = 0
score_b = 0


# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)



# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Bola

bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.2
bola.dy = 0.2


# Objeto

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Jugador 1: {}  Jugador 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


# Funciones

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Teclado: eventos

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Loop de inicio

while True:
    wn.update()

    # Mover la bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Límites de pantalla
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1
        os.system("aplay bounce.wav&")
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1
        os.system("aplay bounce.wav&")
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Jugador 1: {}  Jugador 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Jugador 1: {}  Jugador 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    
    # Devolver la bola
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < paddle_b.ycor() + 40 and bola.ycor() > paddle_b.ycor() - 40):
        os.system("aplay bounce.wav&")
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        bola.setx(340)
        bola.dx *= -1

    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < paddle_a.ycor() + 40 and bola.ycor() > paddle_a.ycor() - 40):
        os.system("aplay bounce.wav&")
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        bola.setx(-340)
        bola.dx *= -1