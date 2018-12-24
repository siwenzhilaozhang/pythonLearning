#part 8

#8.1
# print "8-1"
# def display_message():
#     print "I learned hanshu"
# display_message()

# print "8-2"
# def favorite_book(title):
#     print "One of my favorite books is "+title
# favorite_book("pricess")

#8.2
# print "8-3"
# def make_shirt(size,language):
#     print "size: "+size+" ,language: "+language
# make_shirt("L","love")
# make_shirt(size="small",language="xixi")

# print "8-4"
# def make_shirt(size,language = "I love Python"):
#     print "size: " + size + " ,language: " + language
# make_shirt("L")
# make_shirt("M","I love java")

#8.3
# print "8-6"
# def city_country(city,country):
#     return city+" , "+country
# city=[]
# city.append(city_country("shenzhen","China"))
# city.append(city_country("New York","American"))
# print city

#8.4
print "8-9"
def show_magicians(magician):
    for i in magician:
        print i
magic = ["a","b","c"]
show_magicians(magic)

print "8-10"     #?????
def make_great(magician):
    new_magic = []
    for i in magician:
        i = i + " the Great"
        new_magic.append(i)
    return new_magic
new_magic = make_great(magic)
show_magicians(new_magic)