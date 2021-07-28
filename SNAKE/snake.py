import pygame,  time, turtle
from random import randrange

screen = turtle.Screen()
screen.title('GAME: SNAKE')
screen.setup(650, 650)
screen.bgcolor('lightblue')

screen.tracer(0)

snake = []
for i in range(1):
    snake_segment = turtle.Turtle()
    snake_segment.shape('square')
    snake_segment.penup()
    if i > 0:
        snake_segment.color('green')
    snake.append(snake_segment)

fruit = turtle.Turtle()
fruit.shape('circle')
fruit.color('red')
fruit.penup()
fruit.goto(randrange(-300, 300, 20), randrange(-300, 300, 20))

screen.onkeypress(lambda: snake[0].setheading(90), 'Up')
screen.onkeypress(lambda: snake[0].setheading(180), 'Left')
screen.onkeypress(lambda: snake[0].setheading(0), 'Right')
screen.onkeypress(lambda: snake[0].setheading(270), 'Down')

screen.listen()

while True:

    if snake[0].distance(fruit) < 10:
        fruit.goto(randrange(-300, 300, 20), randrange(-300, 300, 20))
        snake_segment = turtle.Turtle()
        snake_segment.shape('square')
        snake_segment.color('green')
        snake_segment.penup()
        snake.append(snake_segment)

    for i in range(len(snake)-1, 0, -1):
        x = snake[i-1].xcor()
        y = snake[i-1].ycor()
        snake[i].goto(x, y)

    snake[0].forward(20)
 
    screen.update()

    time.sleep(0.3)

screen.mainloop()
