---
title: "ModelDoc::CreatePoint2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreatePoint2.htm"
---

# ModelDoc::CreatePoint2

This method is obsolete and has been superseded by [ModelDoc2::CreatePoint2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__CreatePoint2.htm).

Description

This method creates a sketch point in the active 2D or 3D sketch.

Syntax (OLE Automation)

retval = ModelDoc.CreatePoint2 ( x, y, z )

| Input: | (double) x | X location of the point |
| --- | --- | --- |
| Input: | (double) y | Y location of the point |
| Input: | (double) z | Z location of the point; ignored for 2D sketches |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the newly created SketchPoint object; this value is NULL if the operation fails |

Syntax (COM)

status = ModelDoc->ICreatePoint2 ( x, y, z, &retval )

| Input: | (double) x | X location of the point |
| --- | --- | --- |
| Input: | (double) y | Y location of the point |
| Input: | (double) z | Z location of the point; ignored for 2D sketches |
| Output: | (LPSKETCHPOINT) retval | Pointer the newly created SketchPoint object; this value is NULL if the operation fails |
| Return: | (HRESULT) status | S_OK if successful; S_FALSE otherwise |

Remarks

This method creates a point in the active 2D or 3D sketch. If a sketch is not active, the point is not created and NULL is returned. You can check for an active sketch using ModelDoc::GetActiveSketch2.

ModelDoc::SetAddToDB and ModelDoc::SetDisplayWhenAdded increases performance during entity creation by adding entities directly to the SolidWorks database. ModelDoc::SetAddToDB also avoids inferencing.
