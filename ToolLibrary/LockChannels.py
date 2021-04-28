from maya import cmds

'''
This is script is for locking the translations of
the bones. 
'''

channels_to_lock = ["tx", "ty", "tz", "sx", "sy", "sz"]
print("Locking channels(translate and scale) of selected")
selected = cmds.ls(sl=True)
if selected:
    for item in selected:
        for ch in channels_to_lock:
            chnl = str(item) + "." + ch
            cmds.setAttr(chnl, lock=True)