import sys    #Gives access to files on the system
import random

#This program is currently broken. Please use the other one in Python33. 

def login(question, answer):    #This gives the login prompt. Passwords must match to get through this part, otherwise while loop will put you back through until passwords match.
    i = 0
    print('Welcome! In order to use the following program, you must first login!')
    print('')
    while i == 0:
        username = input('Please enter your username: ')
        password = input('Please enter your password: ')
        password2 = input('Please enter your password again: ')
        if password != password2:
            print('Login error. Passwords did not match. Please try again.')
        else:
            i = i + 1
            
        
    botCheck(question, answer)
    
def botCheck(question, answer):    #This checks to see if the user is a bot. 
    counter = 0    #Makes sure program flow is controlled.
    i = 0
    randArray = []
    print('')
    print("To make sure you are not a bot, you must pass the following bot test.")
    print('')
    
    while counter == 0:
        for i in range(len(question)):
            randArray.append(random.randrange(0, len(question)))
            botTest = input(question[randArray[i]])
            for m in range(len(randArray)):
                while randArray[i] == randArray[m]:
                    randArray.remove(randArray[i])
                    randArray.append(random.randrange(0, len(question + 1)))
            for j in range(len(answer)):
                if randArray[i] == j:
                    if botTest == answer[randArray[i]][0]:
                        print('')
                        print('Great! Onto the next question.')
                        counter = counter + 1
                    else:
                        print('You are a bot. Please try again.')

def main():
        questionFile = open('Login Questions.txt', 'r')    #Opens a file with a list of questions.
        answerFile = open('Login Answers.txt', 'r')
        questions = questionFile.read()    #Reads the file and converts it into a string. Operations can be done on this string (such as storing it in an array, which we do).
        answers = answerFile.read()
        questionArray = questions.split('<>')
        answerArray = answers.split('<>')
        login(questionArray, answerArray)

main()
