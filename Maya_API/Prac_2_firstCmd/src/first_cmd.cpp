#include "first_cmd.h"
using namespace Autodesk::Maya::OpenMaya20190000;



FirstCmd::FirstCmd(){}

//for all maya plug-ins. Returning a pointer to the this type of class
void* FirstCmd::creator()
{
    return new FirstCmd;
}

MStatus FirstCmd::doIt(const MArgList &argList)
{
    MGlobal::displayInfo("This is my first cmd plug-in");
    return MStatus::kSuccess;
}