# 1+2
#ZeroDivisionError
# a = 1/0 ()
# try:
#     my_variable = int(input("enter first number: "))
#     my_other_var = int(input("enter second number: "))
#     result = my_variable / my_other_var
#     print(result)
# except ZeroDivisionError as e:
#     print("could not divide by zero")
# except ValueError as e:
#     print("enter a normal number")
# except BaseException as e:
#     print(e.args)

# 7-9
# def save_names():
#     my_file = open("words.txt", "a")
#     current_name = input("enter your name: ")
#     my_file.write(current_name + "\n")
#     my_file.close()
# def show_name():
#     my_file = open("words.txt", "r")
#     for name in my_file.readlines():
#             print("current name is: " + name, end='')
#
# for i in range(1):
#     save_names()
#
# show_name()

# 10
# def save_names():
#     my_file = open("words.txt", "a")
#     current_name = input("enter your name in Hebrew: ")
#     my_file.write(current_name + "\n")
#     my_file.close()
# def show_name():
#     my_file = open("words.txt", "r")
#     for name in my_file.readlines():
#             print("current name in Hebrew: " + name, end='')
#
# for i in range(1):
#     save_names()
#
# show_name()

