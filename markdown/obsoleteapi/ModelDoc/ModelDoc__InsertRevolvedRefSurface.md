---
title: "ModelDoc::InsertRevolvedRefSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertRevolvedRefSurface.htm"
---

# ModelDoc::InsertRevolvedRefSurface

This method is obsolete and has been superseded by [ModelDoc2::InsertRevolvedRefSurface](../ModelDoc2/ModelDoc2__InsertRevolvedRefSurface.htm).

Description

The method creates a revolved reference surface by revolving a profile around a centerline.

Syntax (OLE Automation)

void ModelDoc.InsertRevolvedRefSurface ( Angle, ReverseDir, Angle2, RevType )

| Input: | (double) Angle | Angle of revolution in radians |
| --- | --- | --- |
| Input: | (BOOL) ReverseDir | Angle is positive or negative ( TRUE or FALSE) |
| Input: | (double) Angle2 | Angle of revolution in radians |
| Input: | (int) RevType | Type of revolution |

Syntax (COM)

status = ModelDoc->InsertRevolvedRefSurface ( Angle, ReverseDir, Angle2, RevType )

| Input: | (double) Angle | Angle of revolution in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) ReverseDir | Angle is positive or negative ( TRUE or FALSE) |
| Input: | (double) Angle2 | Angle of revolution in radians |
| Input: | (int) RevType | Type of revolution |
| Return: | (HRESULT) status | S_OK if Successful |

Remarks

This method is the same as interactively creating a planar surface by selecting Insert, Reference Geometry, Revolved Surface. See SolidWorks Help for more information about what entities are valid for selection.

Make the selections using ModelDoc::SelectByID before calling this function.

The RevType argument can be one of the following values:

- 0 - One direction revolution.
- 1 - MidPlane revolution. For this type of revolve, the angle specification specifies the full revolution. The angle to be revolved is (angle/2 ) on either side of the sketch. The ReverseDir argument has no affect.
- 2 - Two direction revolution. For a two direction revolve, the angle is the angle to be revolved in direction 1 and angle2 is the angle to be revolved in direction 2.
