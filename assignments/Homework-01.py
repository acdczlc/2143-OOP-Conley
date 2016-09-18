"""
Name: Zac Conley
Email: acdczlc@gmail.com
Assignment: Homework 1 - Lists and Dictionaries
Due: 19 Sep @ 1:00 p.m.
"""

#A
a = [1, 5, 4, 2, 3] 
print(a[0], a[-1])
#Prints (1,3)
a[4] = a[2] + a[-2]
print(a)
#Prints [1, 5, 4, 2, 6]
print(len(a))
#Prints 5
print(4 in a)
#Prints True
a[1] = [a[1], a[0]]
print(a)
#Prints [1, [5, 1], 4, 2, 6]

#B
"""Removes all instances of el from lst. 
Given: x = [3, 1, 2, 1, 5, 1, 1, 7]
Usage: remove_all(1, x)
Would result in: [3, 2, 5, 7]
"""
def remove_all(el, lst):
    y=len(lst)  #finds length of list
    lst.sort() 
    for g in range (0,y):
        if (lst[0]==el):  #checks first element of sorted list
            lst.remove(el) # removes element
    print(lst)

x=[3, 1, 2, 1, 5, 1, 1, 7]
remove_all(1,x)

#C
""" Adds y to the end of lst the number of times x occurs in lst. 
Given: lst = [1, 2, 4, 2, 1]
Usage: add_this_many(1, 5, lst)
Results in: [1, 2, 4, 2, 1, 5, 5]
"""
def add_this_many(x, y, lst):
    z=len(lst) #finds length of list
    xnum=0 # sets accumulator for adding y later
    for g in range(0,z):
        if(lst[g]==x):
            xnum+=1 #accumulates
    for h in range(0,xnum): #appends y to list xnum times
        lst.append(y)
    print(lst)

lst=[1, 2, 4, 2, 1]
add_this_many(1, 5, lst)

#D
a = [3, 1, 4, 2, 5, 3]
print(a[:4])
#prints [3, 1, 4, 2]

print(a)
#prints [3, 1, 4, 2, 5, 3]

print(a[1::2])
#prints [1, 2, 3]

print(a[:])
#prints [3, 1, 4, 2, 5, 3]

print(a[4:2])
#prints []

print(a[1:-2])
#prints [1, 4, 2]

print(a[::-1])
#prints [3, 5, 2, 4, 1, 3]

#E
""" Reverses lst in place. 
Given: x = [3, 2, 4, 5, 1] 
Usage: reverse(x)
Results: [1, 5, 4, 2, 3]
"""
def reverse(lst):
    revlst=lst[::-1] #makes backwards list
    print(revlst)

x= [3, 2, 4, 5, 1] 
reverse(x)

#F
""" Return a new list, with the same elements of lst, rotated to the right k.
Given: x = [1, 2, 3, 4, 5]
Usage: rotate(x, 3)
Results: [3, 4, 5, 1, 2]
"""
def rotate(lst, k):
    y=len(lst)
    k=k%y #finds mod
    k=k-1 
    print(lst[k:]+lst[:k]) # prints rotated list
x = [1, 2, 3, 4, 5]
rotate(x,3)

#H
superbowls = {'joe montana': 4, 'tom brady':3, 'joe flacco': 0}
superbowls['peyton manning'] = 1
superbowls['joe flacco'] = 1
print(superbowls)
print('colin kaepernick' in superbowls)
#prints False
print(len(superbowls))
#prints 4
print(superbowls['peyton manning'] == superbowls['joe montana'])
#prints False
superbowls[('eli manning', 'giants')] = 2
print(superbowls)
#prints {'joe flacco': 1, ('eli manning', 'giants'): 2, 'joe montana': 4, 'peyton manning': 1, 'tom brady': 3}
superbowls[3] = 'cat'
print(superbowls)
#prints {3: 'cat', 'peyton manning': 1, ('eli manning', 'giants'): 2, 'joe flacco': 1, 'joe montana': 4, 'tom brady': 3}
superbowls[('eli manning', 'giants')] =  superbowls['joe montana'] + superbowls['peyton manning']
print(superbowls)
#prints {3: 'cat', 'peyton manning': 1, ('eli manning', 'giants'): 5, 'joe flacco': 1, 'joe montana': 4, 'tom brady': 3}

#superbowls[['steelers', '49ers']] = 11
#print(superbowls)
#gives error for list being an unhashable type

#I
"""Replaces all values of x with y. 
Given: d = {1: {2:3, 3:4}, 2:{4:4, 5:3}} 
Usage: replace_all(d,3,1)
Results: {1: {2: 1, 3: 4}, 2: {4: 4, 5: 1}} 
"""
def replace_all(d, x, y):
    if (d[1][2]==x): #checks each tuple for 3's in the values
         d[1][2]=y #changes 3's to 1's
    if (d[1][3]==x):
         d[1][3]=y
    if (d[2][4]==x):
         d[2][4]=y
    if (d[2][5]==x):
         d[2][5]=y
    print(d)

d = {1: {2:3, 3:4}, 2:{4:4, 5:3}} 
replace_all(d,3,1)

#J 
"""Removes all pairs with value x. 
Given:  d = {1:2, 2:3, 3:2, 4:3}
Usage:  rm(d,2)
Results: {2:3, 4:3}
"""
def rm(d, x):
    for g in d.keys(): #looks for 2's in values
        if(d[g]==x):
            del d[g] #deletes 2's
    print(d)
d = {1:2, 2:3, 3:2, 4:3}
rm(d,2)