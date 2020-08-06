#ifndef FIRST_CMD_H
#define FIRST_CMD_H

#include "maya/MPxCommand.h"
#include "maya/MGlobal.h"
#include "maya/MObject.h"
using namespace Autodesk::Maya::OpenMaya20190000;


class FirstCmd : public MPxCommand
{
public:
    FirstCmd();
    virtual MStatus doIt(const MArgList &argList);
    static void *creator();
};

#endif