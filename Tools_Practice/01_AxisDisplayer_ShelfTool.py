from maya import cmds

#This is is for turning off the local Axis
sel = cmds.ls(selection=True)
if(len(sel)==0):
    print "No object selected"
else:
    print "Selection -> Local Rotation Axis [On]"
    for object in sel:
        cmds.setAttr(object+".displayLocalAxis",1)