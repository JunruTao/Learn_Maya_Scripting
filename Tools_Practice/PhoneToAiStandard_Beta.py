from maya import cmds

'''
A basic Phong Shader Cast into Arnold by Junru Tao.2020
PhongToAiStandard.py - Note: only transfering the surface color;
'''
def FindShared(culled=[],culling=[]):
    newList = []
    for item in culled:
        if item in culling:
            newList.append(item)
    return newList
            
#getting all phong material in the scene:
ex_materials = cmds.ls(type="phong")
ex_attrs = cmds.listAttr(ex_materials[0], v=True, se=True, s=True)


#create a new material node, not assigned yet as instance
newMaterialType = "aiStandard"
new_material = cmds.createNode(newMaterialType)
new_material_attrs = cmds.listAttr(new_material, v=True, se=True, s=True)

#get all the new material's attributes(different from Phong)
culled_attrs = FindShared(new_material_attrs, ex_attrs)

cmds.delete(new_material)

for mat in ex_materials:
    new_mat = cmds.shadingNode(newMaterialType, asShader=True, name='myShader')
    connection_list = cmds.listConnections(mat, d=True,p=True,s=False,t="shadingEngine")
    cmds.connectAttr('%s.outColor' % new_mat,connection_list[0], f=True)
    print connection_list[0]
    for attr in culled_attrs:
        value = cmds.getAttr("{0}.{1}".format(mat,attr))
        cmds.setAttr("{0}.{1}".format(new_mat,attr),value)
    cmds.delete(mat)