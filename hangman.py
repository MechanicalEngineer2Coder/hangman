import random

def hangman():
    #Game intro
    name = input("Enter your name: ")
    print("Welcome ", name)
    print("---------------")
    print("Try to guess the word in less than 10 attempts.")
    
    #Game setup
    word = random.choice(["pugger", "littlepugger", "tiger", "superman", "thor", "pokemon"])
    validLetters = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guessMade = ""

    while len(word)>0:
        main = ""

        #Checks each letter in word for match. Initial run sets up all dash marks
        for letter in word:
            if letter in guessMade:
                main += letter
            else:
                main += "_" + ""

        #Checks if game is won and stops progam if match. If not it ask for next guess
        if main == word:
            print(main)
            print("You win!")
            break
        print("Guess the word: ", main)
        guess = input()

        #Checks if guessed letter is a letter. If not user has to retry
        if guess in validLetters:
            guessMade += guess
        else:
            guess = input("Enter a valid character: ")

        #If user guesses incorrectly, turns left is reduced and visual given
        if guess not in word:
            turns -= 1
            if turns == 9:
                print("Wrong. 9 turns left")
                print (" ------ ")
            if turns == 8:
                print("Wrong. 8 turns left")
                print(" ------ ")
                print("   0    \n")
            if turns == 7:
                print("Wrong. 7 turns left")
                print(" ------ ")
                print("   0    ")
                print("   |    \n")
            if turns == 6:
                print("Wrong. 6 turns left")
                print(" ------ ")
                print("   0    ")
                print("   |    ")
                print("  /     \n")
            if turns == 5:
                print("Wrong. 5 turns left")
                print(" ------ ")
                print("   0    ")
                print("   |    ")
                print("  / \   \n")
            if turns == 4:
                print("Wrong. 4 turns left")
                print(" ------ ")
                print(" \ 0    ")
                print("   |    ")
                print("  / \   \n")
            if turns == 3:
                print("Wrong. 3 turns left")
                print(" ------ ")
                print(" \ 0 /  ")
                print("   |    ")
                print("  / \   \n")
            if turns == 2:
                print("2 turns left")
                print(" ------ ")
                print(" \ 0 /|  ")
                print("   |    ")
                print("  / \   \n")
            if turns == 1:
                print("Wrong. 1 turn left")
                print(" ------ ")
                print(" \ 0_|/ ")
                print("   |    ")
                print("  / \   \n")
            if turns == 0:
                print("You lose")
                print(" ------ ")
                print("   0_| ")
                print("  /|\   ")
                print("  / \   \n")
                break
            

hangman()

