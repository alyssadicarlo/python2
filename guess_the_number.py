import random

playing = True

while playing == True:
    secret_number = random.randint(1,10)
    number_of_guesses = 0
    correct = False
    print(secret_number)
    print("I am thinking of a number between 1 and 10.")
    while correct == False and number_of_guesses < 5:
        guess = int(input("What's the number? "))
        if guess == secret_number:
            print("Yes! You win!")
            correct = True
        elif guess > secret_number:
            print("%s is too high" % (guess))
        elif guess < secret_number:
            print("%s is too low" % (guess))
        number_of_guesses = number_of_guesses + 1

    if number_of_guesses == 5:
        print("You ran out of guesses!")
    
    play_again = input("Do you want to play again (Y or N)? ")
    if play_again == "N":
        playing = False