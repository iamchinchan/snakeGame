from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self)->None:
    super().__init__()
    self.score=0
    self.highScore =0
    self.penup()
    self.color("white")
    self.hideturtle()
    self.updateScoreboard()
    # self.pensize(40)
    
    
  def updateScoreboard(self):
    self.clear()
    self.goto((0,320))
    self.write(f"Score: {self.score}, High Score: {self.highScore}", True,align="center",font=("Arial", 18, "normal"),)
  def snakeAteFood(self):
    self.score+=1
    self.updateScoreboard()   
    
  def reset(self):
    if self.score > self.highScore:
      self.highScore = self.score
    self.score = 0
    self.updateScoreboard()
  # def gameover(self):
  #   self.goto((0,0))
  #   self.write("Game Over",True,align="center",font=("Arial", 18, "normal"))