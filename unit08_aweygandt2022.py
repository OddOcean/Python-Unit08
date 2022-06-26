############################################################
#     Aidan Weygandt                        05.08.21       #
#     Unit 8 Problems                                      #
#     Rectangle & RectanglePrivate, Account, Student       #
#     StopWatch, Line & LinearEquation                     #
############################################################


############################ ONE ###########################
  
def prob1():
  from Rectangle import Rectangle
  from RectanglePrivate import RectanglePrivate

  print("\n\n")
  print("Problem #1 - Rectangle Class\n")

  rect1 = Rectangle(4,40) #creates object from rectangle class
  print("Width:", rect1.width, "| Height:", rect1.height, "| Area:", rect1.getArea(), "| Perimeter:",rect1.getPerimeter())
  print(rect1)

  print("\n")
  rect2 = RectanglePrivate(20.5,35.5) #creates object from private rectangle class
  print(rect2, "\n")

  print("\n", "Rectangle width changed directly to 20:")
  rect1.width = 20 #sets rectangle width to 20
  print(rect1, "\n")

  print("\n", "Private rectangle width changed directly to 70.0:")
  rect2.__width = 70.0 #tries and fails to set private rectangel width to 70
  print(rect2)

  print("\n", "Private rectangle width changed with set method to 25.0:")
  rect2.setWidth(25.0) #uses method inside class to set private rectangle width to 25
  print(rect2, "\n")

#prob1()


############################ TWO ###########################

def prob2():
  from Account import Account

  account = Account("Aidan", 2000, 1000) #creates account object with 2000 in save and 1000 in check
  print("Problem #2 - Acount Class\n\n")
  print(account)

  account.checkingDeposit(-200) #fails at depositing -200 dollars into checking
  print(account)

  account.checkingDeposit(200) #deposites 200 dollars into checking
  print(account)

  account.checkingWithdrawal(5000) #withdraws 5000 dollars into checking
  print(account)

  account.checkingWithdrawal(-1000) #fails at withdrawing 5000 dollars from checking
  print(account)

  account.checkingWithdrawal(500) #withdraws 500 dollars from checking
  print(account)

  account.savingsDeposit(-200) #fails at depositing -200 dollars into savings
  print(account)

  account.savingsDeposit(200) #deposites 200 dollars into savings
  print(account)

  account.savingsWithdrawal(5000) #withdraws 5000 dollars from savings
  print(account)

  account.savingsWithdrawal(500) #withdraws 500 from savings
  print(account)

  account.checkingWithdrawal(1800) #withdraws all checking and then dips into savings to make up 1800
  print(account)

#prob2()


############################ THREE ###########################

def prob3():
  from Student import Student

  student = Student() #makes object of student class
  print("Problem #3 - Student", "\n")
  student.setName(input("Enter student's name: ")) #sets name to user input
  student.setGradYear(int(input("Enter student's graduation year: "))) #sets gradyear to input
  student.setTown(input("Enter student's town: ")) #sets town to input
  print()
  stop = "y"
  while stop == "y": #continues entering classes and scores until user says anything other than yes
    student.addClass(input("Class name: "), int(input("Class Score: ")))
    stop = input("Enter more classes? (y, n): ")
    print()
  print(student, "\n")

#prob3()


############################ FOUR ###########################

def prob4():
  import time
  from StopWatch import StopWatch

  loopWatch = StopWatch() #makes object from stopwatch class
  loopSum = 0
  loopWatch.start() #records watch start time
  for num in range(1, 1000001): #loops adding numbers so a few milleseconds pass
    loopSum += num
  loopWatch.stop() #record watch end time

  print("Problem #4 - Stopwatch", "\n")
  print("Start time:", loopWatch.getStartTime())
  print("End time:", loopWatch.getEndTime())
  print("Sum of loop:", loopSum)
  #print("Elapsed Time:", loopWatch.returnTime())
  print("Elapsed Time:", loopWatch.getElapsedTime())
  print()

  countWatch = StopWatch() #creates second stopwatch object
  loopSum = 0
  countWatch.start() #records start time
  for num in range(1, 11): #outputs 1-10
    time.sleep(1) #waits 1 second after every print
    print(num)
  countWatch.stop() #records stop time

  print()
  print("Start time:", countWatch.getStartTime())
  print("End time:", countWatch.getEndTime())
  #print("Elapsed Time:", countWatch.returnTime())
  print("Elapsed Time:", countWatch.getElapsedTime())
  print()

#prob4()

############################ FIVE ###########################

def prob5():
  from LinearEquation import Line
  from LinearEquation import LinearEquation

  #sets all line x, y and plugs them into their corresponding object VVV
  line1 = Line(200,200,0,0)
  line2 = Line(0,200,200,0)
  lnEq1 = LinearEquation(line1, line2)

  line3 = Line(-250,250,0,0)
  line4 = Line(-250,0,0,250)
  lnEq2 = LinearEquation(line3, line4)

  line5 = Line(100,0,0,-100)
  line6 = Line(0,-10,200,-200)
  lnEq3 = LinearEquation(line5, line6)

  line7 = Line(-100,0,0,-100)
  line8 = Line(-200,0,0,-200)
  lnEq4 = LinearEquation(line7, line8)

  lnEq1.drawGraph() #creates cartesian coordinate system

  #lnEq1
  line1.drawLine("red") #draws line 1 in red
  line2.drawLine("blue") #draws line 2 in blue

  print("Line 1: ", end="")
  print(line1)
  print("Slope: ", line1.getM(), "\n")
  print("Line 2: ", end="")
  print(line2)
  print("Slope: ", line1.getM(), "\n")

  if lnEq1.isSolvable(): #if lines intercect print the intercection's x, y
    lnEq1.drawVertex()
  else: print("No intercection")
  
  #lnEq2
  line3.drawLine("purple") #draws line 3 in purple
  line4.drawLine("green") #draws line 4 in green

  print("Line 3: ", end="")
  print(line3)
  print("Slope: ", line3.getM(), "\n")
  print("Line 4: ", end="")
  print(line4)
  print("Slope: ", line3.getM(), "\n")

  if lnEq2.isSolvable(): #if lines intercect print the intercection's x, y
    lnEq2.drawVertex()
  else: print("No intercection")

  #lnEq3
  line5.drawLine("blue") #draws line 5 in blue
  line6.drawLine("green") #draws line 6 in green

  print("Line 5: ", end="")
  print(line5)
  print("Slope: ", line5.getM(), "\n")
  print("Line 6: ", end="")
  print(line6)
  print("Slope: ", line5.getM(), "\n")

  if lnEq3.isSolvable(): #if lines intercect print the intercection's x, y
    lnEq3.drawVertex()
  else: print("No intercection")

  #lnEq4
  line7.drawLine("orange") #draws line 7 in orange
  line8.drawLine("red") #draws line 8 in red

  print("Line 7: ", end="")
  print(line7)
  print("Slope: ", line7.getM(), "\n")
  print("Line 8: ", end="")
  print(line8)
  print("Slope: ", line7.getM(), "\n")

  if lnEq4.isSolvable(): #if lines intercect print the intercection's x, y
    lnEq4.drawVertex()
  else: print("No intercection")

prob5()