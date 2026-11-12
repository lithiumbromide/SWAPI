---
title: "ModelDoc2::CreateCircle2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreateCircle2.htm"
---

# ModelDoc2::CreateCircle2

This method is obsolete and has been superseded by [SketchManager::CreateCircle](sldworksAPI.chm::/SketchManager/SketchManager__CreateCircle.htm).

Description

This method creates a circle based on a center point and a point on the circle.

Syntax (OLE Automation)

retval = ModelDoc2.CreateCircle2 ( xc, yc, zc, xp, yp, zp )

| Input: | (double) xc | X value of the circle center point, in meters |
| --- | --- | --- |
| Input: | (double) yc | Y value of the circle center point, in meters |
| Input: | (double) zc | Z value of the circle center point, in meters |
| Input: | (double) xp | X value of the point on the circle, in meters |
| Input: | (double) yp | Y value of the point on the circle, in meters |
| Input: | (double) zp | Z value of the point on the circle, in meters |
| Return: | (LPDISPATCH) retval | Pointer to the Dispatch object of the circle that was created |

Syntax (COM)

status = ModelDoc2->ICreateCircle2 ( xc, yc, zc, xp, yp, zp, &retval )

| Input: | (double) xc | X value of the circle center point, in meters |
| --- | --- | --- |
| Input: | (double) yc | Y value of the circle center point, in meters |
| Input: | (double) zc | Z value of the circle center point, in meters |
| Input: | (double) xp | X value of the point on the circle, in meters |
| Input: | (double) yp | Y value of the point on the circle, in meters |
| Input: | (double) zp | Z value of the point on the circle, in meters |
| Output: | (LPSKETCHSEGMENT) retval | Pointer to the circle that was created |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method creates a full circle in the active 2D sketch. If a sketch is not active, then a new sketch is created. You can check for an active sketch using ModelDoc2::GetActiveSketch2.

For COM applications, the object pointer returned from this function can be used to call any APIs on the SketchSegment interface. The underlying SketchArc object can be obtained using QueryInterface on the returned SketchSegment object.

OLE applications can define a new ISketchSegment or ISketchArc object using the returned dispatch pointer. Visual Basic applications interpret the pointer for you automatically, so you can use the returned object to call SketchSegment or SketchArc functions.

ModelDoc2::SetAddToDB and ModelDoc2::SetDisplayWhenAdded increase performance during entity creation by adding entities directly to the SolidWorks database.

ModelDoc2::SetAddToDB avoids some of the peculiarities involved with creating entities via the UI, such as inferencing, automatic relations, and snapping to the grid. Adding entities directly to the database significantly increases the performance of this API. When you are done creating entities, it is important to calling ModelDoc2::SetAddToDB(False) to restore SolidWorks to its normal operating mode.

This API also works in conjunction with ModelDoc2::SetDisplayWhenAdded. If you have called ModelDoc2::SetAddToDB(True), additional performance can be gained by calling ModelDoc2::SetDisplayWhenAdded(False) to disable immediate display of entities as they are added to the database. When you are done creating all of your sketch entities, you must redraw your document window (see ModelDoc2::GraphicsRedraw2) to see the entities you have added. You should also restore the original display settings by calling ModelDoc2::SetDisplayWhenAdded(True).

To create a circle using a center point and radius, see ModelDoc2::CreateCircleByRadius2. To create a partial arc, see ModelDoc2::CreateArc2.
