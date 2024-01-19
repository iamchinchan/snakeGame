from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self)->None:
    super().__init__()
    self.score=0
    self.penup()
    self.hideturtle()
    self.color("white")
    self.goto((0,320))
    # self.pensize(40)
    self.write(f"Score: {self.score}", True,align="center",font=("Arial", 18, "normal"),)
    
  def snakeAteFood(self):
    self.clear()
    self.score+=1
    self.goto((0,320))
    self.write(f"Score: {self.score}", True,align="center",font=("Arial", 18, "normal"),)    