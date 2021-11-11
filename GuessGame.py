import random


# generate a random secret_number
def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    # print("The random number is: " + str(secret_number))
    return secret_number


def get_guess_from_user(difficulty):
    # converts input "string" to int
    return int(input("Please select number between 1 to {}:".format(difficulty)))


def compare_results(secret_number, guess):
    # check if the guess matches the secret_number
    if guess == secret_number:
        print("You guessed it right!")
    else:
        print("You lose!")
        print("The number I thought was " + str(secret_number))


def play(difficulty):
    secret = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    compare_results(secret, user_guess)
