from __future__ import division

#creating array from 1 at 9
data = range(10)
#adding 11 to 15
data.extend(range(11,16))
#adding 16
data.append(16)

#tuple is imutable
tuple = (1,2)
print tuple

#dictionary
person = {"name" : "Alexander", "age" : 25, "has_university" : 1}
print person.keys()
print person.values()

#if statement
if 1 == 2:
    print 1
else:
    print 2    

#for statement
for item in tuple:
    print item

#if statement with objetct
for item in [person]:
    print item["name"]

#statement function
def calculate_basic_operators(a , b):
    return (a+b), (a-b), (a*b), (a/b)

print calculate_basic_operators(2,2)    

#class statement
class Person:
    def __init__(self, values=None):
       self.name = "Teste" 
       self.age = 0
       self.has_university = 0

       print self.name

           