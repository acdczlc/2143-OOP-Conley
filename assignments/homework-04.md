#Zac Conley

#Questions

#1. Implement the Cat class by inheriting from the Pet class. Make sure
# to use superclass methods wherever possible. In addition, add a 
#lose_life method to the Cat class.

class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self,name,owner)
        self.lives=lives

    def talk(self):
        print("meow!")
        """A cat says meow! when asked to talk."""

    def lose_life(self):
        """A cat can only lose a life if they have at least
        one life. When lives reach zero, the 'is_alive'
        variable becomes False.
        """
        if(self.lives>0):
            self.lives-=1
        if(self.lives==0):
            self.is_alive=False

#2. Assume these commands are entered in order. What would Python output?

class Foo(object):
    def __init__(self, a):
        self.a = a
    def garply(self):
        return self.baz(self.a)

class Bar(Foo):
    a = 1
    def baz(self, val):
        return val

f = Foo(4)
b = Bar(3)
print(f.a)
# prints 4

print(b.a)
# prints 3

print(f.garply())
# gives error because baz is in bar not Foo
#bar inherits from foo but foo doesn't inherit from bar

print(b.garply())
# prints 3

b.a = 9
print(b.garply())
# prints 9

f.baz = lambda val: val * val
print(f.garply())
# prints 16
