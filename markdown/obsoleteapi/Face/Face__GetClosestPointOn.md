---
title: "Face::GetClosestPointOn"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__GetClosestPointOn.htm"
---

# Face::GetClosestPointOn

This method is obsolete and has been superseded by [Face2::GetClosestPointOn](sldworksAPI.chm::/Face2/Face2__IGetClosestPointOn.htm).

Description

This method uses the X,Y,Z input point and return the closest point on the face.

Syntax (OLE Automation)

retval = Face.GetClosestPointOn ( x, y, z)

| Input: | (double) x | X value of the input point |
| --- | --- | --- |
| Input: | (double) y | Y value of the input point |
| Input: | (double) z | Z value of the input point |
| Return: | (VARIANT) retval | SafeArray of five doubles representing the X, Y, Z point on the sace followed by the U, V parameter on the face that is closest to the input point |

Syntax (COM)

status = Face->IGetClosestPointOn ( x, y, z, retval )

| Input: | (double) x | X value of the input point |
| --- | --- | --- |
| Input: | (double) y | Y value of the input point |
| Input: | (double) z | Z value of the input point |
| Output: | (double*) retval | Pointer to an array of five doubles representing the X, Y, Z point on the face followed by the U, V parameter on the face that is closest to the input point |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method returns only one point, regardless of how many points achieve the minimum distance.
