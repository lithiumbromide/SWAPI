---
title: "View::GetParabolas"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetParabolas.htm"
---

# View::GetParabolas

This method is obsolete and has been superseded by [View::GetParabolas2](sldworksAPI.chm::/View/View__GetParabolas2.htm).

Description

This method gets all of the parabolas in the view.

Syntax (OLE Automation)

retval = View.GetParabolas ( )

| Return: | (VARIANT) retval | VARIANT of type SafeArray |
| --- | --- | --- |

Syntax (COM)

status = View->IGetParabolas ( &retval )

| Output: | (double) retval | pointer to an array of doubles |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return values are in an array of doubles:

[ Color, LineType, LineStyleIndex, LineWeight, StartPt[3], EndPt[3], FocusPt[3], ApexPt[3] ... ]

where:

Color = COLORREF returned as an integer. Return value could be 0 or -1 for default color.

LineType = line type. Valid returns as defined in swLineTypes_e. A lineType is a combination of a lineStyle and lineWeight.

LineStyleIndex = index location of this line style inside SolidWorks Line Style Manager.

LineWeight = integer value defining the line weight.

StartPt[3] = array of 3 doubles (X,Y,Z) describing the parabola start point.

EndPt[3] = array of 3 doubles (X,Y,Z) describing the parabola end point.

FocusPt[3] = array of 3 doubles (X,Y,Z) describing the parabola focus Point.

ApexPt[3] = array of 3 doubles (X,Y,Z) describing the parabola apex Point.

This set of data repeats for each parabola in the view. The size of the array is (NumParabolas * 16). To determine the number of parabolas, use View::GetParabolaCount.
