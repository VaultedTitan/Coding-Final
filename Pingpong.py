import turtle
import winsound



# Game Window
win = turtle.Screen()
win.title("Ping Pong Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)
# Paddles
paddle1 = turtle.Turtle()
paddle1.speed(1)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350, 0)

paddle2 = turtle.Turtle()
paddle2.speed(1)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = -3
# Paddle Collision Sound
def play_paddle_sound():
    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
# Play sound for wall collision
def play_wall_sound():
    winsound.PlaySound("wall_bounce.wav", winsound.SND_ASYNC)
# Play sound for scoring
def play_score_sound():
    winsound.PlaySound("score.wav", winsound.SND_ASYNC)


# Scores
score1 = 0
score2 = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("0 - 0", align="center", font=("Courier", 24, "normal"))

# Game state
game_running = False

def show_winner(winner):
    start_display.clear()
    start_display.goto(0, 0)
    start_display.write(f"{winner} Wins! Press SPACE to Restart", align="center", font=("Courier", 24, "normal"))

def reset_game():
    global game_running, score1, score2
    score1 = 0
    score2 = 0
    score_display.clear()
    score_display.write("0 - 0", align="center", font=("Courier", 24, "normal"))
    show_start_screen()

# Paddle Movement
def paddle1_up():
    if paddle1.ycor() < 250:
        paddle1.sety(paddle1.ycor() + 20)

def paddle1_down():
    if paddle1.ycor() > -240:
        paddle1.sety(paddle1.ycor() - 20)

def paddle2_up():
    if paddle2.ycor() < 250:
        paddle2.sety(paddle2.ycor() + 20)

def paddle2_down():
    if paddle2.ycor() > -240:
        paddle2.sety(paddle2.ycor() - 20)

def start_game():
    reset_game()
    global game_running, score1, score2
    if not game_running:
        game_running = True
        score1, score2 = 0, 0
        score_display.clear()
        score_display.write("0 - 0", align="center", font=("Courier", 24, "normal"))
        start_display.clear()
        game_loop()

# Keyboard bindings
win.listen()
win.onkeypress(paddle1_up, "w")
win.onkeypress(paddle1_down, "s")
win.onkeypress(paddle2_up, "Up")
win.onkeypress(paddle2_down, "Down")
win.onkeypress(start_game, "space")

# Main game loop
def game_loop():
    global score1, score2
    if game_running:
        win.update()
        
        # Move ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border collision for top and bottom
        if ball.ycor() > 285:
            ball.sety(285)
            ball.dy *= -1
            play_wall_sound()
        if ball.ycor() < -280:
            ball.sety(-280)
            ball.dy *= -1
            play_wall_sound()

        # Left and right boundary collision (scoring)
        if ball.xcor() > 390:
            score1 += 1
            ball.goto(0, 0)
            ball.dx *= -1
            score_display.clear()
            score_display.write(f"{score1} - {score2}", align="center", font=("Courier", 24, "normal"))
            play_score_sound()

        if ball.xcor() < -390:
            score2 += 1
            ball.goto(0, 0)
            ball.dx *= -1
            score_display.clear()
            score_display.write(f"{score1} - {score2}", align="center", font=("Courier", 24, "normal"))
            play_score_sound()

        # Game Over Condition
        if score1 == 5:
            show_winner("Player 1")
            return  # Stop game loop
        elif score2 == 5:
            show_winner("Player 2")
            return  # Stop game loop

        # Paddle collision
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() - 50):
            ball.setx(340)
            ball.dx *= -1
            play_paddle_sound()

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1
            play_paddle_sound()

        # Call game_loop every 10 milliseconds
        win.ontimer(game_loop, 10)

def show_start_screen():
    start_display.clear()
    start_display.goto(0, 40)
    start_display.write("Player 1 (Left): W/S", align="center", font=("Courier", 16, "normal"))
    start_display.goto(0, 10)
    start_display.write("Player 2 (Right): Up/Down", align="center", font=("Courier", 16, "normal"))
    start_display.goto(0, -30)
    start_display.write("Press SPACE to Start", align="center", font=("Courier", 24, "normal"))

# Display start message
start_display = turtle.Turtle()
start_display.speed(0)
start_display.color("white")
start_display.penup()
start_display.hideturtle()
show_start_screen()

# Main game loop - does nothing until spacebar is pressed
win.mainloop()
