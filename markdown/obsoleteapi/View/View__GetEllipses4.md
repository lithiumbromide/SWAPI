---
title: "View::GetEllipses4"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetEllipses4.htm"
---

# View::GetEllipses4

This method is obsolete and has been superseded by [View::GetEllipses5](sldworksAPI.chm::/View/View__GetEllipses5.htm).

Description

This method gets all the ellipses that were sketched in this drawing view.

Syntax (OLE Automation)

retval = View.GetEllipses4 ( )

| Return: | (VARIANT)retval | VARIANT of type SafeArray |
| --- | --- | --- |

Syntax (COM)

status = View->IGetEllipses4 ( &retval )

| Output: | (double)retval | Pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method only returns ellipses that have been deliberately sketched in this drawing view. All part and assembly geometry shown in a drawing view is represented by polylines. To access the polylines, use View::GetPolylines3.

The return values are in an array of doubles:

[ Color, LineType, LineStyleIndex, LineWeight, StartPt[3], EndPt[3], CenterPt[3], MajorPt[3], MinorPt[3],Direction ... ]

where:

Color: COLORREF returned as an integer. Return value could be 0 or -1 for default color.

LineType: line type. Valid returns as defined in swLineTypes_e. A lineType is a combination of a lineStyle and lineWeight.

LineStyleIndex: index location of this line style inside SolidWorks line style manager.

LineWeight: integer value defining the line weight.

StartPt[3]: array of 3 doubles (X,Y,Z) describing the ellipse start point

EndPt[3]: array of 3 doubles (X,Y,Z) describing the ellipse end point. If the ellipse is closed, then this will be the same point as the StartPt..

CenterPt[3]: array of 3 doubles (X,Y,Z) describing the ellipse center point.

MajorPt[3]: array of 3 doubles (X,Y,Z) describing a point on the ellipse and on the major axis.

MinorPt[3]: array of 3 doubles (X,Y,Z) describing a point on the ellipse and on the minor axis.

Direction: -1 for Clockwise, +1 for counterclockwise.

This set of data repeats for each ellipse in the view. The size of the array is (NumEllipses * 20). To determine the number of ellipses, use View::GetEllipseCount.

The data returned from this method is in terms of view space. If you want the data in terms of sheet space (for example, the 0,0 origin being the lower-eft corner of the sheet), then combine this data with the three return values from View::GetXForm.
