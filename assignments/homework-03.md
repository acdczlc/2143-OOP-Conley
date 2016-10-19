#Zac Conley

#Questions
# 1) What does Python print for each of the following:

# Answer 1

johns_bag = Bag()
johns_bag.print_bag()
# Prints []

for color in ['blue', 'red', 'green', 'red']:
    johns_bag.add_skittle(Skittle(color))
johns_bag.print_bag()
# Prints ['blue','red','green','red']

s = johns_bag.take_skittle()
print(s.color)
# Prints blue

print(johns_bag.number_sold)
# prints 1

print(Bag.number_sold)
# Prints 1

soumyas_bag = Bag()
soumyas_bag.print_bag()
# Prints []

print(johns_bag.print_bag())
# Prints ['red', 'green', 'red']

print(Bag.number_sold)
# Prints 2

print(soumyas_bag.number_sold)
# Prints 2

#2) Write a new method for the Bag class called take color, which takes
# a color and removes (and returns) a Skittle of that color from the 
#bag. If there is no Skittle of that color, then it returns None.

#Answer 2
 def take_color(self, color):
        temp=None
        for s in self.skittles:
            if s.color==color:
                temp=s
        if not temp==None:
            temp2=temp
            x=self.skittles.index(temp)
            del self.skittles[x]
            return temp2.color
        else:
            return None

# 3. Write a new method for the Bag class called take all, which takes
# all the Skittles in the current bag and prints the color of the each
# Skittle taken from the bag.

#Answer 3
    def take_all(self):
        for s in self.skittles:
            print s.color
        del self.skittles[:]
