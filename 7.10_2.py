# file open mode
# open procssing of file descriptor
# how to call to file to r
# my_file = open("read_my_contents.txt", "r")
# contents = my_file.readlines()
# print(contents)
# for line in contents:
#     print(line, end='')

# try to write to  to file read only

# my_file = open("read_my_contents.txt", "r")
# contents = my_file.write("hh")
# print(contents)
# for line in contents:
#     print(line, end='')
import io
try:
    my_file = open("read_my_contents.txt", "r")
    contents = my_file.write("blabla")
except io.UnsupportedOperation:
    print("Unsupported Operation")

# open file not exsit
# try:
#     my_file = open("ss.txt", "r")
#
# except FileNotFoundError as e:
#     print(e.args)






# # how to call to file to w (in this case the txt file created automaticlly)
# my_file.close()
# my_file = open("names.txt", "w")
# for i in range(3):
#     current_name = input("enter your name: ")
#     my_file.write(current_name + "\n")
# my_file.close()
#
# my_file = open("names.txt", "r")
# for name in my_file.readlines():
#     print(f"hello {name}", end='')
#
