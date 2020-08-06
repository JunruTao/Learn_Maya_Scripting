#include "gNode.h"

MObject G_Node::inVar;
MObject G_Node::outVar;
MObject G_Node::f_magnitude;
MObject G_Node::f_mean;
MObject G_Node::f_variance;

//for local testing it is okay to use any id number
//however if it's an official release, you have to send an 
//email to Autodesk to request an unique ID
MTypeId G_Node::id(0x00003420);




G_Node::G_Node(){}

G_Node::~G_Node(){}

void* G_Node::creator()
{
    return new G_Node();
}

MStatus G_Node::compute(const MPlug& plug, MDataBlock& data)
{
    MStatus status;

    //test if the plug is output
    if(plug != outVar)
    {
        return MS::kUnknownParameter;
    }

    //data that stored in this node object(data owned by Maya)
    //only process that from data block send from maya
    float inputVar = data.inputValue(inVar, &status).asFloat();
    float maginitude = data.inputValue(f_magnitude, &status).asFloat();
    float mean = data.inputValue(f_mean, &status).asFloat();
    float variance = data.inputValue(f_variance, &status).asFloat();
    if (variance <= 0.0f)
    {
        variance = 0.001f;
    }

    float outputVar = maginitude * exp(-((inputVar - mean)*(inputVar - mean))/(2.0f * variance));

    MDataHandle hOutput = data.outputValue(outVar,&status);
    CHECK_MSTATUS_AND_RETURN_IT(status);
    hOutput.setFloat(outputVar);
    hOutput.setClean();//flag from `dirty` to `clean`;
    //or data.setClean(plug);

    return MS::kSuccess;
}


MStatus G_Node::initialize()
{
    MStatus status;
    //Maya Function Numeric Attribute object: in charge of creating attributes
    MFnNumericAttribute nAttr;

    outVar = nAttr.create("outvalue", "outvalue", MFnNumericData::kFloat);
    nAttr.setWritable(false);
    nAttr.setStorable(false);
    addAttribute(outVar);

    inVar = nAttr.create("invalue", "invalue", MFnNumericData::kFloat);
    nAttr.setKeyable(true);
    addAttribute(inVar);
    //see dependency graphic paradime [in --> out] <-- set `dirty`
    attributeAffects(inVar,outVar);

    f_magnitude = nAttr.create("magnitude", "magnitude", MFnNumericData::kFloat);
    nAttr.setKeyable(true);
    addAttribute(f_magnitude);
    attributeAffects(f_magnitude,outVar);

    f_mean = nAttr.create("mean", "mean", MFnNumericData::kFloat);
    nAttr.setKeyable(true);
    addAttribute(f_mean);
    attributeAffects(f_mean,outVar);

    f_variance = nAttr.create("variance", "variance", MFnNumericData::kFloat);
    nAttr.setKeyable(true);
    addAttribute(f_variance);
    attributeAffects(f_variance,outVar);
    

    return MS::kSuccess;
}