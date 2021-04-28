from maya import cmds
'''
This script is for orienting the Leg Joints
'''
# Select the node top node.
root = cmds.ls(selection=True, l=True)[0].split("|")[1]
cmds.select(root, hi=True)

# List all the nodes in the chain
nodes = cmds.ls(selection=True, l=True)

# orient the joint as X is the up vector
cmds.joint(
        edit=True, 
        oj='xyz', 
        secondaryAxisOrient='xup',
        ch=True, # Childern
        zso=True # Zero Scale Orient
)
cmds.select(clear=True)
cmds.select(nodes[-1])
cmds.joint(
        edit=True,
        oj='none',
        ch=False,
        zso=True
)
cmds.select(clear=True)