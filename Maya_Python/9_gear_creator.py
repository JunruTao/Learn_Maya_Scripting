import maya.cmds as cmds


def createGear(teeth=10, length=0.3):
    """
    This function will create a gear mesh procedurally
    :param teeth: number of teeth to create
    :param length: how long is the extrusion of the teeth
    :return:Tuple of the transform, constructor and extrude node
    """
    # teeth are alternative face so spans times 2
    spans = teeth * 2

    transform, constructor = cmds.polyPipe(subdivisionsAxis=spans)

    # side face index:  start---end-----every 2
    # range create a sequence like this
    sideFaces = range(spans * 2, spans * 3, 2)

    cmds.select(clear=True)

    for face in sideFaces:
        cmds.select("%s.f[%s]" % (transform, face), add=True)

    extrude = cmds.polyExtrudeFacet(localTranslateZ=length)[0]
    print(extrude)

    return transform, constructor, extrude


def changeTeeth(constructor, extrude, teeth=10, length=0.3):
    spans = teeth * 2

    #edit=True is important. taking the existing node and change that.
    cmds.polyPipe(constructor, edit=True, subdivisionsAxis=spans)

    sideFaces = range(spans * 2, spans * 3, 2)
    faceNames = []

    for face in sideFaces:
        facename = "f[%s]"%(face)
        faceNames.append(facename)
        
    #note: *faceNames -> the `*` means expanding the list into individual arguements
    cmds.setAttr('%s.inputComponents' % (extrude),
                 len(faceNames),
                 *faceNames,
                 type="componentList")
    cmds.polyExtrudeFacet(extrude, edit=True, ltz=length)



#as running the script in maya:
#the scripts: .py, .pyc should be under: /username/Document/maya/scripts/
# inside of maya, by calling:
import gearCreator
reload(gearCreator)

gearCreator.createGear()