from maya import cmds


class Gear(object):

    # variable here -> static class member(globally instanced)
    log = "JT 2020"

    def __init__(self, _debug_=False):
        # variable here -> object owned members
        self.debug = _debug_
        if _debug_:
            print(self.log)
        self.transform = None
        self.constructor = None
        self.extrude = None

    def create(self, teeth=10, length=0.3):
        """
        This function will create a gear mesh procedurally
        :param teeth: number of teeth to create
        :param length: how long is the extrusion of the teeth
        """
        # teeth are alternative face so spans times 2
        spans = teeth * 2

        self.transform, self.constructor = cmds.polyPipe(subdivisionsAxis=spans)

        # side face index:  start---end-----every 2
        # `range` create a sequence like this
        side_faces = range(spans * 2, spans * 3, 2)

        # how cmd works is selection load/unload at runtime
        cmds.select(clear=True)

        for face in side_faces:
            cmds.select("%s.f[%s]" % (self.transform, face), add=True)

        self.extrude = cmds.polyExtrudeFacet(localTranslateZ=length)[0]

        if self.debug:
            print(self.extrude)

    def modify(self, teeth=15, length=0.1):
        """
        This function will modify existing gear's profile
        :param teeth: number of teeth to create
        :param length: how long is the extrusion of the teeth
        """
        spans = teeth * 2
        cmds.polyPipe(self.constructor, edit=True, subdivisionsAxis=spans)

        side_faces = range(spans * 2, spans * 3, 2)
        face_names = []

        for face in side_faces:
            name = "f[%s]" % face
            face_names.append(name)

        cmds.setAttr('%s.inputComponents' % self.extrude,
                     len(face_names),
                     *face_names,
                     type="componentList")
        cmds.polyExtrudeFacet(self.extrude, edit=True, ltz=length)
