import random


def play():
    return input('Do you want to play? Enter Yes or No: ').lower().startswith('y')


def game():
    number = random.randint(1, 9)
    guess = 0
    count = 0

    while guess != number and guess != "exit":
        guess = input("Guess a number between 1-9")
        count += 1

        if guess == "exit":
            exit()

        try:
            guess = int(guess)
        except ValueError:
            print("Invalid Character")
            continue

        if guess == number:
            print("You got it man, GOOD JOB!")
            print("You have tried ", count , "times. WELL DONE")
            print("Type exit if you want to leave ")
        elif guess < number:
            print("Too Low")
        elif guess > number:
            print("Too High")
        else:
            print(" Please enter a  valid number: 1-9")


if __name__ == '__main__':
    while play():
        game()

# Main nedir