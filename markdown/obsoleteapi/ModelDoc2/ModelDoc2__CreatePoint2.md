---
title: "ModelDoc2::CreatePoint2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreatePoint2.htm"
---

# ModelDoc2::CreatePoint2

This method is obsolete and superseded [SketchManager::CreatePoint](sldworksAPI.chm::/SketchManager/SketchManager__CreatePoint.htm).

Description

This method creates a sketch point in the active 2D or 3D sketch.

Syntax (OLE Automation)

retval = ModelDoc2.CreatePoint2 ( x, y, z )

| Input: | (double) x | X location of the point |
| --- | --- | --- |
| Input: | (double) y | Y location of the point |
| Input: | (double) z | Z location of the point; ignored for 2D sketches |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the newly created sketch point; this value is NULL if the operation fails |

Syntax (COM)

status = ModelDoc2->ICreatePoint2 ( x, y, z, &retval )

| Input: | (double) x | X location of the point |
| --- | --- | --- |
| Input: | (double) y | Y location of the point |
| Input: | (double) z | Z location of the point; ignored for 2D sketches |
| Output: | (LPSKETCHPOINT) retval | Pointer to a newly created sketch point; this value is NULL if the operation fails |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method creates a point in the active 2D or 3D sketch. If a sketch is not active, the point is not created and NULL is returned. Use ModelDoc2::GetActiveSketch2 to check to see if the sketch is active.

ModelDoc2::SetAddToDB and ModelDoc2::SetDisplayWhenAdded increase performance during entity creation by adding entities directly to the SolidWorks database. ModelDoc2::SetAddToDB also avoids inferencing.
