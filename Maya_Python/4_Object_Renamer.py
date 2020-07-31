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
# This will print out all the objects in the scene, including all the hidden ones
#ls has input parameters, such as selection (sl) <- boolean type
#so you can do:
print cdms.ls(selection=True)

#while doing this, the return is a list, that means you can store that in a variable
sel = cmds.ls(selection=True)
print sel

#--------------------------------------------------------
#if statement(has a scope) 
#`len()` to get the size of list
if len(sel) == 0:
    sel = cmds.ls(dag=True, long=True) 
    # dag - short for dagObject, all the objects listed in outliner
    # long - if returning the full path of the object(avoid conflicts layers under has the same name)

#here outside the scope:
sel.sort()#default list.sort will sort objects alphabetically
sel.sort(key=len, reversed=True)
#now it will sort by how long the name(obj path) is, and from long to short because of reversing
print sel
# if the selection at line22 is none, the if statement at line27 will execute, listing all object in the outliner

#--------------------------------------------------------
#for loop:
#   for item in List (grammar)
for object in sel:
    print object

# however the using ls()function in maya, gives you the output of objects' path
# which are strings i.g. "| joint1 | joint2 | joint4 |" <<<--- the `joint1` is at the top
# and `joint4` is acturally the object's name.
# By using split() function to split this at pipe `|` into a sub list [u'', u'joint1', u'joint2', u'joint4']

for object in sel:
    objName = object.split("|")[-1] 
    print objName
    #this will perfrom a basic parsing process
    # [-1] means getting the last object of that list

#--------------------------------------------------------
###-----------From the Tutorial--------------------------
# Now we need to loop through the objects and rename them
# We'll use a for loop for this
# We step through all the items one by one in the selection object, assign it to a variable (obj) and run the logic below it
for obj in sel:
    # For each object in the selection list, run the following logic
    # The name will be something like grandparent|parent|child
    # We just want the child part of the name, so we split using the | character which gives us a list of ['grandparent', 'parent', 'child']
    # We need to get the last item in the list, so we use [-1]. This means we backwards through the list and pick the next item, which would therefore be the last item
    shortName = obj.split('|')[-1]
    print "Before rename: ", shortName

    # If the object is a transform, then we should check if it has a shape below it
    children = cmds.listRelatives(obj, children=True) or []

    # We will only do this if there is one child
    if len(children) == 1:
        # We will take the first child
        child = children[0]
        objType = cmds.objectType(child)
    else:
        # Now we get the object type of the current object
        objType = cmds.objectType(obj)
    print objType

    if objType == "mesh":
        suffix = 'geo'
    elif objType == "joint":
        suffix = 'jnt'
    elif objType == 'camera':
        # In the case of the camera, we will say to continue.
        # Continue means that we will continue on to the next item in the list and skip the rest of the logic for this one
        print "Skipping camera"
        continue
    else:
        suffix = 'grp'


    newName = shortName + "_" + suffix
    print newName
    cmds.rename(obj, newName) #obj as the full path, new name as the name.
#end of for loop
