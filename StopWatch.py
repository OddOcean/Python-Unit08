import time

class StopWatch:
  def __init__(self, startTime = 0, endTime = 0): #constructor sets variable values when created, if no input equals 0
    self.__startTime = float(startTime)
    self.__endTime = float(endTime)
  
  def getStartTime(self): #returns start time
    return self.returnTime(self.__startTime)

  def getEndTime(self): #returns end time
    return self.returnTime(self.__endTime)
  
  def getElapsedTime(self): #calculates and returns elapsed time
    return self.returnTime(self.__endTime - self.__startTime)

  def start(self): #sets start time to now when called
    self.__startTime = time.time()

  def stop(self): #sets start time to now when called
    self.__endTime = time.time()

  '''
  def returnTime(self): #finds elapsed time and returns it
    elapsedTime = float(self.__endTime) - float(self.__startTime)
    milliseconds = str((int(elapsedTime*1000)))
    seconds = int(elapsedTime % 60)
    totalMinutes = elapsedTime // 60
    minutes = int(totalMinutes % 60)
    totalHours = (totalMinutes // 60)
    hours = int(totalHours % 24)

    returnTime = str(hours) + ":" + str(minutes) + ":" + str(seconds) + ":" + milliseconds.zfill(4)
    return returnTime
  '''
  def returnTime(self, thetime): #finds elapsed time and returns it
    #elapsedTime = float(self.__endTime) - float(self.__startTime)
    elapsedTime = thetime
    totalSeconds = int(elapsedTime)
    milliseconds = str((int((elapsedTime-totalSeconds)*1000)))
    print(milliseconds)
    seconds = int(elapsedTime % 60)
    totalMinutes = elapsedTime // 60
    minutes = int(totalMinutes % 60)
    totalHours = (totalMinutes // 60)
    hours = int(totalHours % 24)

    returnTime = str(hours) + ":" + str(minutes) + ":" + str(seconds) + ":" + milliseconds.zfill(4)
    return returnTime