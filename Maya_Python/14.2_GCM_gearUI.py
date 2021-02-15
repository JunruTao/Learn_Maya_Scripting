from maya import cmds
import imp
import gearCreatorV3 as gM
imp.reload(gM)
text_info = "This is Gear Creator v3.0 by Junru Tao 2021\n" \
            "script adaption based on Dhruv's demo 2017"


class WindowManager(object):
    """
    This is the base class manages create and destroy a window wrapping maya cmd.
    [The global Params] these shall be override in the derived classes
    """
    window_id = "Base_Window"
    window_title = "Editor"
    window_dim = (200, 100)

    def show(self):
        """
        [Show Window]This function will be called by the this object and its children
        """
        # preventing duplicated window showing up, note: window titles are different from window_id
        if cmds.window(self.window_id, exists=True):  # note: -exists flag in MEL will ignore other flags
            cmds.deleteUI(self.window_id)

        # Creating the actual window(however window with same was tested)
        cmds.window(self.window_id)
        # Call the override functions here
        self.build_ui()
        # This is a post-adjustment measure, [post-edit] will make sure the window_size/title adjusted
        cmds.window(self.window_id, edit=True, title=self.window_title, widthHeight=self.window_dim)
        # Showing the window
        cmds.showWindow()

    def build_ui(self):
        pass

    def close(self, *args):
        cmds.deleteUI(self.window_id)


class GearCreator(WindowManager):
    """
    [Gear Creator] Inherited from WM, is a class creates a UI for a basic Gear Object creation
    and modification. Functions from base class: 'show()'
    """
    window_id = "GCW_WindowEditor_ID"
    window_title = "Gear Maker"
    window_dim = (300, 256)

    # data container referencing the gears
    def __init__(self):
        self.gears = []
        self.num_gear_id = ''
        self.gear_list_id = ''

        self.num_teeth = 10
        self.num_teeth_slider_id = ''
        self.num_teeth_label_id = ''
        self.num_teeth_txt = "Teeth: {0}"

        self.length = 0.3
        self.length_slider_id = ''
        self.length_label_id = ''
        self.length_txt = "Len: {:.2f}"

    def build_ui(self):
        """
        [Override Function] Create the GUI Layout
        :return:
        """
        column = cmds.columnLayout(rowSpacing=3)
        cmds.separator()
        cmds.text(label=text_info, w=290, font="smallBoldLabelFont")
        cmds.separator()

        cmds.rowLayout(numberOfColumns=3)
        cmds.button(label="Create", w=95, h=28, command=self.create)
        cmds.button(label="Load", w=95, h=28, command=self.load)
        cmds.button(label="Release", w=100, h=28, command=self.release)

        cmds.setParent(column)
        self.num_gear_id = cmds.text(label="Number of Gears: %s" % len(self.gears), w=290)

        cmds.paneLayout()
        self.gear_list_id = cmds.textScrollList(numberOfRows=6, allowMultiSelection=False, w=290)

        cmds.setParent(column)
        cmds.rowLayout(numberOfColumns=3)
        self.num_teeth_label_id = cmds.text(label=self.num_teeth_txt.format(self.num_teeth), w=80)
        self.num_teeth_slider_id = cmds.intSlider(
            min=0, max=40,
            value=self.num_teeth,
            w=150, h=28,
            dragCommand=self.tweak_num_teeth)
        cmds.button(label="Reset", w=50, h=28, command=self.reset_t)

        cmds.setParent(column)
        cmds.rowLayout(numberOfColumns=3)
        self.length_label_id = cmds.text(label=self.length_txt.format(self.length), w=80)
        self.length_slider_id = cmds.floatSlider(
            min=0.001, max=2.0, step=0.01,
            value=self.length,
            w=150, h=28,
            dragCommand=self.tweak_length)
        cmds.button(label="Reset", w=50, h=28, command=self.reset_l)

    def load(self, *args):
        """
        Loading existing Gears into the scene
        :return:
        """
        selection = cmds.ls(selection=True)
        if selection:
            self.release()
            for obj in selection:
                new_gear = gM.Gear()
                status = new_gear.load(obj)
                if status:
                    self.gears.append(new_gear)
                else:
                    continue
        self.update_list()

    def release(self, *args):
        """
        Clearing all the reference to gear objects
        """
        del self.gears[:]
        self.update_list()

    def create(self, *args):
        self.release()
        new_gear = gM.Gear()
        new_gear.create(self.num_teeth, self.length)
        self.gears.append(new_gear)
        self.update_list()
        pass

    def tweak_num_teeth(self, teeth):
        self.num_teeth = teeth
        self.tweak()
        cmds.text(self.num_teeth_label_id, edit=True, label=self.num_teeth_txt.format(self.num_teeth))

    def tweak_length(self, length):
        self.length = length
        self.tweak()
        cmds.text(self.length_label_id, edit=True, label=self.length_txt.format(self.length))

    def tweak(self):
        if self.gears:
            for gear in self.gears:
                gear.modify(self.num_teeth, self.length)

    def update_list(self, *args):
        cmds.text(self.num_gear_id, edit=True, label="Number of Gears: %s" % len(self.gears))
        cmds.textScrollList(self.gear_list_id, edit=True, removeAll=True)
        _list = []
        if self.gears:
            for item in self.gears:
                _list.append(item.transform)
        cmds.textScrollList(self.gear_list_id, edit=True, append=_list)
        print("[Gear Creator] Update Gear Object List")
        pass

    def reset_t(self, *args):
        self.num_teeth = 10
        cmds.intSlider(self.num_teeth_slider_id, edit=True, value=self.num_teeth)
        cmds.text(self.num_teeth_label_id, edit=True, label=self.num_teeth_txt.format(self.num_teeth))
        pass

    def reset_l(self, *args):
        self.length = 0.3
        cmds.floatSlider(self.length_slider_id, edit=True, value=self.length)
        cmds.text(self.length_label_id, edit=True, label=self.length_txt.format(self.length))
        pass

