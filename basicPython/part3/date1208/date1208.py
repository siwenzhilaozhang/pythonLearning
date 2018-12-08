#3.1
print "3-1"
names = ["zhangsan","lisi","wangwu"]
for i in names:
    print i

print "3-2"
for i in names:
    message = i + ",you are beautiful!"
    print message
names.append("wo")
print names

#3.2
print "3-4"
names = ["diedi","mami","miumiu"]
for i in names:
    print "hi "+i+",can you eat dinner together?"

print "3-5"
print names[1]+" can not eat together."
names[1] = "didi"
for i in names:
    print "hi "+i+",can you eat dinner together?"

print "3-6"
print "I have found a bigger table."
names.insert(0,"zhangsan")
names.insert(2,"lisi")
names.append("wangwu")
for i in names:
    print "hi "+i+",can you eat dinner together?"

print "3-7"
print "sorry,I just can eat with two friends."
i = names.__len__()
while i>2:
    #print names[i-1]+"sorry,i cannot eat with you."
    #names.pop(i-1)
    print names.pop(i-1)+" sorry,i cannot eat with you."
    i=i-1
print names[0]+",welcome"
print names[1]+",welcome"
print "two"+str(names)
del names[1]
del names[0]
print "now"+str(names)
