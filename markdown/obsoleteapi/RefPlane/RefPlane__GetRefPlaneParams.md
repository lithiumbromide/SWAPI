---
title: "RefPlane::GetRefPlaneParams"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/RefPlane/RefPlane__GetRefPlaneParams.htm"
---

# RefPlane::GetRefPlaneParams

This method is obsolete and has been superseded by [RefPlane::Transform](sldworksAPI.chm::/RefPlane/RefPlane__Transform.htm).

Description

This method retrieves information about a reference plane.

Syntax (OLE Automation)

retval = RefPlane.GetRefPlaneParams ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray containing an array of doubles (see Remarks ) |
| --- | --- | --- |

Syntax (COM)

status = RefPlane->IGetRefPlaneParams ( retval )

| Output: | (double*) retval | Pointer to an array of doubles (see Remarks ) |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

To get the RefPlane interface, you must get the reference plane as a feature, and then use Feature::GetSpecificFeature to return the RefPlane object.

The return value is the following array of doubles:

[ Origin[3], Xvector[3], NormalVector[3] ]

| Where... | Is an array of three values describing... |
| --- | --- |
| Origin[3] | x,y,z origin of the reference plane. This value locates the model origin in relation to the coordinate system of the plane. The value is in terms of the reference planes coordinate system. |
| Xvector[3] | x-axis vector of the reference plane. |
| NormalVector[3] | normal vector of the reference plane. |
