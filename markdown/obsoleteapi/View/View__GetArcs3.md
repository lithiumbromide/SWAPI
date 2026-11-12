---
title: "View::GetArcs3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetArcs3.htm"
---

# View::GetArcs3

This method is obsolete and has been superseded by [View::GetArcs4](sldworksAPI.chm::/View/View__GetArcs4.htm).

Description

This method returns information for each arc that was sketched in this drawing view.

Syntax (OLE Automation)

retval = View.GetArcs3 ( )

| Return: | (VARIANT) retval | VARIANT of type SafeArray containing an array of doubles |
| --- | --- | --- |

Syntax (COM)

status = View->IGetArcs3 ( &retval )

| Output: | (double)retval | Pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method returns arcs that have been deliberately sketched in this drawing view. All part and assembly geometry shown in a drawing view is represented by polylines. To access the polylines, use View::GetPolylines3.

Return value is an array of doubles with the format:

[ Color, LineType, LineStyleIndex, LineWeight, StartPt[3], EndPt[3], CenterPt[3], RotDir, ... ]

where:

Color is the COLORREF returned as an integer. Return value could be 0 or -1 for default color.

LineType is the line type. Valid returns are found in the swLineTypes_e enumeration. A lineType is a combination of a lineStyle and lineWeight.

LineStyleIndex is the index location of this line style inside SolidWorks Line Style Manager.

LineWeight is an integer value defining the line weight

StartPt[3] equals an array of 3 doubles (X,Y,Z) describing the start point.

EndPt[3] equal an array of 3 doubles (X,Y,Z) describing the end point. If the arc is closed, then this is the same point as the StartPt.

CenterPt[3] is an array of 3 doubles (X,Y,Z) describing the center point.

RotDir equals the rotational direction (CW = -1, CCW = 1)

...

This set of data repeats for each arc in the view. The size of the array is (NumArcs * 14). To determine the number of arcs, use View::GetArcCount.

The data returned from this method is in terms of view space. If you want the data in terms of sheet space (for example, the 0,0 origin being the lower-left corner of the sheet), then combine this data with the three return values from View::GetXForm.
