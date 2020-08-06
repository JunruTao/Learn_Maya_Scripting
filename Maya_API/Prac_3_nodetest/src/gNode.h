#ifndef GNODE_H
#define GNODE_H

#include <maya/MPxNode.h>
#include <maya/MStatus.h>
#include <maya/MObject.h>
#include <maya/MFnNumericAttribute.h>
#include <math.h>

//This is a gaussian function node
class G_Node : public MPxNode
{
public:
    G_Node();
    virtual ~G_Node();
    static void* creator();

    //creating a maya node object, maya will call for compute function
    virtual MStatus compute(const MPlug& plug, MDataBlock& data);

    //use a function to initialise the variables; this will pass to the registry
    static MStatus initialize();

    static MObject inVar;
    static MObject outVar;
    
    //reference, gaussian function: https://en.wikipedia.org/wiki/Gaussian_function
    static MObject f_magnitude;
    static MObject f_mean;
    static MObject f_variance;

    static MTypeId id;


};


#endif