---
title: "Modeler::CreateBodyFromBox"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Modeler/Modeler__CreateBodyFromBox.htm"
---

# Modeler::CreateBodyFromBox

This method is obsolete and has been superseded by [Modeler::CreateBodyFromBox3](sldworksAPI.chm::/Modeler/Modeler__CreateBodyFromBox3.htm).

Description

This method creates a temporary body from box dimensions.

Syntax (OLE Automation)

retval = Modeler.CreateBodyFromBox ( boxDimArray)

| Input: | (VARIANT) boxDimArray | VARIANT of type SafeArray of doubles (see Remarks ) |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Dispatch pointer to the resulting body |

Syntax (COM)

This method is obsolete and has been superseded by Modeler::ICreateBodyFromBox2.

status = Modeler->ICreateBodyFromBox ( boxDimArray, &retval )

| Input: | (double*) boxDimArray | Pointer to an array of 9 doubles |
| --- | --- | --- |
| Output: | (LPBODY*) retval | Pointer to the resulting body |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The input parameter is the following array of doubles:

[ boxFaceCenter[3], boxAxis[3], boxWidth, boxLength, boxHeight ]

where:

| boxFaceCenter [3] | XYZ location that represents the center of one of the box faces. |
| --- | --- |
| boxAxis [3] | XYZ direction. The box will be extruded along this vector from the boxFaceCenter location , a distance of boxHeight. |
| boxWidth | Box width. If boxAxis is parallel to the Z axis (0,0,1), then this value represents the dimension that is parallel to the X-axis; otherwise, the orientation is not defined. |
| boxLength | Box length. If boxAxis is parallel to the Z axis (0,0,1), then this value represents the dimension that is parallel to the Y axis; otherwise, the orientation is not defined. |
| boxHeight | Height to extrude along the boxAxis direction. If boxHeight is 0, a sheet body will be created of dimension boxWidth x boxLength and whose normal is defined by boxAxis . |
