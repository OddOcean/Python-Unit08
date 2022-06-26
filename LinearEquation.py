import turtle

class Line:
  def __init__(self, xStart, yStart, xEnd, yEnd): #constructor sets variable values when created
    self.__xStart = xStart
    self.__yStart = yStart
    self.__xEnd = xEnd
    self.__yEnd = yEnd
    self.__aline = turtle.Turtle()

  def drawLine(self, color): #draws line
    self.__aline.penup()
    self.__aline.color(color)
    self.__aline.goto(self.__xStart, self.__yStart) #goes to object xstart and ystart private variables
    self.__aline.pendown()
    self.__aline.goto(self.__xEnd, self.__yEnd)
    self.__aline.penup()
    self.__aline.goto(0, 0)

  def getDeltaX(self): #calculates and return run of slope
    return self.__xEnd - self.__xStart

  def getDeltaY(self): #calculates and returns rise of slope
    return self.__yEnd - self.__yStart

  def getM(self): #divides rise by run to get slope and returns it
    return self.getDeltaY() / self.getDeltaX()

  def getB(self): #calculates and returns b of line
    return ((self.getM() * self.__xStart) - self.__yStart) * -1

  def __str__(self): #if class is printed it will output this
    return "Line from (" + str(self.__xStart) + "," + str(self.__yStart) + ")" + " to (" + str(self.__xEnd) + "," + str(self.__yEnd) + ")"


class LinearEquation:
  def __init__(self, line1, line2): #constructor sets variable values when created
    self.__line1 = line1
    self.__line2 = line2
    self.__vertex = turtle.Turtle()

  def drawGraph(self): #draws cartesian coordinate system
    self.__vertex.penup()
    self.__vertex.goto(-300, 0)
    self.__vertex.pendown()
    self.__vertex.goto(300, 0)
    self.__vertex.penup()
    self.__vertex.goto(0, -300)
    self.__vertex.pendown()
    self.__vertex.goto(0, 300)
    self.__vertex.penup()
    self.__vertex.goto(0, 0)

  def drawVertex(self): #goes to intercept of both lines and draws red circle
    print("Intersecting Point:", self.getInter(), "\n\n")
    x, y = self.getInter()
    self.__vertex.penup()
    self.__vertex.goto(x, y - 2)
    self.__vertex.pendown()
    self.__vertex.fillcolor("red")
    self.__vertex.begin_fill()
    self.__vertex.circle(2)
    self.__vertex.end_fill()
    self.__vertex.penup()
    self.__vertex.goto(0, 0)

  def isSolvable(self): #returns a true boolian number if lines touch
    return self.__line1.getM() != self.__line2.getM()

  def getInter(self): #calculates intercept of the lines and returns them
    x = (self.__line2.getB() - self.__line1.getB()) / (self.__line1.getM() - self.__line2.getM())
    y = self.__line1.getM() * x + self.__line1.getB()
    return x, y