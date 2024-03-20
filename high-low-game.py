
# Wesly Silitonga & Calista Silalashi
# Started on May 9th 2023 - Finished on May 14th 2023
# IST 2310-61
# High/Low Game! Ver. 1.00

print("Thank you for playing our game, High/Low! To begin, follow the input's instructions below!\n")

# Function block - user's guesses will be inputted and computer will tell high/low
def high_low():
    global lowInp # Globalized these inputs to use them outside function block
    global highInp
    lowInp = int(input("Please pick the low range for random number picker!: ")) # This is where user picks # ranges
    highInp = int(input("Please pick the high range for random number picker!: "))

    import random # Required to randomly pick

    randomNumber = random.randrange(lowInp,highInp) # uses the inputs above to pick between those numbers

    # Function block for High/Low Game
    def hint_givr():
        if guess > randomNumber: # If user's guess is higher than computer-picked number, print lower
            print("~ ~ ~ Lower ~ ~ ~")
        elif guess < randomNumber: # If user's guess is lower than computer-picked number, print higher
            print("~ ~ ~ Higher ~ ~ ~")

    global list1 # Globalize list below for file recording
    list1 = [] # This is where guesses are recorded
    while True: # Repeat Functions Below
        global guess
        guess = int(input("Input your guess here: ")) # User inputs number
        hint_givr() # Runs function above!
        list1.append(guess) # Count user's guesses
        print(list1)
        if guess == randomNumber:
            print("Congratulations! You're a Winner!")
            break

# Ask user for empty .txt file
while True:
    answerInp = input("Will you be using a file to record your data (Yes/No)?: ")
    if answerInp == "Yes": # Decision statement makes it streamlined.
        high_low()
        fileType = input("Will you be using a new file (Yes/No)?: ")
        if fileType == "Yes":

            from datetime import date # This feature imports current date
            today = date.today() # The gives today's date, represented by a variable

            # Below is where user inputs .txt file for recording
            fileInp = input("Please input the an empty .txt file here! It should be in the same\n"
                "folder as this program!: ")
            owFile = open(fileInp, "w") # Open file - OVERWRITES
            owFile.write("Thank you for playing High/Low.\n"
                       "This file will be used to keep track of your previous scores\n")
            owFile.write("\nDate when played: ")
            owFile.write(str(today))
            owFile.write("\nNumber Ranges: ")
            owFile.write(str(lowInp))
            owFile.write(" - ")
            owFile.write(str(highInp))
            owFile.write("\nNumber of Guesses: ")
            owFile.write(str(len(list1)))
        else:
            from datetime import date
            today = date.today()

            fileInp = input("Please input previous game file here!: ")
            openFile = open(fileInp, "a+")  # Opens file for APPENDING
            openFile.write("\n\nDate when played: ")
            openFile.write(str(today))
            openFile.write("\nNumber Ranges: ")
            openFile.write(str(lowInp))
            openFile.write(" - ")
            openFile.write(str(highInp))
            openFile.write("\nNumber of Guesses: ")
            openFile.write(str(len(list1)))
        break
    elif answerInp == "No": # Plays the game normally, no file input
        high_low()
        break
    else: # If the input is not correct (i.e., 'no', 'yes') computer will not accept it
        print("Bad Input!")