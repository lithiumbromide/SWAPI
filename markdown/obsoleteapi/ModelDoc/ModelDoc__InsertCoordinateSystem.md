---
title: "ModelDoc::InsertCoordinateSystem"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertCoordinateSystem.htm"
---

# ModelDoc::InsertCoordinateSystem

This method is obsolete and has been superseded by [ModelDoc2::InsertCoordinateSystem](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertCoordinateSystem.htm).

Description

This method inserts a coordinate system based on selections.

Syntax (OLE Automation)

void ModelDoc.InsertCoordinateSystem ( xFlipped, yFlipped, zFlipped )

| Input: | (BOOL) xFlipped | TRUE to flip the x direction |
| --- | --- | --- |
| Input: | (BOOL) yFlipped | TRUE to flip the y direction |
| Input: | (BOOL) zFlipped | TRUE to flip the z direction |

Syntax (COM)

status = ModelDoc->InsertCoordinateSystem ( xFlipped, yFlipped, zFlipped )

| Input: | (VARIANT_BOOL) xFlipped | TRUE to flip the x direction |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) yFlipped | TRUE to flip the y direction |
| Input: | (VARIANT_BOOL) zFlipped | TRUE to flip the z direction |
| Return: | (HRESULT) status | S_OK if successful. |

Remarks

Programmatic selections should be made with a SelectByMark method. Use the following marks with your SelectByMark selections:

- 1 Origin
- 2 X Axis
- 4 Y Axis
- 8 Z Axis

This method does not require all three axis to be selected. The behavior is the same as interactively creating a coordinate system by selecting Insert, Reference Geometry, Coordinate System. See SolidWorks Help for more information.
