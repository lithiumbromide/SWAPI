---
title: "ModelDoc2::CreateEllipse2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__CreateEllipse2.htm"
---

# ModelDoc2::CreateEllipse2

This method is obsolete and has been superseded by [SketchManager::CreateEllipse](sldworksAPI.chm::/SketchManager/SketchManager__CreateEllipse.htm).

Description

This method creates an ellipse using the specified center point and points.

Syntax (OLE Automation)

retval = ModelDoc2.CreateEllipse2 ( centerX, centerY, centerZ, majorX, majorY, majorZ, minorX, minorY, minorZ )

| Input: | (double) centerX | X values for the ellipse center point |
| --- | --- | --- |
| Input: | (double) centerY | Y values for the ellipse center point |
| Input: | (double) centerZ | Z values for the ellipse center point |
| Input: | (double) majorX | X values for a point on the ellipse and on the major axis |
| Input: | (double) majorY | Y values for a point on the ellipse and on the major axis |
| Input: | (double) majorZ | Z values for a point on the ellipse and on the major axis |
| Input: | (double) minorX | X values for a point on the ellipse and on the minor axis |
| Input: | (double) minorY | Y values for a point on the ellipse and on the minor axis |
| Input: | (double) minorZ | Z values for a point on the ellipse and on the minor axis |
| Return: | (LPDISPATCH) retval | Pointer to the Dispatch object of the ellipse that was created |

Syntax (COM)

status = ModelDoc2->ICreateEllipse2 ( centerX, centerY, centerZ, majorX, majorY, majorZ, minorX, minorY, minorZ, &retval )

| Input: | (double) centerX | X values for the ellipse center point |
| --- | --- | --- |
| Input: | (double) centerY | Y values for the ellipse center point |
| Input: | (double) centerZ | Z values for the ellipse center point |
| Input: | (double) majorX | X values for a point on the ellipse and on the major axis |
| Input: | (double) majorY | Y values for a point on the ellipse and on the major axis |
| Input: | (double) majorZ | Z values for a point on the ellipse and on the major axis |
| Input: | (double) minorX | X values for a point on the ellipse and on the minor axis |
| Input: | (double) minorY | Y values for a point on the ellipse and on the minor axis |
| Input: | (double) minorZ | Z values for a point on the ellipse and on the minor axis |
| Output: | (LPSKETCHSEGMENT) retval | Pointer to the newly created ellipse |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method creates an ellipse in the active 2D sketch. If a sketch is not active, then a new sketch is created. You can check for an active sketch using ModelDoc2::GetActiveSketch2.

| Application | Objects |
| --- | --- |
| OLE | You can define a new ISketchSegment or ISketchEllipse object using the returned Dispatch pointer. Visual Basic applications interpret the pointer for you automatically, so you can use the returned object to call SketchSegment or SketchEllipse functions. |
| COM | The object pointer returned from this method can be used to call any APIs on the SketchSegment interface. The underlying SketchEllipse object can be obtained using QueryInterface on the returned SketchSegment object. |

ModelDoc2::SetAddToDB and ModelDoc2::SetDisplayWhenAdded increase performance during entity creation by adding entities directly to the SolidWorks database.

ModelDoc2::SetAddToDB avoids some of the peculiarities involved with creating entities via the user interface, such as inferencing, automatic relations, and snapping to the grid. Adding entities directly to the database also increases the performance of this method. When you are done creating entities, restore ModelDoc2::SetAddToDB(False)to its normal operating mode.

This method also works with ModelDoc2::SetDisplayWhenAdded. If you called ModelDoc2::SetAddToDB(True), additional performance can be gained by calling ModelDoc2::SetDisplayWhenAdded(False) to disable immediate display of entities as they are added to the database. When you are done creating all of your sketch entities, you must redraw your document window (see ModelDoc2::GraphicsRedraw2) to see the entities you added. You should also restore the original display settings by calling ModelDoc2::SetDisplayWhenAdded(True).

To create a partial ellipse, use ModelDoc2::CreateEllipticalArcByCenter.
