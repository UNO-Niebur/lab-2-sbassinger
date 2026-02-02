#FutureTime.py
#Name: Scott Bassinger
#Date: 02/01/2026
#Assignment: Lab2- FutureTime
#purpose: Calculate the future time based on user input of hours and minutes to add to the current time.

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  usrHours = int(input("Could you provide me with some arbitrary number of hours?"))
  #Ask user for minutes
  usrMinutes = int(input("Okay, and a number of minutes?"))
  #Calculate the time after the user-supplied time has passed.
  totalMinutes = currentMinute + usrMinutes
  totalHours = currentHour + usrHours + (totalMinutes // 60)
  futureMinute = totalMinutes % 60
  futureHour = totalHours % 24
  futureTime = (futureHour, futureMinute)
  
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  print("The time after the hours and minutes you provided will be: {:02}:{:02}".format(futureTime[0], futureTime[1]))


if __name__ == '__main__':
  main()
