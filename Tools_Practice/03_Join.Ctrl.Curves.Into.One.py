from maya import cmds

'''
This script is for joining multiple curves into one curve Object
'''
sel = cmds.ls(selection=True)
if sel:
    cmds.makeIdentity(sel, apply=True,t=True,r=True,s=True,n=False,pn=True)
    grp = cmds.group(em=True, name='joined_CTR_01')
    all_shapes = []
    for obj in sel:
        shapes = cmds.listRelatives(obj,shapes=True)
        if shapes:
            for s in shapes:
                cmds.parent(obj+"|"+s, grp, s=True, r=True)
    cmds.delete(sel)
    cmds.xform(grp, cp=True)
else:
    print "There's no selection"
