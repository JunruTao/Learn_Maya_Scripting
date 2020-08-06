#include "first_cmd.h"
#include "maya/MFnPlugin.h"

using namespace Autodesk::Maya::OpenMaya20190000;

//These 2 functions are required for all plug-ins

MStatus initializePlugin(MObject obj)
{
    MStatus status;

    MFnPlugin fnPlugin(obj, "Junru Tao", "1.0", "Any");

    status = fnPlugin.registerCommand("myCmd", FirstCmd::creator);
    CHECK_MSTATUS_AND_RETURN_IT(status);

    return MStatus::kSuccess;
}

MStatus uninitializePlugin(MObject obj)
{
    MStatus status;

    MFnPlugin fnPlugin(obj);

    status = fnPlugin.deregisterCommand("myCmd");
    CHECK_MSTATUS_AND_RETURN_IT(status);

    return MStatus::kSuccess;
}


/*
#Python Command in maya

> import maya.cmds as cmd
> cmds.myCmd()

*/