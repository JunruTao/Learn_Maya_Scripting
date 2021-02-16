
"""
    [Notes]:
    it is important that keep the functions separated from GUI system so that
    you can simply test them out in commands without touching the UI code.
    
    in pycharm, there is an easy way to create a python package:
    in the project explorer, right click on the path folder -> New*
    -> Python Package; Give it a name, and it will basically create a folder
    and a __init__.py file which usually left empty in here. And python search
    module function will treat the entire sub-dir as a package.
"""

# [Tip 1: Getting Maya's User Application Directory]
from maya import cmds

def get_maya_user_dir():
    return cmds.internalVar(userAppDir=True)

dir = get_maya_user_dir()
print dir

# > OUTPUT: C:/Users/1/Documents/maya/
# Very Useful Handy tool

# [Tip 2: Create a custom directory]
import os

def join_dir(base, suffix):
    return  os.path.join(base, suffix)

controller_dir = join_dir(dir, "controller_shape_lib")

# creating a custom function to manage
def create_dir(directory):
    if directory:
        if not os.path.exists(directory):
            os.mkdir(directory)
            
# calling the dir
create_dir(controller_dir)


# [Tip 3: Also import json, pprint libraries]

import json
import pprint


# [ Tip 4: inherit class from `dict` dictionary wihch is much easier to use
# dictionary functions to manage several files as objects in python]

# [ Tip 5: File Saving in Maya]
CONTROL = "controllers"
MASTER = get_maya_user_dir()
MASTER = join_dir(MASTER, CONTROL)
create_dir(MASTER)

name = "MyContoller_01"

# join that path as well create a file name:
path = join_dir(MASTER, '%s.ma' % name)

# here is a demo how to save our a Maya ASCII .ma file
cmds.file(rename=path)
cmds.file(save=True,type='mayaAscii',force=True)

# however if only exporting the selected objects, this is the way:
if cmds.ls(selection=True):
    cmds.file(force=True, type='mayaAscii', exportSelected=True)
else:
    cmds.file(save=True,type='mayaAscii',force=True)

# as this is in the same class:
self[name] = path


# loading the maya file:

def find(self, dir):
    if not os.path.exists(dir):
        return
    # -ls all the files in this directory
    files = os.listdir(dir)
    
    #****************************************************************************
    # much better way to filter out and matching the strings: <str>.endswith('..')
    # using this list lambda to push all the maya ascii in to this list
    mayaFiles = [f for f in files if f.endswith('.ma')]
    
    
    #####
    ##### This is `Find` function will be placed in the class which inherited from
    # `dict`, so using self[name] will access key(name) and store it as it
    for ma in mayaFiles:
        # extract names
        name, ext = os.path.splitext(ma)
        # print name
        
        # the extension is got rig of, we will store {DIR}/filename as the `key`
        path = join_dir(dir, ma)
        # `name` as key, and store path in here
        self[name] = path
        
        ####CHANGES:
        info = {}
        infoFile = '%s.json' % name
        
        if infoFile in files:
            infoFile = join_dir(dir, infoFile)
            with open(infoFile,'r') as f:
                info = json.load(f)
        
        # so here, file with not extra info will least have these meta data
        # and the ones with json files loaded will have extra metadata appended into info
        info['name'] = name
        info['path'] = path
        self[name] = info
            
        
        
        # so if you print out this object, it will print out as a dictionary
    
    # using pprint, the flat-dictionary print will be printed as vertical list:
    # [key, value]
    pprint.pprint(self)
    
    
def load(self, name):
    # as info was dictonary all the information:
    path = self[name]['path']
    # file reading: -i(import), usingNamespaces will overcomplicate the structure
    cmds.file(path, i=True, usingNamespaces=False)
    
    

# define the save file function: 
# you can pass any extra arguments into the field: just like *args *kwargs
def save(self, name, dir, **info):
    # Try this out, you can put any flag at the back
    if 0:
        print info
        return
    
    create_dir(dir)
    path = join_dir(dir, '%s.ma' % name)
    infoFile = join_dir(dir, '%s.json' % name)
    # because info by itself is a dictionary:
    info['name'] = name
    info['path'] = path
    
    
    
    cmds.file(rename=path)
    
    if cmds.ls(selection=True):
        cmds.file(force=True, type='mayaAscii', exportSelected=True)
    else:
        cmds.file(save=True,type='mayaAscii',force=True)
        
    # Writing a json file: in this fashion:
    # - with -> func`open file`
    #   -> infoFile(File Path) -> 'w'(Write File Mode)
    #   -> as a f (file stream):
    #   -> using json to dump `info` into f, with indentation as 4 spaces
    with open(infoFile, 'w') as f:
        json.dump(info, f, indent=4)
    
    #store the dictionary info into this:
    self[name] = info
    
    # ^^^^ Changes in Load() as well. reading the json and store in self[name]