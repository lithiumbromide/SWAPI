---
title: "Face::GetBox"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetBox.htm"
---

# Face::GetBox

This method is obsolete and has been superseded by [Face2::GetBox](sldworksAPI.chm::/Face2/Face2__GetBox.htm).

Description

This method gets the box boundaries for this face.

Syntax (OLE Automation)

retval = Face.GetBox ()

| Return: | (VARIANT) retval | VARIANT SafeArray of 6 doubles containing the two diagonal points that bound the component |
| --- | --- | --- |

Syntax (COM)

status = Face->IGetBox ( retval )

| Output: | (double*) retval | Two diagonal points which bound the component in the form of a pointer to an array of 6 doubles |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The X,Y,Z points returned are the lower and upper diagonal corners that bound the face with the box sides parallel to the X, Y and Z axes. The box dimensions returned enclose the face and are typically close to the minimum possible size, but not always.

The return value is an array of doubles as follows:

```vb
[ XCorner1, YCorner1, ZCorner1, XCorner2, YCorner2, ZCorner2 ]
```
