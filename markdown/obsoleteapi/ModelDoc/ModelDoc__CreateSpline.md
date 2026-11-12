---
title: "ModelDoc::CreateSpline"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__CreateSpline.htm"
---

# ModelDoc::CreateSpline

This method is obsolete and has been superseded by [ModelDoc2::CreateSpline](../ModelDoc2/ModelDoc2__CreateSpline.htm).

Description

This method creates a spline passing through the given points.

Syntax (OLE Automation)

retval = ModelDoc.CreateSpline ( pointData )

| Input: | (VARIANT) pointData | Set of X,Y,Z point coordinates to use in creating the spline |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to the Dispatch object of the spline that was created |

Syntax (COM)

status = ModelDoc->ICreateSpline ( pointCount, pointData, &retval )

| Input: | (long) pointCount | Number of points in the pointData array |
| --- | --- | --- |
| Input: | (double*) pointData | Set of X,Y,Z point coordinates to use in creating the spline, |
| Output: | (LPSKETCHSEGMENT) retval | Pointer to the spline that was created |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method creates a spline in the active 2D sketch. If a sketch is not active, then a new sketch is created. You can check for an active sketch using ModelDoc::GetActiveSketch2.

If you are creating a sketch spline from a macro, then you must use ModelDoc::SketchSpline. You cannot use ModelDoc::CreateSpline because it requires an array of points.

The pointData array is a set of, at least two X, Y, Z values. The X value for the start point of the spline is pointData[0], the Y value for the start point is pointData[1], and the Z value for the start point is pointData[2]. The X value for the next point is pointData[3], and so on. For the COM interface, the total number of points in the array must be passed in. For the OLE interface, the total number of points is determined automatically within SolidWorks, by taking the UBound of the pointData VARIANT, and dividing by 3, so dimension that array correctly.

For COM applications, the object pointer returned from this method can be used to call any of the SketchSegment functions. The underlying SketchSpline object can be obtained using QueryInterface on the returned SketchSegment object.

OLE applications can define a new SketchSegment or SketchSpline object using the returned dispatch pointer. Visual Basic applications interpret the pointer for you automatically, so you can use the returned object to call SketchSegment or SketchEllipse functions.

This method does not work with ModelDoc::SetAddToDB or ModelDoc::SetDisplayWhenAdded. It always adds the spline directly to the database, as if ModelDoc::SetAddToDB(True) was in effect. You must redraw your document window to see the entities that you added, as if ModelDoc::SetDisplayWhenAdded(False) was in effect.

In 2D sketches, SolidWorks ignores the Z value in pointData.
