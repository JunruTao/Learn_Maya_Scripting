#in Python self keyword is same with `this` pointer

class Animal(object):
    name = None
    def speak(self):
        print "My name is", self.name
        
    def walk(self):
        print "I can walk"
    
    def breath(self):
        print "I can breath"
        
#using class in python:
tiger = Animal()
tiger.name = 'Tiger'
tiger.speak()


#Inheritance:
class Dog(Animal):
    kind = "Smart Dog"
    #class function overloading:
    def speak(self):
        print "Woof"
        
    def getKind(self):
        print self.kind

Nato = Dog()
Nato.speak()
Nato.getKind()
#checking the inheritance:
print isinstance(Nato,Animal)


#In Maya example:
#--------------------------------
from maya import cmds


class Gear(object):
    log = "JT 2020"

    def create(self):
        print(self.log)

import gearCreatorV2 as gc
reload(gc)

obj = gc.Gear()
obj.create()