from maya import cmds
from functools import partial


def playblast_test():

    win = cmds.window(title="play blast test", menuBar=True, height=400, width=200, resizeToFitChildren=True)
    col = cmds.columnLayout()
    sf = 1
    ef = 10
    cmds.text(label="some text")
    name = cmds.textField()
    cmds.button(label="Play Blast",command = 'cmds.playblast(st="%s", et="%s")'%(sf,ef))
    cmds.showWindow(win)

playblast_test()
