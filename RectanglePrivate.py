class RectanglePrivate:
  def __init__(self, width = 1, height = 2): #constructor sets variable values when created, will be 1 if no number is passed in
    self.__width = width
    self.__height = height

  def getPerimeter(self): #returns the perimeter
    return (2 * self.__width) + (2 * self.__height)

  def getArea(self): #returns the area
    return self.__width * self.__height
  
  def setWidth(self, width): #allows for setting of width, cannot be done directly
    if width > 0: #make sure radius isn't negative or 0
      self.__width = width
  
  def setHeight(self, height): #allows for setting of height, cannot be done directly
    if height > 0: #make sure radius isn't negative or 0
      self.__height = height

  def getWidth(self): #allows for getting radius because cannot be done directly
    return self.__width

  def __str__(self): #format for how the object will be printed
    return "Width: "+ str(self.__width) + " | Height: " + str(self.__height) + " | Perimeter: " + str(self.getPerimeter()) + " | Area: " + str(self.getArea())