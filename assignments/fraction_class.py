"""
Name: Zac Conley
Email: acdczlc@gmail.com
Assignment: Homework 2 - Getting your python feet wet
Due: 26 Sep @ 1:00 p.m.
"""
class fraction(object):
    def __init__(self,n=None,d=None):
        self.numerator = n
        self.denominator = d

    def __str__(self):
        return "%s / %s" % (self.numerator , self.denominator)

    def numerator(self,n):
        self.numerator = n 

    def denominator(self,d):
        self.denominator = d

    def __mul__(self,rhs):
        x = self.numerator * rhs.numerator
        y = self.denominator * rhs.denominator
        return fraction(x,y)
    
    def add(self, b):
        f=self.numerator*b.denominator + self.denominator*b.numerator #makes new numerator=f
        g=self.denominator*b.denominator #makes new denominator=g
        e=(f%g)/g #creates e to subtract remainder from fraction on next line
        h=f/g-e
        i=int(h) #turns the fraction without remainder into an int for cleaner printing
        j=f%g #creates numerator of remainder fraction
        k=int(j) #turns numerator of reaminder fraction to int
        l=int(g) #turns denominator of remainder fraction to int
        print a,
        print"+",
        print b,
        print"=",
        print i, #prints the whole number with a space then the remainder fraction
        print "",
        print(str(fraction(k,l)))


if __name__ == '__main__':
    a = fraction(1.0,2.0)
    b = fraction(4.0,5.0)
    c= fraction.add(a,b)
  
    