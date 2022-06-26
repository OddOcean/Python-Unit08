import time

class Account:
  def __init__(self, name="no name", savings=0, checking=0): #constructor sets variable values when created, if no input they equal 0
    self.__idd = (int)(time.time()) #private string of numbers
    self.__name = name #private name
    self.__checking = checking #private checking balance
    self.__savings = savings #private savings balance
  
  def getIdd(self): #returns id
    return self.__idd
  
  def getName(self): #returns acount owner's name
    return self.__name

  def getChecking(self): #returns checking balance
    return self.__checking

  def getSavings(self): #returns savings balence
    return self.__savings

  def checkingDeposit(self, deposit): #deposites x amount into checking only if its positive
    if float(deposit) <= 0: print(deposit, "is not a valid deposit")
    else:
      self.__checking += float(deposit)
      print("You just deposited", deposit, "and your checking balance is", self.__checking)
  
  def savingsDeposit(self, deposit): #deposites x amount into savings only if its positive
    if float(deposit) <= 0: print(deposit, "is not a valid deposit")
    else:
      self.__savings += float(deposit)
      print("You just deposited", deposit, "and your savings balance is", self.__savings)

  def checkingWithdrawal(self, withdrawal): #withdraw x amount from checking only if its positive 
    if float(withdrawal) <= 0: print(withdrawal, "is not a valid withdrawal")
    elif self.__checking - withdrawal >= 0:
      self.__checking - withdrawal
      print("You just withdrew", withdrawal, "and your checking balance is", self.__checking)
    elif self.__checking + self.__savings - withdrawal >= 0: #withdraws excess from savings if not enough money is in checking
      self.__savings -= float(withdrawal) - self.__checking
      self.__checking = 0
      print("You just withdrew", withdrawal, end=".")
      print(" Your checking balance is", self.__checking, "and your savings balance is", self.__savings)
    elif self.__checking + self.__savings - withdrawal < 0: print("You have insuffcient funds to withdraw", withdrawal)
    else:
      self.__checking -= float(withdrawal)
      print("You just withdrew", withdrawal, "and your checking balance is", self.__checking)
  
  def savingsWithdrawal(self, withdrawal): #withdraws x amount into savings only if its positive
    if float(withdrawal) <= 0: print(withdrawal, "is not a valid withdrawal")
    elif self.__savings - withdrawal < 0: print("You have insuffcient funds to withdraw", withdrawal)
    else:
      self.__savings -= float(withdrawal)
      print("You just withdrew", withdrawal, "and your savings balance is", self.__savings)

  def __str__(self): #if class is printed it will output this
    #return ("Account ID:" + str(self.__idd) + "Account Name:" + self.__name + "Checking Balance:" + str(self.__checking) + "Savings Balance:" + str(self.__savings) + "Total Balance:" + str(self.__checking +self.__savings))
    return "Account ID: " + str(self.__idd) + " | Account Name: " + str(self.__name) + "\nChecking Balance: " + str(self.__checking) + " | Savings Balance: " + str(self.__savings) + " | Total Balance: " + str(self.__checking + self.__savings) + "\n"

