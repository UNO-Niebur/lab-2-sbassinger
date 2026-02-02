#Magic8Ball.py
#Name: Scott Bassinger
#Date: 02/01/2026
#Assignment: Lab2- Magic8Ball
#purpose: Create a Magic 8 Ball program that provides random answers to user questions.

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  responses = ["Yes", "No", "Wouldn't you like to know?", "What do you think?", "What would your therapist say?", 
               "Definitely maybe", "Ask again later", "Indubitably", "The outlook is grim", 
               "I'm reporting your question to the authorities"]
  print("Magic 8 Ball")
  #Prompt the user for their question.
  question = input("Ask me anything and I shall answer: ")
  #Answer question randomly with one of the options from your earlier list.
  answer = random.choice(responses)
  print("The Magic 8 Ball says: " + answer)

if __name__ == '__main__':
  main()
