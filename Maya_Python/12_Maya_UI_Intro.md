### Overview of UI Libs in Maya
* Original Link: https://github.com/dgovil/AdvancedPythonForMaya/ by [Dhruv Govil](https://www.udemy.com/user/dhruv-govil/) at Udemy

### Maya UI & Qt
Timeline: Maya UI(Mel) <---- *ver 2011* ----> Qt
Mel, PyQt, PySide2


#### Python-cmds(MEL)
reference: https://download.autodesk.com/us/maya/2009help/CommandsPython/window.html
```
import maya.cmds as cmds

# Make a new window
#
window = cmds.window( title="Long Name", iconName='Short Name', widthHeight=(200, 55) )
cmds.columnLayout( adjustableColumn=True )
cmds.button( label='Do Nothing' )
cmds.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)') )
cmds.setParent( '..' )
cmds.showWindow( window )
```

----


### Qt - Prefered Method
A Combined version by `mottosso` -> **`Qt.py`**
very simple to use and automatically detect and load the right version of Qt libraries to use
TODO:
1. Clone repo: 
`git clone https://github.com/mottosso/Qt.py.git`
2. Under `Qt.py/` folder find `Qt.py`
3. Place it under `{$user-Maya}/scripts/`

**USAGE IN MAYA** [ Example: ]
```
    import Qt
    win = Qt.QtWidgets.QDialog()
    win.show()
```


#### Findings: If Placing Scripts in different folder under maya/script
**[ solution 1 ]:**
```
    import sys
    sys.path.append('../qt')

    import Qt as Qt
    reload(Qt)
    win = Qt.QtWidgets.QDialog()
    win.show()
```
**Other Methods:(better one)**
http://www.john-player.com/maya/creating-a-new-folder-in-your-maya-directory-from-python/


**[ solution 2 ]:**
due to maya 2019 using python 2.7:
making `qt.py` a **python module** will be a easier solution;
1. still placing `Qt.py` into the subfolder `qt` inside `{$user-Maya}/scripts/`
2. create a new file called "`__init__.py`", put a single line: `from qt import Qt`
3. then there's the simple part, In maya: call:
```
import qt.Qt as Qt
#reload(Qt)
win = Qt.QtWidgets.QDialog()
win.show()
...
```
4. however if the scripts are in a dev/pipeline structure, the solution 1 is perfered as all your scripts will placed into modules under various folders parallel to your asset folder.