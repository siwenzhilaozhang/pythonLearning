#coding:utf-8
# with open("pi_digits.txt") as file_object:
#     contents = file_object.read()
# #     #全部文件读取
# #     #print contents
# #     #print contents.rstrip()
# #
#     #逐行读取
#     for line in file_object:
#         print line
#
# filename = 'pi_digits.txt'
# with open('pi_digits.txt') as file_object:
#     # for line in file_object:
#     #     print line.rstrip()
#
#     lines = file_object.readlines()
#     for line in lines:
#         print line.rstrip()

#10.1
# print "10-1"
# filename = "learning_python.txt"
# with open(filename) as file_object:
#     # content = file_object.read()
#     # print content
#     #
#     # for line in file_object:
#     #     print line
#
#     lines = file_object.readlines()

#10.2
# filename = "learning_python_10_2.txt"
# with open(filename,"w") as file_object:
#     file_object.write("I love diedi.\n")

# print "10-3"
# string_input = raw_input("please enter your name")
# with open("guest.txt",'w') as file_object:

#     file_object.write(string_input)

#10.3
try:
    print 5/0
except ZeroDivisionError:
    print "you can`t divide by zero!"


