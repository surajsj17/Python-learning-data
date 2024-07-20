# overloading:
class Area :
    def find_area(self, a = None, b = None):
        if a != None and b != None:
            print(" rectangle area is ", a *b) #multiplication of 2 numbers
        elif a != None :
            print(" square area is ", a * a) # square of any number or area of square
        else:
            print("try again")

# + : 12 +13 =25
# "hello" + "hi"--> "hello hi"

a = Area()


a.find_area(12)  #
a.find_area(12,4)
a.find_area()

