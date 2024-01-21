from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=700,height=700)
screen.title(titlestring="Snake Game")
screen.bgcolor("black")
screen.tracer(0)


snake= Snake()
food= Food()
scoreboard = Scoreboard()

screen.listen()

# must move then update screen and check after each turn if food eaten or any collision happened

# or in snake class to these dir fn's add a cond such that it mst have been moved since last turn through normal loop before we change its dir again
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)
isGameOn = True
# snake.head.goto((311,0))
# screen.update()
screen.update()

while isGameOn:
  screen.update()
  time.sleep(.1)
  snake.move()
  
  # detect snake's distance with food
  if(snake.head.distance(food)<=15):
    food.refresh()
    snake.extend()
    scoreboard.snakeAteFood()
    
  # detect snake's collision with walls
  if(snake.head.xcor()>330 or snake.head.xcor()<-330 or snake.head.ycor()>330 or snake.head.ycor()<-330):
    screen.update()
    isGameOn=False
    scoreboard.gameover()   
  
  #detect snake's collision with itself
  for snakeSegment in snake.turtles:
    if snakeSegment == snake.head:
      pass
    elif snake.head.distance(snakeSegment)<10:
      isGameOn=False
      scoreboard.gameover()
screen.exitonclick()