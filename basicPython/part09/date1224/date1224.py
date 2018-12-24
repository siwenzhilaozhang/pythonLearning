#part9.1
# print "9-1"
# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print self.restaurant_name
#         print self.cuisine_type
#
#     def open_restaurant(self):
#         print "zhengzaiyingye"
#
# restaurant = Restaurant("xixi","haha")
# print restaurant.restaurant_name
# print restaurant.cuisine_type
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

#9.2
# print "9-4"
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print self.restaurant_name
        print self.cuisine_type

    def open_restaurant(self):
        print "zhengzaiyingye"

    def set_number_served(self,number_served):
        self.number_served = number_served

    def increment_number_served(self,number):
        self.number_served += number
#
# restaurant = Restaurant("haha","xixi")
# print restaurant.number_served
# restaurant.number_served = 3
# print restaurant.number_served
# restaurant.set_number_served(4)
# print restaurant.number_served
# restaurant.increment_number_served(4)
# print restaurant.number_served

#9.3
print "9-6"
class IceCreamStand():

