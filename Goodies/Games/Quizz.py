print('Welcome to Sitraka s Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Question 1: What is your Favourite programming language?')
    if answer.lower()=='python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: Do you follow any author on Twitter? ')
    if answer.lower()=='yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: What is the name of your favourite website for learning Python?')
    if answer.lower()=='askpython':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')


#This code was written thanks to AskPython 
#How does the else if aka ELIF works ? 
#Here is an example.
#if condition:
    # code
#elif condition:
    # code
    # multiple elif statements
#else:
    # default code
