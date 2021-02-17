from maya import cmds
import os
import json
import pprint


def join_dir(directory='', name=''):
    if directory and name:
        return os.path.join(directory, name)
    else:
        raise RuntimeError("Util.[join_dir]: No Directory Specified")


def create_dir(directory=''):
    if directory:
        if not os.path.exists(directory):
            os.mkdir(directory)
            return True
        else:
            return False
    else:
        raise RuntimeError("Util.[create_dir]: No Directory Specified")


def join_file_dir(directory='', name='', extension='txt'):
    """
    [Utility -> Save Maya File] If there is no object selected; The entire maya scene will
    be saved out as the new file.
        :param (string) directory: Base folder directory
        :param (string) name: file name
        :param (string) extension: file format
        :return: (string) file full path
    """
    if directory and name:
        return os.path.join(directory, '%s.%s' % (name, extension))
    else:
        raise RuntimeError("Util.[file_dir]: No Directory Specified")


def get_maya_user_dir():
    return cmds.internalVar(userAppDir=True)


def get_maya_script_dir():
    return cmds.internalVar(userScriptDir=True)


def save_maya_file(path=''):
    """
    [Utility -> Save Maya File] If there is no object selected; The entire maya scene will
    be saved out as the new file.
        :param path: (string) Maya file path to save
    """
    # making sure given a valid maya file
    if path and path.endswith('.ma'):
        cmds.file(rename=path)
        # selection toggle:
        if cmds.ls(selection=True):
            cmds.file(force=True, type='mayaAscii', exportSelected=True)
        else:
            # Here you might accidentally selected nothing and save out an entire scene
            # therefore it is nice to pop out a window to ask you to confirm
            result = cmds.confirmDialog(
                title='Save Confirm',
                message='[Warning]: You are about to save the entire scene as a controller\nDo you wish to continue?',
                defaultButton='Cancel',
                button=['Yes', 'Cancel'],
                cancelButton='Cancel',
                dismissString='Cancel'
            )
            if result == 'Yes':
                cmds.file(save=True, force=True, type='mayaAscii')
                print("Util.[save_maya_file]: [Save Entire Scene] as Controller to %s" % path)
            else:
                raise RuntimeError("Util.[save_maya_file]: [Save Entire Scene - Cancelled] Terminate Saving Process")
    else:
        raise RuntimeError("Util.[save_maya_file]: No valid maya file path")


def save_json_file(data, path='', indentation=4):
    """
    [Utility -> Save Json File]
        :param data: (string) dictionary[] format data to write
        :param path: (string) file path
        :param indentation: (int) number of spaces to indent
    """
    if path and path.endswith('.json'):
        path = os.path.realpath(path)
        with open(path, 'w') as f:
            json.dump(data, f, indent=indentation)
    else:
        raise RuntimeError("Util.[save_json_file]: No valid json file path")


def save_screenshot(name, directory=''):
    if directory:
        screenshot_path = join_file_dir(directory, name, 'jpg')
        cmds.setAttr('defaultRenderGlobals.ren', 'mayaHardware2', type='string')
        cmds.viewFit()
        cmds.setAttr('defaultRenderGlobals.imageFormat', 8)  # 8 Stands for .jpg format
        cmds.playblast(
            completeFilename=screenshot_path,
            forceOverwrite=True,
            width=200, height=200,
            showOrnaments=False,
            startTime=1, endTime=1,
            format="image",  # Bug in tut: needs to set this to 'image' so that it will cache
            viewer=False
        )
        return screenshot_path
    else:
        raise RuntimeError("Util.[save_screenshot]: No valid directory")


def open_folder(directory=''):
    if directory:
        path = os.path.realpath(directory)
        os.startfile(path)
        return True
    else:
        return False
