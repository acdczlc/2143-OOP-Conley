#Zac Conley

#1: Definitions:
#Using python comments, label all lines that an OOP definition could
# be applied to.
class Employee: #1

   empCount = 0 #2

   def __init__(self, name, salary): #3
      self.name = name #2
      self.salary = salary #2
      Employee.empCount += 1 #2

   def displayCount(self): #4
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):#4
      print "Name : ", self.name,  ", Salary: ", self.salary#2

emp1 = Employee("Zara", 2000) #5
emp2 = Employee("Manni", 5000) #5
emp1.displayEmployee() #4
emp2.displayEmployee() #4
print "Total Employee %d" % Employee.empCount

#Answer 1
# 1 - Class
# 2 - Data Member
# 3 - Constructor
# 4 - Method
# 5 - Instance


#2: List Functions
#Given the list below:
States = ['Alabama','Illinois','Wyoming','New York', 
'Vermont', 'New Hampshire', 'Maine', 'Texas']
#A) Sort the list

#B) Add 'Oklahoma' to the list in alphabetical order without sorting 
#the list again. Actually, write a function that would add an item 
#to the list in alphabetical order. Example:
#def addInOrder(L):
    #add to the list L in the proper order
    #return your ordered list
    #return L
    
#Answer 2
#A
L=sorted(States)

#B
import bisect
def addInOrder(L):
    bisect.insort(L,'Oklahoma')
    return L

#3: Looping over Lists

#(10 Points)

#Using the following list as an example: L = [10,20,30,40,50,60,70,
#80,90,100] write a function that would divide each value by its 
#index location + 1. Our example list would turn into: 
#L = [10,10,10,10,10,10,10,10,10,10]. Remember NOT to get caught
# up on these values. Your function should work on any list.

#Usage:

L =  [10,20,30,40,50,60,70,80,90,100]
#NList = addPrevious(L)
#print(NList)
# prints: [10,10,10,10,10,10,10,10,10,10]
#Your answer should consist of just the function definition and none 
#of the usage I provided above.

#Answer 3
def addPrevious(L):
    for i in range(0,len(L)):
        L[i]=L[i]/(i+1)
    return L
NList = addPrevious(L)
print(NList)

#4: Looping over Dictionaries
#(10 Points)

#Given the following dictionary:

months = { 1 : "January", 
        2 : "February", 
        3 : "March", 
        4 : "April", 
        5 : "May", 
        6 : "June", 
        7 : "July",
        8 : "August",
        9 : "September", 
        10 : "October", 
        11 : "November",
        12 : "December" }
#Iterate over this dictionary, and create a new one that only uses the 
#first three letters of the month. Also make the new months all 
#lowercase. Your new dictionary should look like:
abbr_months = {1:"jan",
        2 :"feb",
        3 :"mar",
        4 : "apr", 
        5 : "may", 
        6 : "jun", 
        7 : "jul",
        8 : "aug",
        9 : "sep", 
        10 : "oct", 
        11 : "nov",
        12 : "dec" }
#To help you look up string slicing and lower.
#Your answer should include just the code that loops and creates the 
#new dictionary.

#Answer 4
abbr_months={}
for i in months:
    abbr_months[i]=(months[i][:3]).lower()
print abbr_months

#5: Min and Max
#(10 Points)
#Assume that pythons built in min , max , and sort functions are 
#broken. Write a function that receives a list then traverses the
# list and returns the min , max, and average values in a tuple.
#def miniStats(L):
""" 
@Description: Finds the min,max,and average values in a list
@Params: L (list)
@Returns: tuple (int,int,double)
"""
# Start with a copy of the list so we don't modify the original
#L = L[:]
#When writing your answer, include the entire function definition 
#(without the comment block).

#Answer 5
def miniStats(L):
    Lcopy=L
    minimum=Lcopy[0]
    maximum=Lcopy[0]
    sum=0
    for i in range (0,len(Lcopy)):
        sum+=Lcopy[i]
        if (Lcopy[i]<minimum):
            minimum=Lcopy[i]
        if (Lcopy[i]>maximum):
            maximum=Lcopy[i]
    average=sum/len(Lcopy)
    return ('Maximum:',maximum,'Minimum:',minimum,'Average:',average)

L=[1,4,2,7,3,6,8,9]
print(miniStats(L))

#6: Prime Class
#Write a class called myPrimes that represents a collection of your 
#prime numbers.
#addPrime :
#receives a prime number and adds it to your collection of primes
#it must be checked to make sure it's prime! (should be a private 
#method that does this).
#removePrime:
#a method will remove a prime from your list
#printPrimes:
#this method will print your prime numbers out

#Answer 6
class myPrimes(object):
    def __init__(self,primecollection):
        self.primecollection=primecollection
    def addPrime(self,newprime):
        if (self.__checkprime__(newprime)):
            self.primecollection.append(newprime)
    def __checkprime__(self,newprime):
        for i in (2, newprime-1):
            if newprime%i == 0:
                return False
        else:
            return True
    def removePrime(self,del_target):
        templist=[]
        for i in range(0,len(self.primecollection)):
            if not(self.primecollection[i]==del_target):
                templist.append(self.primecollection[i])
        self.primecollection=templist
    def printPrimes(self):
        print self.primecollection
myprimenums=[]
P1=myPrimes(myprimenums)
P1.addPrime(7)
P1.addPrime(5)
P1.addPrime(11)
P1.removePrime(11)
P1.printPrimes()

