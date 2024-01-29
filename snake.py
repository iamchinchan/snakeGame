from turtle import Turtle,Screen
MOVE_DISTANCE=20
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
# ,(-60,0),(-80,0)
UP=90
RIGHT=0
DOWN=270
LEFT=180
class Snake:
  
  def __init__(self) -> None:
    self.turtles = []
    self.resetSnake()
    # self.screen =screen
  def makeSnake(self):
    # creating 3 turtles in the begining for making a snake
    for position in STARTING_POSITIONS:
      self.addSegment(position)
    # self.extend()
  
  def resetSnake(self):
    for turtle in self.turtles:
      turtle.hideturtle()
    self.turtles.clear()
    self.makeSnake()
    self.head = self.turtles[0]
    self.justTurned=False
    
  def addSegment(self,position):
    magTheTurtle = Turtle(shape="square")
    magTheTurtle.color("white")
    magTheTurtle.penup()
    magTheTurtle.goto(position)
    self.turtles.append(magTheTurtle)
  
  def extend(self):
    # print("extending snake")
    self.addSegment(self.turtles[-1].position())
  
  def move(self):
    for turtle_num in range(len(self.turtles)-1,0,-1):
      #start is inclusive, 0 is exclusive
      newPosition = self.turtles[turtle_num-1].position()
      self.turtles[turtle_num].goto(newPosition)  
    # changing position of the first segment (snake head)
    self.head.forward(MOVE_DISTANCE) #moving 20 is important
    self.justTurned=False
  
  def up(self):
    if self.justTurned==False and self.head.heading() != DOWN and self.head.heading()!= UP:
      self.head.setheading(UP)
      self.justTurned=True

  def down(self):
    if self.justTurned==False and self.head.heading() != DOWN and self.head.heading()!= UP:
      self.head.setheading(DOWN)
      self.justTurned=True
   
  def left(self):
    if  self.justTurned==False and  self.head.heading() != LEFT and self.head.heading()!= RIGHT:
      self.head.setheading(LEFT)
      self.justTurned=True
      
  def right(self):
    if  self.justTurned==False and self.head.heading() != LEFT and self.head.heading()!= RIGHT:
      self.head.setheading(RIGHT)
      self.justTurned=True

      
