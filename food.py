from turtle import Turtle
from random import randint
class Food(Turtle):
  def __init__(self) -> None:
    super().__init__()
    self.setFoodProperties()
    self.refresh()
  def setFoodProperties(self):
    self.color("blue")
    self.shape("circle")
    self.shapesize(stretch_len=0.5, stretch_wid=0.5)
    self.penup()
    self.speed("fastest")
   
  
  def refresh(self):
    # randomPosition = (randint(0,330),randint(0,330))
    randomPosition = (randint(0,330),randint(0,310))
    self.goto(randomPosition)
    # self.goto((0,310))