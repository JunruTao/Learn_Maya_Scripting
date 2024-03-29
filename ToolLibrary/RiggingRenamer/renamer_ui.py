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
        self.setFixedSize(300, 240)
        # only happens on windows (getting rid of the):
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.prefix_ = util.load_old_prefix()
        self.build_ui()
        # [QT Building UI]
        self.show()

    def build_ui(self):

        main_tab = QtWidgets.QTabWidget(self)  # parent to this window. ->this_ptr
        main_tab.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        main_tab.setFixedSize(300, 240)

        panel1 = QtWidgets.QWidget()
        panel1.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        master_layout = QtWidgets.QVBoxLayout(panel1)
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

        panel2 = QtWidgets.QWidget()
        panel2.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        panel2_layout = QtWidgets.QVBoxLayout(panel2)

        new_name_widget = QtWidgets.QWidget()  # new name edit line.
        new_name_layout = QtWidgets.QHBoxLayout(new_name_widget)
        new_name_label = QtWidgets.QLabel("New Name: ")
        self.new_name_edit = QtWidgets.QLineEdit()
        padding_label = QtWidgets.QLabel("Padding:")
        self.padding_edit = QtWidgets.QLineEdit()
        self.padding_edit.setText("2")
        new_name_layout.addWidget(new_name_label, 1)
        new_name_layout.addWidget(self.new_name_edit, 3)
        new_name_layout.addWidget(padding_label, 1)
        new_name_layout.addWidget(self.padding_edit, 1)

        button_sel_hi = QtWidgets.QPushButton("Select Hierarchy")
        button_rename = QtWidgets.QPushButton("Rename Object/Sequence")
        button_rename.clicked.connect(self.rename_sq)
        button_sel_hi.clicked.connect(rn.select_hi)

        panel2_layout.addWidget(new_name_widget)
        panel2_layout.addWidget(button_sel_hi)
        panel2_layout.addWidget(button_rename)

        main_tab.addTab(panel1, "Pre/Suf Renaming")
        main_tab.addTab(panel2, "Sequence Renaming")

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

    def closeEvent(self, event):
        global perforceBrowserWnd
        global default_prefix
        perforceBrowserWnd = None
        util.write_to_cache_dir(self.prefix_edits.text())

    def rename_sq(self):
        rn.rename_sequence(self.new_name_edit.text(), int(self.padding_edit.text()))


def open_editor():
    global perforceBrowserWnd
    if perforceBrowserWnd is None:
        perforceBrowserWnd = RenamerUI()
    else:
        perforceBrowserWnd.close()
        perforceBrowserWnd = RenamerUI()
    perforceBrowserWnd.show()
