import maya.OpenMayaUI as oMI
from maya import cmds
import os
from shiboken2 import wrapInstance
from PySide2 import QtWidgets


def get_maya_window():
    """
    in order to set the parent that floats above Maya's main interface. This function
    allows you to return a long pointer(2.7, in Py3 use int(prt) instead).
    :return: long_ptr to maya QtWidget mainWindow object
    """
    main_window_ptr = oMI.MQtUtil.mainWindow()
    if main_window_ptr:
        return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


def write_to_cache_dir(prefix=''):
    path = os.path.join(os.path.dirname(__file__), "old_prefix.txt")
    f = open(path, 'w')
    f.write(prefix)
    f.close()


def load_old_prefix():
    path = os.path.join(os.path.dirname(__file__), "old_prefix.txt")
    try:
        f = open(path, 'r')
    except:
        return

    data = f.read()
    print data

    return data
