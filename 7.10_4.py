# def save_name_under_name_file():
#     my_file = open("names.txt", "a")
#     for i in range(3):
#         current_name = input("enter your name: ")
#         my_file.write(current_name + "\n")
#
# save_name_under_name_file()
#
# def show_name_from_file():
#     my_file = open("names.txt", "r")
#     contents = my_file.readlines()
#     print(contents)
#     for line in contents:
#         print(line, end='')
# show_name_from_file()

def save_names():
    my_file = open("names.txt", "a")
    current_name = input("enter your name: ")
    my_file.write(current_name + "\n")
    my_file.close()


def show_name():
    my_file = open("names.txt", "r")
    for name in my_file.readlines():
            print("current name is: " + name, end='')

    # with open("names.txt", "r") as my_file:
    #     for name in my_file.readlines():
    #         print("current name is: " + name, end='')

for i in range(4):
    save_names()

show_name()