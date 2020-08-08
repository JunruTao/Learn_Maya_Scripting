import maya.cmds as cmds

SUFFIXES = {
    "mesh":"GEO",
    "joint":"JNT",
    "camera":None,
    "pointLight":"LGT",
    "ambientLight":"LGT"
}

DEFAULT_SUFFIX = "GRP"

def rename():
    """
    This function will rename any objects to have correct suffix

    Returns:
        A List of objects that operated on
    """
    #this is the helper comment, you can use print help(objRenamer.rename) to print these to console
    selection = cmds.ls(selection=True)

    if len(selection) == 0:
        selection = cmds.ls(dag=True, long=True)
    
    selection.sort(key=len, reverse=True)

    for obj in selection:
        shortName = obj.split("|")[-1] #getting the last element once it's split into lists

        # If the object is a transform, then we should check if it has a shape below it
        children = cmds.listRelatives(obj, children=True, fullPath=True) or []

        objType = None

        if len(children) == 1:
            child = children[0]
            objType = cmds.objectType(child)
        else:
            objType = cmds.objectType(obj)
        
        suffix = SUFFIXES.get(objType, DEFAULT_SUFFIX)
        if not suffix:
            continue

        if obj.endswith(suffix):
            continue

        newName = "%s_%s"%(shortName,suffix)
        cmds.rename(obj, newName)

        index = selection.index(obj)
        selection[index] = obj.replace(shortName, newName)
        #now this local list will be replaced by newly named names
        #you can print out this function by print objRenamer.rename()
    
    return selection