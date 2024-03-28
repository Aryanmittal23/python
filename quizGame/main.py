def newGame():

    Guesses = []
    correctGuesses = 0
    questionNum = 1
    
    for key in questions:
        print('---------------------------------')
        print(key)
        for i in options[questionNum-1]:
            print(i)
        guess = input('Enter (A,B,C,D):')
        guess = guess.upper()
        Guesses.append(guess)

        correctGuesses = checkAnswer(questions.get(key),guess)
        questionNum+=1

    displayScore(correctGuesses,Guesses)        

def checkAnswer(answer,guess):
    if answer == guess:
        print('correct!')
        return 1
    else:
        print('Wrong!')
        return 0
    
def displayScore(correctGuesses,Guesses):
    print('-----------------------------------')
    print('Results!')
    print('-----------------------------------')

    print("Answer:",end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()

    print("Guesses:",end='')
    for i in Guesses:
        print(i,end= " ")
    print()

    score = int((correctGuesses/len(questions))*100)
    print("Your score is :"+str(score)+"%")

def playAgain():
    response = input("Do you want to paly agian? (yes or no):")
    response = response.upper()

    if response == 'yes':
        return True
    else:
        return False

questions = {
    "Who created python?:":"A",
    'What year was python created?:':'B',
    'Python is tributed to which comedy group?:':'C',
    'Is the earth round?:':'D'
    }
options = [["A. Gudio van Rossum",'B. Elon Musk','C. Bill Gates','D.Mark Zuckerburg'],
           ['A. 1989','B.1991','C.2000','D.2016'],
           ['A.Lonely Island','B.Smosh','C.Monty python','D.SNL'],
           ['A.True','B.False','C.sometimes','D.What"s Earth']]

newGame()