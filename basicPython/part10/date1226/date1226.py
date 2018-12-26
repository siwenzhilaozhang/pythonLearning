#10.3
print "10-6"

def string_to_int(inputString):
    try:
        inputInt = int(inputString)
    except ValueError:
        print "please input int"
    else:
        return inputInt
def input_num():
    inputString = raw_input("input a number")
    num = string_to_int(inputString)
    return num
num1 = input_num()
num2 = input_num()
try:
    print num1+num2
except TypeError:
    pass
