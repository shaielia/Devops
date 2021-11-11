import random
import os
import time


# generate a random secret_number
def generate_sequence(difficulty):
    # random_numbers = random.randint(1, 101, difficulty)
    random_numbers = random.sample(range(1, 101), difficulty)
    print("The random number is: " + str(random_numbers))
    time.sleep(0.7)
    os.system("clear")
    return random_numbers


def get_list_from_user(difficulty):
    number_list = []
    user_list: str = str(input("your list between 1 to {} please write your number between 1 to 101 and separated them by comma :".format(difficulty)))
    print("\n")
    for i in range(0, int(user_list)):
        print("Enter number at index", i, )
        item = int(input())
        number_list.append(item)
    print("User list is " + str(number_list))
    return number_list


def is_list_equal(random_numbers, number_list):
    if sorted(list(random_numbers)) == sorted(list(number_list)):
        print("You Win")
    else:
        print("You lose")


def play(difficulty):
    computer = generate_sequence(difficulty)
    user = get_list_from_user(difficulty)
    is_list_equal(computer, user)
