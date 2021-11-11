from GuessGame import play as play_guess_game
from MemoryGame import play as play_memory_game


def welcome(name):
    if not name.isalpha():
        print("Not an integer,Your input must be of a integer type")
    else:
        print("Hello %s and welcome to the World of Games (WoG).\nHere you can find many cool games to play." % (name))


def level_of_difficulty():
    level = 0
    while level > 5 or level < 1:
        level = int(input("please choose level of difficulty from 1 to 5: "))
        if 0 < level <= 5:
            return level
        else:
            print("If you want to play you must choose level of difficulty from 1 to 5")


def load_game():
    game_number = 0
    while game_number > 3 or game_number < 1:
        print("""
            Game Options:
            ------------
            1.Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
            2.Guess Game - guess a number and see if you chose like the computer
            3.Currency Roulette - try and guess the value of a random amount of USD in ILS
            """)
        game_number = int(input("please choose game from 1 to 3: "))
        if 0 < game_number <= 3:
            difficulty = level_of_difficulty()
            if game_number == 1:
                print("Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
                play_memory_game(difficulty)
            elif game_number == 2:
                print("Guess Game - guess a number and see if you chose like the computer")
                play_guess_game(difficulty)
            elif game_number == 3:
                print("Currency Roulette - try and guess the value of a random amount of USD in ILS")
            break
        else:
            print("If you want to play you must choose game from 1 to 3")
