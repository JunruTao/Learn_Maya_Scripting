# coding=utf-8
import controller_manager as cm
import utility as util
from PySide2 import QtWidgets, QtCore, QtGui
import pprint
import imp
imp.reload(util)


class ConLibUI(QtWidgets.QDialog):
    def __init__(self, parent=util.get_maya_window()):
        super(ConLibUI, self).__init__(parent)

        # [Database and values]
        self.version_str = 'Tao_Controller_Library_ver0.1'
        self.library = cm.ControllerManager()

        # [QT Window Properties]
        self.setObjectName('CTR_Lib_UI_Main_Window')
        self.setWindowTitle('Controller Library')
        self.setMinimumWidth(300)
        self.setMinimumHeight(400)
        # only happens on windows (getting rid of the):
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setAttribute(QtCore.Qt.WA_AlwaysShowToolTips)

        # [QT Building UI]
        self.build_ui()
        self.populate()

    def build_ui(self):
        # [Master Layout] 0.1 - Construct
        master_layout = QtWidgets.QVBoxLayout(self)  # parent to this window. ->this_ptr

        # [Save Button and Name string input]
        # ===== 1.1 Construct Save Field Layout
        save_field_widget = QtWidgets.QWidget()
        save_field_layout = QtWidgets.QHBoxLayout(save_field_widget)

        master_layout.addWidget(save_field_widget)
        # ===== 1.2 String input `LineEdit` add to layout
        self.saveNameField = QtWidgets.QLineEdit()  # String input to name
        save_field_layout.addWidget(self.saveNameField)
        # ===== 1.3 Save Button add to layout
        self.buttonSave = QtWidgets.QPushButton('Save')
        self.buttonSave.clicked.connect(self.save)
        save_field_layout.addWidget(self.buttonSave)

        # [List Widget]
        self.listWidget = QtWidgets.QListWidget()
        self.listWidget.setViewMode(QtWidgets.QListWidget.IconMode)
        self.listWidget.setIconSize(QtCore.QSize(64, 64))
        self.listWidget.setResizeMode(QtWidgets.QListWidget.Adjust)
        self.listWidget.setGridSize(QtCore.QSize(80, 80))
        master_layout.addWidget(self.listWidget)

        # [Buttons Widget]
        buttons_widget = QtWidgets.QWidget()
        buttons_layout = QtWidgets.QHBoxLayout(buttons_widget)
        master_layout.addWidget(buttons_widget)

        self.buttonImport = QtWidgets.QPushButton('Import')
        self.buttonRefresh = QtWidgets.QPushButton('Refresh')
        self.buttonClose = QtWidgets.QPushButton('Close')

        self.buttonClose.clicked.connect(self.close)  # function ptr
        self.buttonRefresh.clicked.connect(self.populate)  # function ptr
        self.buttonImport.clicked.connect(self.load)

        buttons_layout.addWidget(self.buttonImport)
        buttons_layout.addWidget(self.buttonRefresh)
        buttons_layout.addWidget(self.buttonClose)

    def populate(self):
        self.listWidget.clear()
        self.library.find()

        for name, info in self.library.items():
            item = QtWidgets.QListWidgetItem(name)
            self.listWidget.addItem(item)

            screenshot = info.get('screenshot')
            if screenshot:
                icon = QtGui.QIcon(screenshot)
                item.setIcon(icon)

            # [Bug with Maya]: Sometimes, the tool tip is now shown at all. This is the issue
            # Maya's settings.(when `Tool clip` is disabled, QtGui.QToolTip is also disabled)
            # {SOLUTION} Go to Window ->Settings/Preferences ->[Preferences]–[Help],
            # and make sure Display `Tool clips` is on.
            item.setToolTip(pprint.pformat(info))

    def load(self):
        current_item = self.listWidget.currentItem()
        if not current_item:
            return

        name = current_item.text()
        self.library.load(name)

    def save(self):
        name = self.saveNameField.text()
        if not name.strip():
            raise Warning("[Controller Library UI - Save] No name specified")
        print("name: %s" % name)

        self.library.save(name)
        self.populate()
        self.saveNameField.setText('')


def open_editor():
    ui = ConLibUI()
    ui.show()
    return ui
