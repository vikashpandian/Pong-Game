import turtle

width = 1280
height = 720
pad_pos = width / 2 - 30
pad_len = height / 12
pad_len_factor = pad_len / 10
ver_lmt = height / 2 - 10
hor_lmt = width / 2 + 10
move_val = 20
score_pos = height / 2 - 40

win = turtle.Screen()
win.title("Pong by Vikash")
win.bgcolor("#0a0b4b")
win.setup(width, height)
win.tracer(0)


# Paddle
class Paddle(turtle.Turtle):
    def __init__(self, stretch_len, color, x):
        super().__init__()
        self.speed(0)  # max_possible
        self.shape("square")  # default_size 20 x 20
        self.color(color)
        self.shapesize(stretch_len, 1)
        self.penup()
        self.goto(x, 0)

    # Movement
    def move(self, val):
        y = self.ycor()
        y += val
        self.sety(y)


# Ball
class Ball(turtle.Turtle):
    def __init__(self, color, dx, dy):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color(color)
        self.penup()
        self.goto(0, 0)
        self.dx = dx
        self.dy = dy


# Pen
class Pen(turtle.Turtle):
    def __init__(self, color, pos, a, b):
        super().__init__()
        self.speed(0)
        self.color(color)
        self.penup()
        self.hideturtle()
        self.goto(0, pos)
        self.write("Player A: " + str(a) + "\tPlayerB: " + str(b), align="center", font=("courier", 24, "normal"))

    def rewrite(self, a, b):
        self.clear()
        self.write("Player A: " + str(a) + "\tPlayerB: " + str(b), align="center", font=("courier", 24, "normal"))


paddle_a = Paddle(pad_len_factor, "black", -pad_pos)
paddle_b = Paddle(pad_len_factor, "black", pad_pos)

# Score
score_a = 0
score_b = 0

ball = Ball("green", 0.3, 0.3)
pen = Pen("white", score_pos, score_a, score_b)

# Keyboard Binding
win.listen()
win.onkeypress(lambda: paddle_a.move(move_val), "w") 
win.onkeypress(lambda: paddle_a.move(-move_val), "s")
win.onkeypress(lambda: paddle_b.move(move_val), "Up")
win.onkeypress(lambda: paddle_b.move(-move_val), "Down")

while True:
    win.update()

    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Wall Constraints
    if ball.ycor() > ver_lmt or ball.ycor() < -ver_lmt:
        ball.dy *= -1

    if ball.xcor() > hor_lmt or ball.xcor() < -hor_lmt:
        if ball.xcor() > hor_lmt:
            score_a += 1
        else:
            score_b += 1
        pen.rewrite(score_a, score_b)
        ball.goto(0, 0)
        ball.dx *= -1

    # Hit Constraints
    if int(ball.xcor()) == int(paddle_a.xcor()) + 20 and -pad_len <= ball.ycor() - paddle_a.ycor() <= pad_len:
        ball.dx *= -1
    if int(ball.xcor()) == int(paddle_b.xcor()) - 20 and -pad_len <= ball.ycor() - paddle_b.ycor() <= pad_len:
        ball.dx *= -1
