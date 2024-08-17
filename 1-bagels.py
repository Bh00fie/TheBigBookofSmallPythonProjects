import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    
    while True:
        secretNum = getSecretNumber()
        print("I have a number")
        print("You have {} of guesses to guess it".format(MAX_GUESSES))
        
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = " "
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}".format(numGuesses))
                guess = input("< ")
                
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
            
            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print("you have used all of  your guesses")
                print("the right number was {}".format(secretNum))
                
        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing")

def getSecretNumber():
    numbers = list("0123456789")
    random.shuffle(numbers)
    
    secretNum = ""
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum
    
def getClues(guess, secretNum):
    if guess == secretNum:
        return "You got it"
    
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append("Pico")
    if len(clues) == 0:
        return "bagels"
    else:
        clues.sort()
        return " ".join(clues)
    
if __name__ == "__main__":
    main()
    
                