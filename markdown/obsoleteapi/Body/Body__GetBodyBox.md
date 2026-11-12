---
title: "Body::GetBodyBox"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__GetBodyBox.htm"
---

# Body::GetBodyBox

This method is obsolete and has been superseded by [Body2::GetBodyBox](sldworksAPI.chm::/Body2/Body2__GetBodyBox.htm).

Description

This method gets the bounding body box.

Syntax (OLE Automation)

retval = Body.GetBodyBox ( )

| Return: | (VARIANT) retval | VARIANT of type SafeArray of 6 doubles representing the extents of the bounding box |
| --- | --- | --- |

Syntax (COM)

status = Body->IGetBodyBox ( BoxCorners )

| Input: | (double*) BoxCorners | Pointer to an array of 6 doubles representing the extents of the bounding box |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The X,Y,Z points returned are the lower and upper diagonal corners that bound the body with the box sides parallel to the X, Y and Z axes. The box dimensions returned enclose the body and are typically close to the minimum possible size, but not always.

The return value is an array of doubles:

[ XCorner1, YCorner1, ZCorner1, XCorner2, YCorner2, ZCorner2 ]
