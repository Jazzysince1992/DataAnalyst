import random
maxNumber = int(input("Please enter a number below which you want to guess number"))
randomNumber = random.randint(1,maxNumber)
numOfGuesses = 0 
while True:
    numOfGuesses+=1
    guessedNumber=input("Please enter the number:")
    if guessedNumber.isdigit():
        guessedNumber = int(guessedNumber)
        if guessedNumber> randomNumber:
            print("\n You are the above numbber. Try guessing a smaller number.")
            print(list(range(1,guessedNumber)))
        elif guessedNumber<randomNumber:
            print("\n You are below the number. Try guessing a bigger number.")
            print(list(range(guessedNumber+1,maxNumber+1)))
        else:
            print("Congrats! You got it.")
            break
    else:
        print("Please enter a valid number.")
print("You took",numOfGuesses)