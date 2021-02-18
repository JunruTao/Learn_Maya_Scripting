from PySide2 import QtWidgets, QtCore, QtGui
import pymel.core as pm
import TaoUtility as TU
from functools import partial
import imp
imp.reload(TU)


class LightManager(QtWidgets.QDialog):

    light_types = {
        "Point Light": pm.pointLight,
        "Spot Light": pm.spotLight,
        "Directional Light": pm.directionalLight,
        "Area Light": partial(pm.shadingNode, 'areaLight', asLight=True),
        "Volume Light": partial(pm.shadingNode, 'volumeLight', asLight=True)
    }

    def __init__(self, parent=TU.get_maya_window()):
        super(LightManager, self).__init__(parent)

        win_name = "QtWin_LightManager"
        win_title = "Light Manager"
        win_size = (200, 300)

        # [QT Window Properties]
        self.setObjectName(win_name)
        self.setWindowTitle(win_title)
        self.setMinimumSize(*win_size)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setAttribute(QtCore.Qt.WA_AlwaysShowToolTips)

        self.build_ui()

    def build_ui(self):
        lay_master = QtWidgets.QGridLayout(self)

        self.CB_light_type = QtWidgets.QComboBox()
        for light_type in sorted(self.light_types):
            self.CB_light_type.addItem(light_type)

        lay_master.addWidget(self.CB_light_type, 0, 0)  # start pos

        self.buttonCreate = QtWidgets.QPushButton('Create')
        self.buttonCreate.clicked.connect(self.create_light)
        lay_master.addWidget(self.buttonCreate, 0, 1)

        scroll_widget = QtWidgets.QWidget()
        scroll_widget.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        self.lay_scroll = QtWidgets.QVBoxLayout(scroll_widget)

        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_widget)
        lay_master.addWidget(scroll_area, 1, 0, 1, 2)

    def create_light(self):
        light_type = self.CB_light_type.currentText()
        func_ptr = self.light_types[light_type]
        light = func_ptr()
        widget = LightWidget(light)
        self.lay_scroll.addWidget(widget)


class LightWidget(QtWidgets.QWidget):
    def __init__(self, light):
        super(LightWidget, self).__init__()
        if isinstance(light, basestring):
            light = pm.PyNode(light)

        self.light = light
        self.build_ui()

    def build_ui(self):
        lay_master = QtWidgets.QGridLayout(self)

        self.name = QtWidgets.QCheckBox(str(self.light.getTransform()))
        self.name.setChecked(self.light.visibility.get())
        self.name.toggled.connect(lambda val: self.light.getTransform().visibility.set(val))
        lay_master.addWidget(self.name, 0, 0)


def display():
    ui = LightManager()
    ui.show()
    return ui
