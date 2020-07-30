# This is the first lesson with maya python scripting
# Junru Tao 7/7/2020


#✪[ 𝐒𝐓𝐀𝐑𝐓 ]
#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬🅜▬🅐▬🅨▬🅐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

# ◉ Loading maya lib `maya command lib`
from maya import cmds

# ◉ python basic concole function
print 'Hello World'

#❒[Note]: 1. In order run the single script in maya, select the line you need to run:
#        2. click on the green icon {▶▶} with 2 arrows; or using [ctrl]+[Enter↵] keys



#✪[ 𝐂𝐑𝐄𝐀𝐓𝐄 ]
#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬🅜▬🅐▬🅨▬🅐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
cube = cmds.polyCube() #❒This will create a polycube and will be stored in `cube` variable
print cube             

#  ╓────────────────────────────RUN──────────────────────────────╖    ___________________
#  ║ >>>>>Maya Concole Output:  [u'pCube1', u'polyCube1'] ←‒‒‒‒‒‒╫‒‒‒│ `[]` means a List │
#  ║                             ↑     ↑            ↑            ║    ¯¯¯¯¯¯¯¯¯↑¯¯¯¯¯¯¯¯¯
#  ║    _________________________│__   │            │            ║             │
#  ║   │u''Stands for Unicode string│  │  __________│__________  ║             │
#  ║    ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ __│ │Maya Node Constructor│ ║             │
#  ║             ___________________│____ ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯  ║             │
#  ║            │Name String of the cube │                       ║             │
#  ║             ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯                        ║             │    
#  ╙─────────────────────────────────────────────────────────────╜             │
cubeShape = cube[0]    # ◀◀‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒#  Get the "first[0]" element #
print cubeShape                                                #  of this cube[list]         # 

#  ╓────────────────────────────RUN──────────────────────────────╖
#  ║ >>>  # Result: u'pCube1' #                                  ║
#  ╙─────────────────────────────────────────────────────────────╜



#✪[ 𝐆𝐄𝐓 𝐓𝐘𝐏𝐄 ]
#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬🅜▬🅐▬🅨▬🅐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
circle = cmds.circle()
print circle

#  ╓────────────────────────────RUN──────────────────────────────╖
#  ║ >>>  print circle                                           ║
#  ║ >>>  [u'nurbsCircle1', u'makeNurbCircle1']                  ║
#  ╙─────────────────────────────────────────────────────────────╜

# ◉ Getting the type of the variable:
# █[1]
type(circle)
#  ╓────────────────────────────RUN──────────────────────────────╖
#  ║ >>>  # Result: <type 'list'> #                              ║
#  ╙─────────────────────────────────────────────────────────────╜
# █[2]
type(circle[0])
#  ╓────────────────────────────RUN──────────────────────────────╖
#  ║ >>>  # Result: <type 'unicode'> #                           ║
#  ╙─────────────────────────────────────────────────────────────╜
#❒ Therefore objects' name in maya are unicode strings.
circleShape = circle[0]



#✪[ 𝐏𝐀𝐑𝐄𝐍𝐓 ]
#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬🅜▬🅐▬🅨▬🅐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
# ◉ Now we have 2 Objects, doing `parenting` on them:
# 
#   ⊝-circleShape  (u'nurbsCircle1')
#     ┃
#     ┗━❒ cubeShape   (u'pCube1')

cmds.parent(cubeShape, circleShape)


#✪[ 𝐋𝐎𝐂𝐊 𝐀𝐓𝐓𝐑𝐈𝐁𝐔𝐓𝐄𝐒 ]
#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬🅜▬🅐▬🅨▬🅐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

#in MEL: 𝘴𝘦𝘵𝘈𝘵𝘵𝘳 -𝘭𝘰𝘤𝘬 𝘵𝘳𝘶𝘦 "𝘱𝘊𝘶𝘣𝘦2.𝘵𝘹"    ◀‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒(locking pCube1's translate.x)

# ◉ Now Convert mel command to python
cmds.setAttr("pCube2.tx", lock = True)

#Now using the signed variables to do this procedurally
cmds.setAttr(cubeShape+".tx", lock = True)

#This will lock all the Transform attributes of the cubeshape we created
cmds.setAttr(cubeShape+".translate", lock = True)
cmds.setAttr(cubeShape+".rotate", lock = True)
cmds.setAttr(cubeShape+".scale", lock = True)

#✪[ 𝐒𝐄𝐋𝐄𝐂𝐓 ]
#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬🅜▬🅐▬🅨▬🅐▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
cmds.select(circleShape)


# ◉ So from now rerun the script in any new scene by {▶▶} you will get a cube parented under a 
#    Nurbs curve and won't be able to move, and you selection will assined to the circle shape
#    which become a simple rig allows you to move the cube around.




#_________________________________________________________________________________________________
#╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳
#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬🅔▬🅝▬🅓▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒