---
title: "DatumOrigin::GetAxisPoints"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DatumOrigin/DatumOrigin__GetAxisPoints.htm"
---

# DatumOrigin::GetAxisPoints

This method is obsolete and has been superseded by [DatumOrigin::GetAxisPoint2](sldworksAPI.chm::/DatumOrigin/DatumOrigin__GetAxisPoints2.htm).

Description

This method gets the points that define the geometry of this datum origin.

Syntax (OLE Automation)

retval = DatumOrigin.GetAxisPoints ()

| Output: | (VARIANT*) retval | VARIANT of type SafeArray of 4 doubles (see Remarks ) |
| --- | --- | --- |

Syntax (COM)

status = DatumOrigin->IGetAxisPoints ( retval)

| Output: | (double*) retval | Pointer to an array of 4 doubles (see Remarks ) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method gives the end user control over the shape of the symbol.

The array of 4 doubles is 2 (X,Y) coordinates in drawing space:

- The first coordinate (array items 0 and 1) is the tip of the arrowhead on the X leader portion of the symbol.
- The second coordinate (array items 2 and 3) is the tip of the arrowhead on the Y leader portion of the symbol.

The end user has this control via the selection drag handles of the symbol.
