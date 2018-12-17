#4.3
#4-3
print "4-3"
for i in range(1,21):
    print i

#4-4,4-5
print "4-4,4-5"
list = [i for i in range(1,1000001)]
#print list
print min(list)
print max(list)
print sum(list)

#4-6
print "4-6"
list = [i for i in range(3,30,3)]
for i in list:
    print i

print "******************"
#4.4
#4-10
print "4-10"
list = [i for i in range(3,30,3)]
print list
print "The first three items in the list are:"
print list[:3]
print "Three items from the middle of the list are:"
print list[3:6]
print "The last three items in the list are:"
print list[-3:]

#4-11
print "4-11"
pizzas = ["liulian pizza","niurou pizza","shuiguo pizza"]
friend_pizzas = pizzas[:]
pizzas.append("mugua")
friend_pizzas.append("boluo")
print "My favorite pizzas are:"
print pizzas
print "My friend`s favorite pizzas are:"
print friend_pizzas
