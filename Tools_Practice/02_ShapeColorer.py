from maya import cmds

'''
This script is for coloring nurbs controllers,
as there could be various of shape under the 
nurbs obj. Manual functions is not effecient.
-Junru Tao 2021
'''
def setRGBColor(shape, color = (1,1,1,1)):
    rgb = ("R","G","B")
    cmds.setAttr(shape + ".overrideEnabled",1)
    cmds.setAttr(shape + ".overrideRGBColors",1)
    for channel, color in zip(rgb, color):
        cmds.setAttr(shape + ".overrideColor%s" %channel, color)

cmds.colorEditor()
if cmds.colorEditor(query=True, result=True):
    values = cmds.colorEditor(query=True, rgb=True)
    print str(values)
    sel = cmds.ls(selection=True)
    shapes = ()
    if sel:
        shapes = cmds.listRelatives(sel[0],shapes=True)
        if shapes:
            for item in shapes:
                full_name = sel[0] + "|" + item
                setRGBColor(full_name,values)
        else:
            print "[Error] No shapes in this object"
    else:
        print "[Error] No selection"

