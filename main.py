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
while isGameOn:
  screen.update()
  time.sleep(.1)
  snake.move()
  
  # detect snake's distance with food
  if(snake.head.distance(food)<=15):
    food.refresh()
    scoreboard.snakeAteFood()
  
  
screen.exitonclick()