---
title: "ModelDoc::CreateCircleByRadius2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateCircleByRadius2.htm"
---

# ModelDoc::CreateCircleByRadius2

## ModelDoc ::CreateCircleByRadius2

This method is obsolete and has been superseded by [ModelDoc2::CreateCircleByRadius2](../ModelDoc2/ModelDoc2__CreateCircleByRadius2.htm).

Description

This method creates a circle based on a center point and a specified radius.

Syntax (OLE Automation)

retval = ModelDoc.CreateCircleByRadius2 ( xc, yc, zc, radius )

| Input: | (double) xc | X value of the circle center point, in meters |
| --- | --- | --- |
| Input: | (double) yc | Y value of the circle center point, in meters |
| Input: | (double) zc | Z value of the circle center point, in meters |
| Input: | (double) radius | Radius of the circle, in meters |
| Return: | ( LPDISPATCH ) retval | Pointer to the Dispatch object of the circle that was created |

Syntax (COM)

status = ModelDoc->ICreateCircleByRadius2 ( xc, yc, zc, radius, &retval )

| Input: | (double) xc | X value of the circle center point, in meters |
| --- | --- | --- |
| Input: | (double) yc | Y value of the circle center point, in meters |
| Input: | (double) zc | Z value of the circle center point, in meters |
| Input: | (double) radius | Radius of the circle, in meters |
| Output: | ( LPSKETCHSEGMENT ) retval | Pointer to the circle that was created |
| Return: | ( HRESULT ) status | S_OK if successful |

Remarks

This method creates a full circle in the active 2D sketch. If a sketch is not active, then a new sketch will be created. You can check for an active sketch using the ModelDoc::GetActiveSketch2 function.

For COM applications, the object pointer returned from this method can be used to call any APIs on the SketchSegment interface. The underlying SketchArc object can be obtained using QueryInterface on the returned SketchSegment object.

OLE applications can simply define a new SketchSegment or SketchArc object using the returned dispatch pointer. Visual Basic applications will interpret the pointer for you automatically, so you can use the returned object to call SketchSegment or SketchArc functions.

ModelDoc::SetAddToDB and ModelDoc::SetDisplayWhenAdded increase performance during entity creation by adding entities directly to the SolidWorks database.

ModelDoc::SetAddToDB avoids some of the peculiarities involved with creating entities via the user interface, such as inferencing, automatic relations, and snapping to the grid. Adding entities directly to the database also significantly increases the performance of this API. When you are done creating entities, it is important to call ModelDoc::SetAddToDB(False), to restore SolidWorks to its normal operating mode.

This API also works in conjunction with [ModelDoc::SetDisplayWhenAdded](ModelDoc__SetDisplayWhenAdded.htm). If you have called [ModelDoc::SetAddToDB](ModelDoc__SetAddToDB.htm)(True), additional performance can be gained by calling [ModelDoc::SetDisplayWhenAdded](ModelDoc__SetDisplayWhenAdded.htm)(False) to disable immediate display of entities as they are added to the database. When you are done creating all of your sketch entities, you will need to redraw your document window (refer to [ModelDoc::GraphicsRedraw2](ModelDoc__GraphicsRedraw2.htm)) to see the entities you've added. You should also restore the original display settings by calling [ModelDoc::SetDisplayWhenAdded](ModelDoc__SetDisplayWhenAdded.htm)(True).

The create a circle using a center point and a point on the circle, refer to [ModelDoc::CreateCircle2](ModelDoc__CreateCircle2.htm). To create a partial arc, refer to ModelDoc::CreateArc2.
