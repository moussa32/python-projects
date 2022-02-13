import random

def convertInputToDigit(number):
    if number.isdigit():
        number = int(number)

        if number <= 0:
            print("Please type a number larger than 0 next time.")
            quit()

        return number
    else:
        print("Please type a number next time.")
        quit()


top_of_range = convertInputToDigit(input("Type the numbers range: "))
randomNumber = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == randomNumber:
        print("You got it!")
        print(f"You got it in {guesses} guesses")
        break
    else:
        if abs((user_guess - randomNumber)) <= 2:
            print("Wrong but you are very close to the right number")
        elif user_guess > randomNumber: 
            print("You were above the number!")
        elif user_guess < randomNumber:
            print("You were below the number!")
        else:
            print("You got it wrong")

