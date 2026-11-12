---
title: "Face::FaceInSurfaceSense"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__FaceInSurfaceSense.htm"
---

# Face::FaceInSurfaceSense

This method is obsolete and has been superseded by [Face2::FaceInSurfaceSense](sldworksAPI.chm::/Face2/Face2__FaceInSurfaceSense.htm).

Description

This method checks if the face normal has the opposite direction (sense) as the underlying surface.

Syntax (OLE Automation)

retval = Face.FaceInSurfaceSense ()

| Return: | (BOOL) retval | TRUE if face normal and surface normal are in the opposite direction, FALSE if face normal and surface normal are in same direction |
| --- | --- | --- |

Syntax (COM)

status = Face->FaceInSurfaceSense ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if face normal and surface normal are in the opposite direction, FALSE if face normal and surface normal are in same direction |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method is important because the underlying surface geometry created by parasolids can have an orientation with which its normal vector points toward or away from the body material. The normal vector of faces, however, is always directed away from the body material.
