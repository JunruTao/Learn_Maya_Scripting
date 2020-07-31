#Get access to the help functions
#goto both maya's and python's website, find the documentations

#or you can do this in maya's script editor

#----Printing out the documentation about list
print help(list)
#use dir() function to get all the function object that object
a = list()
print dir(a)

#--------------------------------------------------------
#LS command
from maya import cmds
print cmds.ls()

