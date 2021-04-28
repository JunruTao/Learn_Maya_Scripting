from maya import cmds

'''
[Object Rename Tool] by Junru Tao 2021
file: renamer_core.py
use: this file contains all the functions that process the renaming functions
'''


nameLibrary = {
    "mesh": 'GEP',  # GEP: geometry polygon
    "joint": 'JNT',  # JNT: Joint
    "camera": '_skip_',  # Identifier to allow system to skip
    "nurbsCurve": 'CTR'
}


def rename_selection(prefix="", sides="", suffix_override=""):
    """
    renaming the selected objects
    :param suffix_override:
    :param prefix:
    :param sides: _L or _R as input
    :return: none
    """
    selection = cmds.ls(selection=True)
    if len(selection) == 0:
        # Nothing in the selection
        cmds.warning("No Objects to rename, please select objects")
        return
    for obj in selection:
        name = str(obj.split("|")[-1])  # getting the last item's short name in the selection
        names = name.split("_")
        if len(names) > 2:
            name = names[1]

        if not suffix_override:
            # getting the object type.
            obj_type = cmds.objectType(obj)
            suffix = nameLibrary.get(obj_type, 'GRP')

            # skipping the camera objects
            if suffix == '_skip_':
                continue
            elif suffix == 'GRP':
                children = cmds.listRelatives(obj, children=True, s=True) or []
                if len(children) >= 1:  # this happens when a nurbs curve
                    # We will take the first child
                    child = children[0]
                    obj_type = str(cmds.objectType(child))
                    print(obj_type)
                    if obj_type == "nurbsCurve":
                        suffix = "CTR"
                        new_name = prefix + "_" + name + "_" + suffix + sides
                        cmds.rename(obj, new_name)
                        continue
        else:
            # the existing suffix is presume found:
            suffix = suffix_override
            new_name = prefix + "_" + name + "_" + suffix + sides
            cmds.rename(obj, new_name)
            continue

        # already got the suffix
        if name.endswith(suffix):
            if not sides:
                new_name = name + sides
                cmds.rename(obj, new_name)
            continue
        elif name.endswith("_L"):
            new_name = name.replace("_L", sides)
            cmds.rename(obj, new_name)
            continue
        elif name.endswith("_R"):
            new_name = name.replace("_R", sides)
            cmds.rename(obj, new_name)
            continue

        new_name = prefix + "_" + name + "_" + suffix + sides
        cmds.rename(obj, new_name)
    # end for loop

# end rename selection function


def select_hi():
    """
    select hierarchy
    :return: none
    """
    cmds.select(hi=True)


