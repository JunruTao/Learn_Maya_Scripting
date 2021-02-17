from maya import cmds
import imp
import os
import json
import pprint
import utility as util

imp.reload(util)

# Global Variables
CONTROLLER_FOLDER = util.join_dir(util.get_maya_user_dir(), 'controllerCollection')


def create_controller_folder(directory='', o=False):
    """
    [Create/Set Controller Folder] Create a new Controller Folder, if directory not specified,
    {$MAYA_USER_DIR}/{$CONTROLLER_FOLDER} will be set as default. Use o=True flag to open up
    the controller folder in file explorer
        :param directory: (String) A directory to specify, non will create
        :param o: (Boolean) if Open this directory in file explorer
    """
    # Controller folder variable could be altered: use global keyword to grant access
    global CONTROLLER_FOLDER
    if not directory:
        directory = CONTROLLER_FOLDER
    else:
        CONTROLLER_FOLDER = directory
    if util.create_dir(directory):
        print("[CONTROLLER FOLDER] -> Created path: %s" % directory)
    else:
        print("[CONTROLLER FOLDER] -> File Path Exists: %s" % directory)

    # with -o flag on, open up the folder in file explorer
    if o:
        print("[CONTROLLER FOLDER] -> Open=True")
        util.open_folder(directory)


def get_controller_folder():
    return CONTROLLER_FOLDER


def open_controller_folder():
    util.open_folder(CONTROLLER_FOLDER)


def set_controller_folder(directory):
    # Controller folder variable could be altered: use global keyword to grant access
    global CONTROLLER_FOLDER
    CONTROLLER_FOLDER = directory


class ControllerManager(dict):
    """
    [Controller Manager]
        - Dictionary Class handling create, save and loading controller geometries
        and its adjacent information.
            -> geo.ma [maya ASCII, controller geometry]
            -> geo.json [meta data, controller info]
            -> geo.jpg [icon-thumbnail]
    """

    def save(self, name='', directory=CONTROLLER_FOLDER, screenshot=True, **info):
        """
        [CM]- SAVE() Saving out Controller geometry and its relevant info
            :param name:(string) File name
            :param directory:(string) default path to {$MAYA_USER_DIR}/{$CONTROLLER_FOLDER}
            :param screenshot (Boolean) if saving the screenshot to dist
            :param info: (Dict) extra properties to burn to meta data
            :return:
        """
        # construct the file path for geo and json
        geo_path = util.join_file_dir(directory, name, 'ma')
        info_path = util.join_file_dir(directory, name, 'json')
        # create the directory folder to save
        util.create_dir(directory)
        # save geometry(prompt window appear if no selection)
        util.save_maya_file(geo_path)
        # save screenshot
        if screenshot:
            info['screenshot'] = util.save_screenshot(name, directory)
        # store Meta-data block to CM's dictionary(memory)
        info['name'] = name
        info['path'] = geo_path
        # append other information down here
        self[name] = info
        # [LAST STEP] save out info-block to json
        util.save_json_file(info, info_path)

    def find(self, directory=CONTROLLER_FOLDER, p=False):
        """
        [CM]- FIND() Search under the Controller Directory and load the info to memory
            :param directory: (String) Directory to search from
            :param p: (Boolean) if Print out the result
            :return: (Boolean) if found
        """
        if not os.path.exists(directory):
            print("CM->Find(): Invalid Directory")
            return False

        # getting all the files under this directory
        all_files = os.listdir(directory)

        # using a list lambda to get all the maya files
        maya_files = [f for f in all_files if f.endswith('.ma')]

        for ma_file in maya_files:
            # splitting out the name
            name, ext = os.path.splitext(ma_file)
            # get the `full path` of maya geometry files
            path = util.join_dir(directory, ma_file)
            # finding the info files and load into memory
            info_file_name = '%s.json' % name
            if info_file_name in all_files:
                info_path = util.join_dir(directory, info_file_name)
                with open(info_path, 'r') as f:
                    info_block = json.load(f)
            else:
                info_block = {}

            # find screenshot file under the same dir
            screenshot = '%s.jpg' % name
            if screenshot in all_files:
                info_block['screenshot'] = util.join_dir(directory, screenshot)

            info_block['name'] = name
            info_block['path'] = path
            self[name] = info_block

        if p:  # Printing the Lists and Info
            print("[Found %s Controllers]: Meta Data Loaded" % len(maya_files))
            pprint.pprint(self)

        return True

    def load(self, name=''):
        """
        [CM]- LOAD() Load the Controller geometry
            :param name: (String) name of controller to load
            :return: (Boolean) Found
        """
        path = self[name]['path']
        if path:
            # importing maya files to the scene (-i -> -import)
            cmds.file(path, i=True, usingNamespaces=False)
            return True
        else:
            print("[CM]-Load: Controller NOT found in database, call CM->find() to search")
            return False
