from maya import cmds


def tween(percentage=50, obj=None, attrs=None, selection=True):
    """
    This is a small demo function allowing users to morph values between 2 keyframes
    :param percentage: tween percentage
    :param obj: object in the selection
    :param attrs: attributes to tween
    :param selection: bool; selection toggle
    :return:
    """

    # If object wasn't given and selection is set to False. Raise error
    if not obj and not selection:
        raise ValueError("No Object is given to tween")

    # if there is no object specified, select the first object in the scene
    if not obj:
        obj = cmds.ls(selection=True)[0]

    #  if there is no attribute specified, all key-able attributes will be set to tween
    if not attrs:
        attrs = cmds.listAttr(obj, keyable=True)

    current_time = cmds.currentTime(query=True)

    debug_print_keyframes_and_channel = 0
    for attribute in attrs:
        # constructing the full name of the attribute channel
        attr_name = '{0}.{1}'.format(obj, attribute)
        keyframes = cmds.keyframe(attr_name, query=True)
        if not keyframes:
            continue
        elif debug_print_keyframes_and_channel:
            print('channel has key: [%s]' % attr_name)
            print(keyframes)

        # using a lambda function to replace for loop and if statement
        # `list comprehension` - temp-frame variable will be used only inside(faster)
        # [Same Logic]:
        ''' 
        for frame in keyframes:
           if frame < current_time:
              previous_keyframes.append(frame)
        '''
        previous_keyframes = [frame for frame in keyframes if frame < current_time]
        later_keyframes = [frame for frame in keyframes if frame > current_time]

        if not previous_keyframes and not later_keyframes:
            continue

        # 2 ways to do this:
        #   1. traditional if-else and max() statement
        if previous_keyframes:
            left_frame = max(previous_keyframes)
        else:
            left_frame = None

        #   2. condensed statement:(same logic above)
        right_frame = min(later_keyframes) if later_keyframes else None

        # either side of keyframe is none, then skip it.
        if not left_frame or not right_frame:
            continue

        left_value = cmds.getAttr(attr_name, time=left_frame)
        right_value = cmds.getAttr(attr_name, time=right_frame)

        # linear interpolation of 2 values:
        value = (percentage * right_value + ((100.0 - percentage) * left_value)) * 0.01
        cmds.setKeyframe(attr_name, time=current_time, value=value)


class TweenWindow(object):
    """
    This is an object that displays a simple UI to control the tween keyframe function
    """
    window_name = "Tween_Animation_Editor"
    slider = None

    def show(self):
        if cmds.window(self.window_name, query=True, exists=True):
            cmds.deleteUI(self.window_name)

        cmds.window(self.window_name)
        self.build_ui()
        cmds.window(self.window_name, edit=True, title="Tween Editor", widthHeight=(300, 90))
        cmds.showWindow()

    def build_ui(self):
        column = cmds.columnLayout(rowSpacing=3)
        cmds.text(label="Create keyframe between 2 keyframes")
        row = cmds.rowLayout(numberOfColumns=2)

        # this command will take a function pointer.
        self.slider = cmds.floatSlider(min=0, max=100, value=50, step=1, w=200, h=28, dragCommand=tween)
        cmds.button(label="Reset", w=40, h=28, command=self.reset)
        
        # in order to jump up a level also can use '..'
        cmds.setParent(column)
        cmds.button(label="Close", w=100, h=30, command=self.close)

    def reset(self, *args):
        cmds.floatSlider(self.slider, edit=True, value=50)

    def close(self, *args):
        cmds.deleteUI(self.window_name)
