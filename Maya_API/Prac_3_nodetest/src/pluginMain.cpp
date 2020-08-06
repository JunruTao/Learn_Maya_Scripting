#include "gNode.h"
#include <maya/MFnPlugin.h>


//These 2 functions are required for all plug-ins

MStatus initializePlugin(MObject obj)
{
    MStatus status;

    MFnPlugin fnPlugin(obj, "Junru Tao", "1.0", "Any");

    status = fnPlugin.registerNode("gNode", G_Node::id, G_Node::creator, G_Node::initialize);
    CHECK_MSTATUS_AND_RETURN_IT(status);

    return MStatus::kSuccess;
}

MStatus uninitializePlugin(MObject obj)
{
    MStatus status;

    MFnPlugin fnPlugin(obj);

    status = fnPlugin.deregisterNode(G_Node::id);
    CHECK_MSTATUS_AND_RETURN_IT(status);

    return MStatus::kSuccess;
}


/*
#Python Command in maya

> import maya.cmds as cmd
> cmds.gNode()

*/