from PySide2 import QtWidgets, QtCore, QtGui
import renamer_core as rn
import utility as util
reload(rn)
reload(util)

perforceBrowserWnd = None
default_prefix = ''


class RenamerUI(QtWidgets.QDialog):

    def __init__(self, parent=util.get_maya_window()):

        super(RenamerUI, self).__init__(parent)

        # [QT Window Properties]
        self.setObjectName('Renamer_UI_Main_Window')
        self.setWindowTitle('Rigging Renamer')
        self.setFixedSize(300, 200)
        # only happens on windows (getting rid of the):
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.prefix_ = util.load_old_prefix()
        self.build_ui()
        # [QT Building UI]

    def build_ui(self):

        master_layout = QtWidgets.QVBoxLayout(self)  # parent to this window. ->this_ptr
        master_layout.setSpacing(0)
        master_layout.addStretch()
        master_layout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)

        prefix_widget = QtWidgets.QWidget()  # empty widget
        prefix_layout = QtWidgets.QHBoxLayout(prefix_widget)  # add a layout to widget

        # [ Prefix  Widget ] ==================================================
        prefix_label = QtWidgets.QLabel("Prefix: ")
        self.prefix_edits = QtWidgets.QLineEdit()
        self.prefix_edits.setText(self.prefix_)
        prefix_layout.addWidget(prefix_label)
        prefix_layout.addWidget(self.prefix_edits)

        # [ Override Suffix  Widget ] ==================================================
        override_widget = QtWidgets.QWidget()
        override_layout = QtWidgets.QHBoxLayout(override_widget)
        self.suffix_override = QtWidgets.QLineEdit()
        self.clear_override_button = QtWidgets.QPushButton("Clear")
        self.clear_override_button.clicked.connect(lambda: self.suffix_override.setText(""))

        override_layout.addWidget(QtWidgets.QLabel("Suffix Override: "))
        override_layout.addWidget(self.suffix_override, 3)
        override_layout.addWidget(self.clear_override_button)

        # [ Renamer Buttons  Widgets ] ==================================================
        self.button_select_hi = QtWidgets.QPushButton("Select Hierarchy")
        self.button_rename1 = QtWidgets.QPushButton("Rename Selected")
        self.button_renameL = QtWidgets.QPushButton("Rename on Left")
        self.button_renameR = QtWidgets.QPushButton("Rename on Right")

        self.button_select_hi.clicked.connect(rn.select_hi)
        self.button_rename1.clicked.connect(self.rename_sel)
        self.button_renameL.clicked.connect(self.rename_l)
        self.button_renameR.clicked.connect(self.rename_r)

        self.button_select_hi.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.button_rename1.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.button_renameL.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.button_renameR.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        button_widgets2 = QtWidgets.QWidget()  # empty widget
        buttons_layout2 = QtWidgets.QHBoxLayout(button_widgets2)  # add a layout to widget
        buttons_layout2.addWidget(self.button_renameL, 1)
        buttons_layout2.addWidget(self.button_renameR, 1)
        buttons_layout2.setSpacing(0)
        buttons_layout2.setMargin(0)

        button_widgets2.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        # adding widgets to main layout
        master_layout.addWidget(prefix_widget)
        master_layout.setSpacing(0)
        master_layout.addStretch()
        master_layout.addWidget(override_widget)
        master_layout.addWidget(self.button_select_hi, 1)
        master_layout.setSpacing(3)
        master_layout.addWidget(self.button_rename1, 2)
        master_layout.setSpacing(0)
        master_layout.addStretch()
        master_layout.addWidget(button_widgets2, 2)

    def rename_sel(self):
        global default_prefix
        prefix = self.prefix_edits.text()
        default_prefix = prefix
        rn.rename_selection(prefix, '', self.suffix_override.text())

    def rename_l(self):
        global default_prefix
        prefix = self.prefix_edits.text()
        default_prefix = prefix
        rn.rename_selection(prefix, '_L', self.suffix_override.text())

    def rename_r(self):
        global default_prefix
        prefix = self.prefix_edits.text()
        default_prefix = prefix
        rn.rename_selection(prefix, '_R', self.suffix_override.text())

    def closeEvent(*args, **kwargs):
        global perforceBrowserWnd
        global default_prefix
        perforceBrowserWnd = None
        util.write_to_cache_dir(default_prefix)


def open_editor():
    global perforceBrowserWnd
    if perforceBrowserWnd is None:
        perforceBrowserWnd = RenamerUI()
    else:
        perforceBrowserWnd.close()
        perforceBrowserWnd = RenamerUI()
    perforceBrowserWnd.show()
