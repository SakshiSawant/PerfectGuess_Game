import random

randomNum = random.randint(1, 100)

userInput = int(input("Enter the Number "))
i = 0
while userInput != randomNum:
    if userInput > randomNum:
        userInput = int(input("Enter a Smaller Number "))
    elif userInput < randomNum:
        userInput = int(input("Enter a Larger Number "))
    i += 1

if userInput == randomNum:
    print("It's correct!!")
    print(f"You took {i} Guesses")
