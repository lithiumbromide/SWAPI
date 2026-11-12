---
title: "ModelDoc::CreateLine2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateLine2.htm"
---

# ModelDoc::CreateLine2

This method is obsolete and has been superseded by [ModelDoc2::CreateLine2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__CreateLine2.htm).

Description

This method creates a sketch line in the currently active 2D or 3D sketch.

Syntax (OLE Automation)

retval = ModelDoc.CreateLine2 ( xStart, yStart, zStart, xEnd, yEnd, zEnd )

| Input: | (double) xStart | X value of the line start point |
| --- | --- | --- |
| Input: | (double) yStart | Y value of the line start point |
| Input: | (double) zStart | Z value of the line start point |
| Input: | (double) xEnd | X value of the line end point |
| Input: | (double) yEnd | Y value of the line end point |
| Input: | (double)zEnd | Z value of the line end oint |
| Return: | (LPDISPATCH) retval | Pointer to a dispatch object, the newly created SketchSegment object; if the operation fails, then NULL is returned |

Syntax (COM)

status = ModelDoc->ICreateLine2 ( xStart, yStart, zStart, xEnd, yEnd, zEnd, &retval )

| Input: | (double) xStart | X value of the line start point |
| --- | --- | --- |
| Input: | (double) yStart | Y value of the line start point |
| Input: | (double) zStart | Z value of the line start point |
| Input: | (double) xEnd | X value of the line end point |
| Input: | (double) yEnd | Y value of the line end point |
| Input: | (double) zEnd | Z value of the line end oint |
| Output: | (LPSKETCHSEGMENT) retval | Pointer to the newly created SketchSegment object; if the operation fails, then NULL is returned |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

If a sketch is not active, then the line is not be created and NULL is returned. You can check for an active sketch using the ModelDoc::GetActiveSketch2 method.

For COM applications, obtain the underlying SketchLine object using QueryInterface on the SketchSegment object returned. C++ Dispatch applications can define a new SketchLine or SketchSegment object, which uses this dispatch pointer. Visual Basic applications interpret the pointer for you automatically so you can use the returned object to call SketchSegment or SketchLine functions.

ModelDoc::SetAddToDB and ModelDoc::SetDisplayWhenAdded increase performance during entity creation by adding entities directly to the SolidWorks database. ModelDoc::SetAddToDB avoids inferencing.
