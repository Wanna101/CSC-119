"""
David Young
CSC119-479
6/14/2020
Julie Schneider
"""

def main():
    # defining set variables
    CODE = 6165
    guess = 0
    bullCount = 0
    cowCount = 0
    # code as a 4 digit integer - initialized to a set value
    print("  GAME CODE: 6165")
    # userInput - guess
    guess = input("Enter Guess: ")
    # prints labels: CODE, guess, Bulls, Cows
    print("%12s %2d %6s %5s" % ("CODE:", CODE, "Bulls", "Cows"))
    print("%12s %2d %6d %5d" % ("Guess:", int(guess), bullCount, cowCount))
main()
