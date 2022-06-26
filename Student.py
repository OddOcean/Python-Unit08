import datetime

now = datetime.datetime.now()

class Student:
  def __init__(self,name = "empty",grade = now.year,town = "empty", classes = [], scores = []): #constructor sets variable values when created, else they equal their defualts
    self.__name = name
    self.__gradYear = grade
    self.__town = town
    self.__classes = classes
    self.__scores = scores

  def getName(self): #returns the name
    return self.__name

  def setName(self, name): #sets the name, only able to be set with this function
    self.__name = name
  
  def getGradYear(self): #returns the gradyear
    return self.__gradYear
  
  def setGradYear(self, grade): #sets the gradyear, only able to be set with this function
    if grade >= 1000:
      self.__gradYear = grade
    else: print("Grade must be a valid year")
  
  def getTown(self): #returns the town
    return self.__town

  def setTown(self, town): #sets the town, only able to be set with this function
    self.__town = town
  
  def addClass(self, newClass, score): #adds class and score to their lists
    self.__classes.append(newClass)
    self.__scores.append(score)
  
  def printClasses(self): #print all classes, their scores, and the score average
    temp = ""
    avg = 0
    for x in range(len(self.__classes)):
      temp += self.__classes[x] + " - " + str(self.__scores[x]) + "\n"
      avg += int(self.__scores[x])
    avg /= len(self.__scores)
    temp += "Average = " + str(avg)
    return temp

  def __str__(self): #format for how the object will be printed
    return "Name: "+ self.__name + " | Grad Year: " + str(self.__gradYear) + " | Town: " + self.__town + "\nClasses:\n" + self.printClasses()
