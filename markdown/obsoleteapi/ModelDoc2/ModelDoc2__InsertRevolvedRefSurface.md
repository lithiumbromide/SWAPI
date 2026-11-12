---
title: "ModelDoc2::InsertRevolvedRefSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertRevolvedRefSurface.htm"
---

# ModelDoc2::InsertRevolvedRefSurface

This method is obsolete and has been superseded by [FeatureManager::InsertRevolvedRefSurface](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertRevolvedRefSurface.htm).

Description

This method creates a revolved reference surface by revolving a profile around a centerline.

Syntax (OLE Automation)

void ModelDoc2.InsertRevolvedRefSurface ( Angle, ReverseDir, Angle2, RevType )

| Input: | (double) Angle | Angle of revolution in radians |
| --- | --- | --- |
| Input: | (BOOL) ReverseDir | Angle is positive or negative ( TRUE or FALSE) |
| Input: | (double) Angle2 | Angle of revolution in radians |
| Input: | (int) RevType | Type of revolution |

Syntax (COM)

status = ModelDoc2->InsertRevolvedRefSurface ( Angle, ReverseDir, Angle2, RevType )

| Input: | (double) Angle | Angle of revolution in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) ReverseDir | Angle is positive or negative ( TRUE or FALSE) |
| Input: | (double) Angle2 | Angle of revolution in radians |
| Input: | (int) RevType | Type of revolution |
| Return: | (HRESULT) status | S_OK if euccessful |

Remarks

Make the selections using ModelDocExtension::SelectByID2 before calling this method. See the SolidWorks Help for information about what entities are valid for selection.

The revType argument can be one of these values:

- 0 = One direction revolution.
- 1 = MidPlane revolution. For this type of revolve, the angle specification specifies the full revolution. The angle to revolve is (angle/2 ) on either side of the sketch. The reverseDir argument has no affect.
- 2 = Two direction revolution. For a two direction revolve, the angle is the angle to revolve in Direction1 and angle2 is the angle to revolve in Direction2.

This method does not support 3D sketches.
